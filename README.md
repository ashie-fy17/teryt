https://github.com/user-attachments/assets/f76be457-b991-4b0d-bfc7-ea017282e775


# >_ teryt

teryt (pronounced "ter-it") is a minimalist, distraction-free terminal YouTube client built specifically for advanced Linux terminal setups. it allows you to search for videos and stream them directly inside your text console grid using True Color Text (TCT) matrix rendering.

## 💡 the idea behind this project

as a Linux user, i practically live in the terminal. my entire workflow depends on it. as i was looking through all the current YouTube clients for the terminal, i realized something. all of them spawned a separate window. i started wondering, "what if I could render a video directly *inside* the terminal?" and that was the birth of this quirky, fun project that I've named teryt.

# demo :3
https://github.com/user-attachments/assets/f76be457-b991-4b0d-bfc7-ea017282e775

## 📋 prerequisites

before running teryt, ensure your system has the following system dependencies installed:

- **Python 3**
- **yt-dlp**
- **mpv** (compiled with terminal graphics support)
- a terminal emulator that supports 24-bit True Color (Recommended: **Kitty** or **Alacritty**)

on Arch Linux / EndeavourOS, install them via pacman:

```bash
sudo pacman -S python yt-dlp mpv kitty
```

on Ubuntu / Debian / Linux Mint, install them via apt:

```bash
sudo apt update && sudo apt install python3 python3-pip yt-dlp mpv kitty
```

on Fedora, install them via dnf:

```bash
sudo dnf install python3 yt-dlp mpv kitty
```

on OpenSUSE, install them via zypper:

```bash
sudo zypper install python3 yt-dlp mpv kitty
```

## ⚙️ installation & setup

1. clone or download this repository.
2. install the required Python libraries:

```bash
pip install -r requirements.txt
```

3. make the script executable:

```bash
chmod +x teryt.py
```

## 🎮 usage

Launch the client from your terminal:

```bash
./teryt.py
```

*note: for the best visual experience, fully zoom out your terminal window before playback to maximize the text grid density!*
