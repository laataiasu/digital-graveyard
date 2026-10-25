---
title: "Dota 2 Pro Keybinds and Laptop Fn Bypass"
date: 2026-10-25
tags: [gaming, dota2, linux, hardware]
publish_external: false
---

# Dota 2 Pro Keybinds & Laptop Fn Bypass

Dokumentasi konfigurasi hotkey Dota 2 ala Pro Player (Miracle- / Topson 100% Keyboard Style) untuk mengatasi masalah BIOS reset pada laptop tanpa baterai CMOS.

---

## 🛑 Akar Masalah: Kenapa F1–F12 Bermasalah?

1. **HP Laptop 15-ef2xxx Tidak Punya Baterai CMOS Terpisah**:
   - Motherboard HP seri 15-ef / 15s tidak memiliki slot baterai kancing CR2032.
   - Sirkuit RTC dan NVRAM BIOS disuplai oleh daya *trickle* dari baterai laptop utama (**HT03XL**).
   - Ketika baterai utama dilepas, setiap kali restart atau daya drop, CMOS mengalami *checksum error* (**Error 502**) dan BIOS otomatis kembali ke **Factory Default** (*Action Keys Mode = Enabled*).
2. **Kenapa `keyd` & `hwdb` Gagal di Linux?**:
   - Saat *Action Keys Mode* aktif di BIOS, chip *Embedded Controller* (EC) di motherboard HP **mencegat tombol fisik F2 (Brightness Down) & F3 (Brightness Up) di level hardware**.
   - Sinyal tidak pernah dikirim sebagai tombol keyboard biasa ke kernel; chipset langsung mengalihkannya ke sirkuit ACPI display, dan hanya melempar sinyal dummy `0xab` yang sama persis untuk F2 dan F3.
   - Karena kedua tombol menghasilkan scancode kembar di hardware, remapping software apa pun di OS tidak bisa memisahkan F2 dan F3.
3. **Solusi Terbaik**:
   - **Hardware Fix**: Pasang kembali baterai internal (tipe **HT03XL** / part *L11119-855*).
   - **Software / Gaming Fix**: Evakuasi seluruh kontrol in-game Dota 2 keluar dari baris tombol `F1`–`F12` ke tombol keyboard utama (Zero F-Keys Layout).

---

## 🗺️ Cheatsheet Layout Dota 2 Pro Player (100% Keyboard)

```text
┌─────────────────────────────────────────────────────────────────┐
│  [1] [2] [3] [4]        [5]              [6]                    │
│   Item 1, 2, 3, 4    Antar Kurir    Pilih Kurir                 │
│                                                                 │
│  [Q] [W] [E] [R] [D] [F]                                        │
│   Skills & Ultimate                                             │
│                                                                 │
│  [A] Serang      [S] Stop / Cancel                              │
│                                                                 │
│  [Z] Item 5      [X] Item 6                                     │
│  [C] Semua Unit  [V] Unit Lain (Ilusi)                          │
│                                                                 │
│  [ B ] Buka Shop (Buy)          [ ALT + B ] Beli TP (Sticky)    │
│  [SPACE] Pilih Hero             [ ALT + SPACE ] Quick Buy       │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚡ Detail Key Mapping

| Fungsi | Tombol | Modifier / QuickCast | Keterangan |
| :--- | :--- | :--- | :--- |
| **Pilih Hero / Snap Kamera** | `SPACE` | None | **Double-tap Space**: Kamera langsung mengunci ke hero (standar RTS & Miracle-/Topson). |
| **Antar Kurir** | `5` | None | Tepat di samping Item 4. Satu kali pencet langsung ambil barang dan antar ke hero. |
| **Pilih Kurir** | `6` | None | Kontrol kurir manual. |
| **Item Slot 1–4** | `1`, `2`, `3`, `4` | `ALT + [1-4]` | Baris angka atas untuk item aktif krusial (Blink, BKB, Hex). |
| **Item Slot 5–6** | `Z`, `X` | `ALT + [Z, X]` | Baris bawah untuk item pasif / sekunder. |
| **Neutral Item** | `T` | `ALT + T` | Slot item neutral. |
| **Town Portal (TP)** | `ALT + T` | None | Slot TP scroll. |
| **Buka / Tutup Toko** | `B` | None | Tombol universal RTS (*B = Buy*). |
| **Quick Buy** | `SPACE` | `ALT + SPACE` | Beli item darurat saat sekarat tanpa melepaskan jari dari tombol skill. |
| **Beli TP (Sticky)** | `B` | `ALT + B` | Beli TP cadangan instan dari toko. |
| **Semua Unit** | `C` | None | Kontrol hero + ilusi + summon sekaligus. |
| **Unit Lain (Ilusi)** | `V` | None | Kontrol ilusi / summon tanpa menggerakkan hero utama. |
| **Ganti Unit** | `TAB` | None | Siklus antar unit summon / clone. |

---

## 📁 Lokasi File Konfigurasi

- **Live Steam Config**:
  ```text
  ~/.local/share/Steam/userdata/1261781240/570/remote/cfg/dotakeys_personal.lst
  ```
- **Dotfiles Backup & Versioning**:
  ```text
  ~/Projects/dotfiles-private/personal/dota2/dotakeys_personal.lst
  ```

### Cara Restore jika Ter-reset Steam Cloud:
```bash
cp ~/Projects/dotfiles-private/personal/dota2/dotakeys_personal.lst \
   ~/.local/share/Steam/userdata/1261781240/570/remote/cfg/dotakeys_personal.lst
```

---

## 🔗 Related Notes
- [[HP Laptop 15-ef2xxx Hardware Upgrade Guide]]
- [[Linux Tips]]
