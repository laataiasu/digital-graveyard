---
title: "Termux & PRoot Debian Mobile Workstation Guide"
date: 2026-09-20
tags: [guide, linux, termux, debian, mobile, android]
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

### 6. Auto-Login ke Debian & Persistent Wakelock
Biar setiap kali membuka aplikasi Termux langsung masuk ke PRoot Debian tanpa ngetik manual:

Tambahkan baris ini ke `~/.bashrc` di Termux luar:
```bash
cat <<'EOF' >> ~/.bashrc
# Cegah CPU tidur saat proses background berjalan
termux-wake-lock 2>/dev/null || true

# Auto-enter PRoot Debian langsung ke Zsh
if [ -z "$PROOT_DISTRO" ]; then
  exec proot-distro login debian --shared-tmp -- /bin/zsh
fi
EOF
```

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

## Troubleshooting & Tips

- **Clipboard Share**: Pipe output terminal langsung ke clipboard Android lewat `cat output.txt | termux-clipboard-set` (membutuhkan `termux-api`).
- **Font Rusak / Kotak-kotak**: Pastikan step 4 di Part 1 sudah dieksekusi di Termux host luar dan jalankan `termux-reload-settings`.
- **Zsh Tidak Otomatis Muncul**: Pastikan flag login menggunakan `-- /bin/zsh` atau periksa apakah block auto-switch sudah ada di `~/.bashrc` Debian.
