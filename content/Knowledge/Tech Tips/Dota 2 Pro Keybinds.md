---
title: "Dota 2 Keybinds and Laptop Fn Hardware Quirk"
date: 2026-10-25
tags: [gaming, dota2, linux, hardware]
publish_external: false
---

# Dota 2 Keybinds & Laptop Fn Hardware Quirk

Dokumentasi konfigurasi hotkey Dota 2 personal (`al@fedora`), catatan troubleshooting CMOS error pada laptop HP tanpa baterai, serta backup konfigurasi.

---

## 🛑 Akar Masalah: Kenapa F1–F12 Bermasalah saat Baterai Dicopot?

1. **HP Laptop 15-ef2xxx Tidak Punya Baterai CMOS Terpisah**:
   - Motherboard HP seri 15-ef / 15s tidak memiliki slot baterai kancing CR2032 terpisah.
   - Sirkuit RTC dan NVRAM BIOS disuplai langsung oleh daya *trickle* dari baterai laptop utama (**HT03XL**).
   - Ketika baterai utama dilepas, setiap kali restart atau daya terputus, CMOS mengalami *checksum error* (**HP CMOS Reset 502**) dan BIOS otomatis kembali ke **Factory Default** (*Action Keys Mode = Enabled*).
2. **Kenapa `keyd` & `hwdb` Gagal di Linux?**:
   - Saat *Action Keys Mode* aktif di BIOS, chip *Embedded Controller* (EC) di motherboard HP **mencegat tombol fisik F2 (Brightness Down) & F3 (Brightness Up) di level hardware**.
   - Sinyal tidak pernah dikirim sebagai tombol keyboard biasa ke kernel; chipset langsung mengalihkannya ke sirkuit ACPI display, dan hanya melempar sinyal dummy `0xab` yang sama persis untuk F2 dan F3.
   - Karena kedua tombol menghasilkan scancode kembar di hardware, remapping software apa pun di OS tidak bisa memisahkan F2 dan F3.
3. **Solusi Definitif**:
   - **Hardware Fix**: Pasang kembali baterai internal (tipe **HT03XL** / part *L11119-855*), sehingga settingan BIOS tersimpan permanen dan CMOS error hilang.
   - **External Keyboard**: Menggunakan keyboard eksternal USB / wireless (tidak terpengaruh oleh BIOS laptop).

---

## 🗺️ Active Layout (Personal Default)

Layout default yang aktif dan sudah terbiasa dengan muscle memory:

```text
┌─────────────────────────────────────────────────────────────────┐
│  [F1] Pilih Hero     [F2] Pilih Kurir     [F3] Antar Kurir      │
│  [F4] Buka Shop      [F5] Quick Buy       [F8] Sticky (Beli TP) │
│                                                                 │
│  [1] [2] [3]         [Z] [SPACE] [X]                            │
│   Item 1, 2, 3        Item 4, 5, 6                              │
│                                                                 │
│  [Q] [W] [E] [R] [D] [F]                                        │
│   Skills & Ultimate                                             │
│                                                                 │
│  [A] Serang          [S] Stop / Cancel                          │
│  [C] Semua Unit      [V] Unit Lain (Ilusi)                      │
│                                                                 │
│  [T] Neutral Item    [ ALT + T ] Town Portal (TP)               │
└─────────────────────────────────────────────────────────────────┘
```

| Fungsi | Tombol | Modifier / QuickCast |
| :--- | :--- | :--- |
| **Hero Select** | `F1` | None |
| **Courier Select** | `F2` | None |
| **Courier Deliver** | `F3` | None |
| **Shop Toggle** | `F4` | None |
| **Quick Buy** | `F5` | None |
| **Sticky Buy (TP)** | `F8` | None |
| **Inventory 1–3** | `1`, `2`, `3` | `ALT + [1-3]` |
| **Inventory 4** | `Z` | `ALT + Z` |
| **Inventory 5** | `SPACE` | `ALT + SPACE` |
| **Inventory 6** | `X` | `ALT + C` |
| **Neutral Item** | `T` | `ALT + T` |
| **Town Portal (TP)** | `ALT + T` | None |
| **Select All Units** | `C` | None |
| **Select Other Units** | `V` | None |
| **Cycle Units** | `TAB` | None |

---

## 📁 Lokasi File Konfigurasi & Backup

- **Live Steam Config**:
  ```text
  ~/.local/share/Steam/userdata/1261781240/570/remote/cfg/dotakeys_personal.lst
  ```
- **Dotfiles Backup**:
  ```text
  ~/Projects/dotfiles-private/personal/dota2/dotakeys_personal.lst
  ```

### Restore Command:
```bash
cp ~/Projects/dotfiles-private/personal/dota2/dotakeys_personal.lst \
   ~/.local/share/Steam/userdata/1261781240/570/remote/cfg/dotakeys_personal.lst
```

---

## 🔗 Related Notes
- [[HP Laptop 15-ef2xxx Hardware Upgrade Guide]]
- [[Linux Tips]]
