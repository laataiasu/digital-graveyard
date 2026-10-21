---
title: "Bypassing HyperOS Restrictions for Circle to Search on Custom Launchers"
date: 2026-10-21
tags: [android, hyperos, xiaomi, reverse-engineering, launcher]
publish_external: true
status: seedling
---

# Bypassing HyperOS Restrictions for Circle to Search on Custom Launchers

## The Problem
On Xiaomi devices running **HyperOS** (tested on Xiaomi 14T Pro / `rothko_global`), setting any third-party launcher (e.g. Nova, Lawnchair, or custom launchers like Sans Launcher) as the default Home app breaks native **Circle to Search (CtS)** / Google Lens text selection.

When interacting with the system:
- **Stock `com.miui.home`**: Long-pressing the navigation bar or Home button activates the glowing border, freezes the screen, and allows dragging to select/copy text or image OCR via Google Lens.
- **Third-Party Default Launcher**: Long-pressing the Home button either does nothing or long-pressing Recent Apps only pops up the generic Gemini assistant sheet ("Ask about this screen") instead of the frozen-screen Lens OCR selection tool.

---

## Technical Root Cause Analysis: The `isThirdHome` Trap

Inspecting logcat during physical gesture execution reveals Xiaomi's hardcoded restriction:

```bash
adb logcat -d -s CircleToSearchHelper
```

Output from `com.miui.home`:
```text
CircleToSearchHelper: has com.google.android.feature.CONTEXTUAL_SEARCH :true
CircleToSearchHelper: invokeOmni isNotificationExpanded:false,lockScreen:false,ctrlPanelEpd:false,splitMode:false,halfSplitMode:false,isThirdHome:true
```

1. **HyperOS Hardcoded Block (`isThirdHome: true`):**
   Xiaomi does not route the Home button long-press through the standard AOSP Digital Assistant intent. Instead, `MiuiPhoneWindowManager` queries `com.miui.home`. If the current default launcher is third-party, `com.miui.home` detects `isThirdHome: true` and **cancels** the Circle to Search trigger.
2. **Why Recent App Button Opens Gemini Instead of Lens:**
   HyperOS maps `long_press_menu_key=launch_google_search`. Without the private `omni.entry_point` payload, the Google app treats this as a generic assistant invocation and launches Gemini chat rather than the screen OCR overlay.
3. **Why Direct Software Calls Work:**
   The underlying Google App contextual search service (`IVoiceInteractionManagerService`) is **fully functional**. When invoked directly via Binder (bypassing `com.miui.home`), Circle to Search launches flawlessly over whatever screen is active.

---

## How Circle to Search Actually Works Under the Hood

Circle to Search (internally Google's `omnient` / Contextual Search) is **not** an exported Activity with a public Intent. Instead, it relies on Android's `IVoiceInteractionManagerService` via raw IPC:

- **Binder Service**: `voiceinteraction` (`com.android.internal.app.IVoiceInteractionManagerService`)
- **Transaction Code**: `3` (`TRANSACTION_showSessionFromSession`)
- **Key Payload**:
  - `invocation_time_ms`: Current monotonic time via `SystemClock.elapsedRealtime()`.
  - `omni.entry_point`: `1` (Navigation bar long press) or `2` (Home button long press).
  - Flags: `SHOW_WITH_ASSIST (1) | SHOW_WITH_SCREENSHOT (2) | SHOW_SOURCE_ASSIST_GESTURE (4)` = `7`.
  - `attributionTag`: Calling context attribution tag.

---

## Solutions

### Method 1: Direct Integration in Custom Launchers (Kotlin)

If developing a custom launcher, you can directly implement the binder invocation and register as an Assist target:

#### 1. Core Binder Helper (`CircleToSearchHelper.kt`)
```kotlin
package com.sans.launcher

import android.content.Context
import android.os.Bundle
import android.os.IBinder
import android.os.Parcel
import android.os.SystemClock
import android.util.Log

object CircleToSearchHelper {
    private const val TAG = "SansCircleToSearch"
    private const val BINDER_DESCRIPTOR = "com.android.internal.app.IVoiceInteractionManagerService"
    private const val TRANSACTION_SHOW_SESSION_FROM_SESSION = 3
    private const val INVOCATION_TIME_MS_KEY = "invocation_time_ms"
    private const val CS_KEY = "omni.entry_point"
    private const val OMNIENT_ENTRYPOINT_LONG_PRESS_NAV_HANDLE = 1
    private const val FLAGS = 7 // ASSIST | SCREENSHOT | GESTURE

    fun launch(context: Context): Boolean {
        return try {
            val serviceManager = Class.forName("android.os.ServiceManager")
            val getService = serviceManager.getDeclaredMethod("getService", String::class.java)
            val service = getService.invoke(null, "voiceinteraction") as? IBinder ?: return false

            val sessionArgs = Bundle().apply {
                putLong(INVOCATION_TIME_MS_KEY, SystemClock.elapsedRealtime())
                putInt(CS_KEY, OMNIENT_ENTRYPOINT_LONG_PRESS_NAV_HANDLE)
            }

            val data = Parcel.obtain()
            val reply = Parcel.obtain()
            try {
                data.writeInterfaceToken(BINDER_DESCRIPTOR)
                data.writeStrongBinder(null)
                data.writeInt(1)
                sessionArgs.writeToParcel(data, 0)
                data.writeInt(FLAGS)
                data.writeString(context.attributionTag)

                val status = service.transact(TRANSACTION_SHOW_SESSION_FROM_SESSION, data, reply, 0)
                reply.readException()
                val ret = reply.readInt()
                status && ret != 0
            } finally {
                data.recycle()
                reply.recycle()
            }
        } catch (e: Exception) {
            Log.e(TAG, "Failed to invoke Circle to Search", e)
            false
        }
    }
}
```

#### 2. System-Wide Assist Handler (`AssistActivity.kt`)
Catch `android.intent.action.ASSIST` so hardware / nav-bar long presses in any app trigger CtS:
```kotlin
class AssistActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        CircleToSearchHelper.launch(this)
        finish()
    }
}
```

In `AndroidManifest.xml`:
```xml
<activity
    android:name=".AssistActivity"
    android:exported="true"
    android:taskAffinity=""
    android:excludeFromRecents="true"
    android:noHistory="true"
    android:theme="@android:style/Theme.NoDisplay">
    <intent-filter>
        <action android:name="android.intent.action.ASSIST" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</activity>
```

#### 3. Quick Settings Tile (`CircleToSearchTileService.kt`)
Add a pull-down Control Center tile to summon CtS from anywhere:
```kotlin
class CircleToSearchTileService : TileService() {
    override fun onClick() {
        super.onClick()
        CircleToSearchHelper.launch(this)
    }
}
```

#### 4. Setting as Default Assistant via ADB
```bash
adb shell settings put secure assistant <your.package>/.AssistActivity
```
*(Google's background `voice_interaction_service` remains untouched, allowing Google App to supply the Lensient overlay).*

---

### Method 2: Standalone Utility (CTSLauncher by chenxiaolong)

For users using closed-source third-party launchers (Nova, Niagara, etc.):
1. Install [CTSLauncher](https://github.com/chenxiaolong/CTSLauncher) release APK.
2. In **Settings > Apps > Default apps > Digital assistant app**, set **CTSLauncher** as the default assistant.
3. Grant secure settings permission:
   ```bash
   adb shell pm grant com.chiller3.ctslauncher android.permission.WRITE_SECURE_SETTINGS
   ```
4. Long-pressing the Home button or tapping its Quick Settings tile triggers Circle to Search immediately.
