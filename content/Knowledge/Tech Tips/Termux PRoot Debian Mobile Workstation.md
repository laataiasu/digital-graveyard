---
title: "Termux & PRoot Debian Mobile Workstation Guide"
date: 2026-09-20
tags: [guide]
publish_external: true
updated: 2026-09-20
---

Panduan arsitektur dan setup lengkap untuk menjadikan smartphone Android (khususnya flagship modern seperti Xiaomi 14T Pro / Dimensity 9300+) sebagai mobile workstation mandiri untuk coding berbasis AI agent.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 1: ANDROID HOST & TERMUX (Bionic libc)                                    │
│  • Touchscreen UX: Extra keys bar (`~/.termux/termux.properties`)              │
│  • Glyph rendering: JetBrainsMono Nerd Font (`~/.termux/font.ttf`)              │
│  • Android Bridges: Storage access, Termux:API clipboard, wake-lock             │
│  • Engine: `proot-distro` (isolasi userland tanpa root)                         │
└──────────────────────────────────────┬──────────────────────────────────────────┘
                                       │ `proot-distro login debian --shared-tmp`
┌──────────────────────────────────────▼──────────────────────────────────────────┐
│ LAYER 2: PROOT DEBIAN CONTAINER (glibc standard)                                │
│  • Dotfiles: `dotfiles-public` (`--profile mobile` / headless)                 │
│  • Shell: Zsh + Starship prompt + zsh-autosuggestions + syntax-highlighting     │
│  • AI Toolchain: Antigravity CLI (`agy`), Astral Python (`uv`), Runtime (`bun`) │
│  • Memory Guard: Capped V8 heap (`--max-old-space-size=512`)                   │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## PART 1: Konfigurasi di Luar (Termux Host Layer)

Layer Termux bertindak sebagai antarmuka terminal, jembatan hardware Android, dan pengelola session.

### 1. Update Paket & Install PRoot
Buka aplikasi Termux, jalankan:
```bash
pkg update -y
pkg install -y proot-distro termux-api openssh tar
proot-distro install debian
```

### 2. Jinakkan Android OS & HyperOS (Biar Gak Dibunuh)
Android dan HyperOS sangat agresif mematikan proses background:
1. **Bypass Phantom Process Killer (via ADB laptop sekali saja)**:
   ```bash
   adb shell "/system/bin/device_config put activity_manager max_phantom_processes 2147483647"
   ```
2. **App Info Termux**:
   - Buka Settings HP ➡️ Apps ➡️ Manage Apps ➡️ Termux.
   - Set **Battery saver** ke **No restrictions**.
   - Aktifkan **Autostart** dan kunci (lock) Termux di Recents screen.

### 3. Setup Extra Keys Bar (Ergonomi Layar Sentuh)
Tambahkan baris tombol shortcut di atas virtual keyboard untuk mempermudah navigasi, tab completion, dan simbol:

```bash
mkdir -p ~/.termux
cat <<'EOF' > ~/.termux/termux.properties
extra-keys = [ \
  ['ESC', 'TAB', 'CTRL', 'ALT', {key: '-', popup: '_'}, {key: '/', popup: '\\'}, 'UP'], \
  [{key: 'QUOTE', popup: '\"'}, {key: 'APOSTROPHE', popup: '`'}, {key: '(', popup: ')'}, {key: '[', popup: ']'}, 'LEFT', 'DOWN', 'RIGHT'] \
]
EOF
termux-reload-settings
```

### 4. Pasang JetBrainsMono Nerd Font
Agar icon cabang Git dan status di Starship prompt tidak pecah menjadi kotak tanda tanya:

```bash
mkdir -p ~/.termux
curl -fsSL "https://github.com/ryanoasis/nerd-fonts/releases/latest/download/JetBrainsMono.tar.xz" | tar -xJf - -O JetBrainsMonoNerdFont-Regular.ttf > ~/.termux/font.ttf
termux-reload-settings
```

### 5. Akses Storage HP
Izinkan Termux membaca dan menulis ke folder penyimpanan Android (Downloads, Documents):
```bash
termux-setup-storage
```

### 6. Auto-Login ke Debian Tanpa Menutup Termux saat Exit
Agar saat membuka aplikasi Termux otomatis masuk ke PRoot Debian, tetapi **saat exit dari Debian tetap kembali ke shell Termux default** (bukan menutup aplikasi):

Tambahkan baris ini ke `~/.bashrc` di Termux luar:
```bash
cat <<'EOF' >> ~/.bashrc
# Cegah CPU tidur saat proses background berjalan
termux-wake-lock 2>/dev/null || true

