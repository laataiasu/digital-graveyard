---
title: "Fixing Suspend Freeze on HP 15-ef2xxx With RTL8821CE on Linux"
date: 2026-08-24
tags: [guide]
publish_external: true
---

For over a year, every Linux distro I tried on my [[HP]] 15-ef2xxx laptop had the same fatal flaw: the moment the machine went to suspend, it never came back. Closing the lid or pressing the power button meant a black screen I could never log in out of — eventually a hard reset, and sometimes a drained battery. Windows on the same hardware suspends flawlessly. Every forum thread ended in "disable suspend" as the fix, which always felt like surrender.

Today I finally root-caused it. The culprit was never the distro, nor the kernel's ACPI handling — it was the Wi-Fi chip: a **Realtek RTL8821CE** PCIe adapter (`10ec:c821`) driven by the `rtw88` driver.

## Root cause

The RTL8821CE firmware supports a Deep Power Save mode (`LPS_DEEP_MODE_LCLK`). When that mode is active *concurrently* with PCIe ASPM L1 power saving, the chip fails to handle wake signaling. On this HP firmware the failure is total: the platform wedges mid-suspend.

The kernel log told the whole story once I knew where to look:

```
PM: suspend entry (s2idle)
← nothing. Ever.
```

A healthy s2idle cycle ends with `PM: suspend exit`. Mine never did — across months of boots, every single suspend died at entry. Hours before one of these events, the driver had also thrown its confession:

```
rtw88_8821ce: firmware failed to ack driver for leaving Deep Power mode
WARNING: ... rtw_power_mode_change+0xda/0x120 [rtw88_core]
Call Trace: rtw_pci_tx_kick_off_queue ...
```

## The fix

Tell the driver to never use deep LPS and to keep the PCIe link awake:

```bash
# /etc/modprobe.d/rtw88-suspend-fix.conf
options rtw88_core disable_lps_deep=Y
options rtw88_pci disable_aspm=Y
```

Then reload (or reboot):

```bash
sudo modprobe -r rtw88_8821ce && sudo modprobe rtw88_8821ce
```

First controlled test with `rtcwake -m mem -s 90`:

```
PM: suspend devices took 0.163 seconds
PM: resume devices  took 0.441 seconds
PM: suspend exit    ← first clean cycle ever on this machine
```

Wi-Fi reconnected instantly after resume. The cost is a few percent of battery idle drain — a trivial price.

## Why Windows works but Linux doesn't

Windows uses HP/Realtek's proprietary driver stack, which manages the S0ix handshake correctly. Linux relies on generic ACPI plus `amd_pmc`, so a sloppy firmware + an aggressive Wi-Fi power-save feature becomes fatal. This also explains why *every distro* failed identically — the bug follows the hardware, not the OS install.

## Contributing back

It turns out this is a known upstream issue in the [[Linux]] kernel Bugzilla (bugs 215131, 219830 and 218697 — all symptoms of the same ASPM/LPS race). A DMI quirk already landed for one HP SKU (`P3S95EA#ACB`) that auto-applies exactly these two workarounds. The quirk table just doesn't know my laptop exists yet.

The contribution path:

1. Add a tested data point to an existing Bugzilla report (hardware, BIOS version F.35, kernel, the warning trace, and "confirmed fixed by both module options").
2. Longer term, extend the DMI quirk table in `drivers/net/wireless/realtek/rtw88/pci.c` with the HP 15-ef2xxx DMI strings so future users get the fix automatically — ~36 lines of code, zero risk to other systems.

The lesson generalizes: when *every* distro breaks the same way, stop reinstalling and start reading logs. The answer was sitting in `journalctl -b -1 -k` all along.