# Alias manual buat masuk lagi kapan saja
alias debian="proot-distro login debian --shared-tmp -- /bin/zsh"

# Auto-enter PRoot Debian hanya saat sesi awal dibuka (tanpa exec)
if [ -z "$PROOT_DISTRO" ] && [ -z "$TERMUX_DROPPED" ]; then
  export TERMUX_DROPPED=1
  proot-distro login debian --shared-tmp -- /bin/zsh
fi
EOF
```
> **Cara kerjanya**:
> - Jangan gunakan `exec`! `exec` me-replace PID shell utama, sehingga exit dari Debian langsung membunuh sesi Termux.
> - Dengan `TERMUX_DROPPED=1`, begitu lo ketik `exit` di Debian, lo akan jatuh kembali ke prompt Termux native (`~ $`).
> - Kalau mau masuk lagi ke Debian, cukup ketik `debian`.
> - Kalau mau beneran nutup Termux, ketik `exit` sekali lagi di Termux native.

---

## PART 2: Konfigurasi di Dalam (PRoot Debian Container)

Layer Debian menyediakan standard **glibc** penuh sehingga binary Linux seperti `agy`, `bun`, dan `uv` berjalan 100% native tanpa error missing linker atau Bionic libc limitation.

### 1. Masuk ke PRoot Debian Pertama Kali
```bash
proot-distro login debian --shared-tmp
```

### 2. Siapkan Dependensi Awal & Bootstrap Dotfiles
Di dalam prompt root Debian:
```bash
# Install paket minimal untuk bootstrapping
apt-get update && apt-get install -y git curl sudo

# Clone repository dotfiles
mkdir -p ~/Projects
git clone https://github.com/nichsedge/dotfiles-public.git ~/Projects/dotfiles-public
cd ~/Projects/dotfiles-public

# Eksekusi mobile profile
./bootstrap.sh --profile mobile
```

### 3. Apa yang Dilakukan oleh `--profile mobile`?
1. **Minimal Packages**: Hanya menginstal `git`, `curl`, `zsh`, `ripgrep`, `fzf`, `unzip`, `ca-certificates`. Melewati compiler berat (`rustup`, `build-essential`) dan desktop bloatware.
2. **AI Toolchain**: Menginstal resmi binary flat ARM64:
   - **`uv`**: Astral Python package manager.
   - **`bun`**: JavaScript/TypeScript runtime ultra-cepat.
   - **`agy`**: Google Antigravity CLI / AI Agent toolkit.
3. **Headless Symlinking**: Hanya menyinkronkan config portable (`.zshrc`, `.gitconfig`, `.profile`, `.config/starship.toml`) dan mengabaikan config GUI desktop (Hyprland, Waybar, Ghostty).
4. **Auto-Switch Zsh di PRoot**: Menyisipkan script deteksi di `/root/.bashrc` agar mengatasi bug PRoot yang selalu memanggil bash secara default.

### 4. Verifikasi Instalasi
Reload shell Zsh:
```bash
exec zsh
```
Pastikan seluruh toolchain aktif:
```bash
uv --version
bun --version
agy --version
```

### 5. Memory & Session Guardrails

1. **Batasan Memory Node.js / V8**:
   Di `.zshrc` bawaan dotfiles, memori heap Node.js sudah dibatasi otomatis jika mendeteksi environment mobile/proot:
   ```zsh
   export NODE_OPTIONS="--max-old-space-size=512"
   ```
2. **Keyboard Ergonomics untuk Autosuggestions**:
   Di virtual keyboard, tekan `Ctrl + Space` atau `Ctrl + F` untuk langsung menerima rekomendasi *zsh-autosuggestions*.
3. **Gunakan Multiplexer (`tmux` / `zellij`)**:
   Saat menjalankan tugas AI panjang lewat `agy`, selalu jalankan di dalam session `tmux` agar proses tidak terhenti jika Termux dialihkan ke background oleh sistem operasi:
   ```bash
   tmux new -s ai
   agy
   ```

---

## PART 3: Multi-Device Data Sync (Cloudflare R2 SSOT)

Untuk sinkronisasi database lokal (`events.db` di `ierp`) antara laptop dan HP tanpa membuat database silo, digunakan **Cloudflare R2** (`ichsanul-dev`) sebagai Single Source of Truth (SSOT).

### Perintah Cepat di Zsh (Laptop & HP):
- **`event sync`**: Auto-sync cerdas. Membandingkan hash MD5/ETag SQLite lokal dengan remote R2. Otomatis `pull` jika remote lebih baru, atau `push` jika lokal punya update baru.
- **`event push`**: Paksa upload snapshot SQLite lokal ke R2 (`db/ierp_latest.sqlite`).
- **`event pull`**: Paksa download snapshot terbaru dari R2 ke SQLite lokal (lengkap dengan backup snapshot otomatis sebelum overwrite).
- **`event r2 status`**: Lihat perbandingan ukuran, timestamp, MD5, dan status sync.

Format command native:
```bash
uv --directory ~/Projects/ierp run ierp r2 [status|push|pull|auto]
```

---

## PART 4: Migrasi Cron Hermes Workstation ke HP (Zero Battery Waste)

Untuk menghemat listrik dan membebaskan laptop agar tidak harus menyala 24/7, beberapa scheduled jobs Hermes di laptop bisa dipindahkan ke Termux PRoot menggunakan arsitektur **Wake-Lock Sandwich**:

### Pola Wake-Lock Sandwich (Zero Battery Drain saat Idle)
Jangan jalankan daemon cron terus-menerus di dalam PRoot. Jalankan `crond` di **Termux host (luar)** dengan format:
```cron
<minute> <hour> <day> <month> <dow> termux-wake-lock && proot-distro login debian --shared-tmp -- /bin/bash <script_runner> && termux-wake-unlock
```
- **Saat idle**: HP tetap masuk ke status *Deep Sleep* (Doze mode), konsumsi baterai 0%.
- **Saat jam eksekusi**: Termux mengambil `wake-lock` ➡️ eksekusi script di PRoot Debian ➡️ lepaskan `wake-lock` ➡️ HP kembali tidur lelap.

### Setup Cron di Termux Luar
1. Install `cronie` di Termux luar:
   ```bash
   pkg install -y cronie
   crond
   ```
2. Pasang crontab:
   ```bash
   crontab ~/Projects/_scheduled_jobs/mobile_runners/termux_crontab.txt
   ```
3. Agar `crond` otomatis aktif saat HP dinyalakan, install app **Termux:Boot** dari F-Droid dan buat file:
   ```bash
   mkdir -p ~/.termux/boot
   echo "crond" > ~/.termux/boot/start-cron.sh
   chmod +x ~/.termux/boot/start-cron.sh
   ```

---

## Troubleshooting & Tips

- **Clipboard Share**: Pipe output terminal langsung ke clipboard Android lewat `cat output.txt | termux-clipboard-set` (membutuhkan `termux-api`).
- **Font Rusak / Kotak-kotak**: Pastikan step 4 di Part 1 sudah dieksekusi di Termux host luar dan jalankan `termux-reload-settings`.
- **Zsh Tidak Otomatis Muncul**: Pastikan flag login menggunakan `-- /bin/zsh` atau periksa apakah block auto-switch sudah ada di `~/.bashrc` Debian.
- **Baterai Cepat Habis**: Pastikan tidak ada `termux-wake-lock` yang berjalan permanen di `~/.bashrc`. Gunakan wake-lock hanya saat script berjalan.
