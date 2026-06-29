# >_teryt

teryt (pronounced "ter-it") is a minimalist, distraction-free terminal YouTube client built specifically for advanced Linux terminal setups. It allows you to search for videos and stream them directly inside your text console grid using True Color Text (TCT) matrix rendering.

## 📋 Prerequisites

Before running teryt, ensure your system has the following system dependencies installed:

- **Python 3**
- **yt-dlp**
- **mpv** (compiled with terminal graphics support)
- A terminal emulator that supports 24-bit True Color (Recommended: **Kitty** or **Alacritty**)

On Arch Linux / EndeavourOS, install them via pacman:
\`\`\`bash
sudo pacman -S python yt-dlp mpv kitty
\`\`\`

## ⚙️ Installation & Setup

1. Clone or download this repository.
2. Install the required Python libraries:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`
3. Make the script executable:
   \`\`\`bash
   chmod +x teryt.py
   \`\`\`

## 🎮 Usage

Launch the client from your terminal:
\`\`\`bash
./teryt.py
\`\`\`
*Note: For the best visual experience, fully zoom out your terminal window before playback to maximize the text grid density!*

## 💡 The Idea Behind This Project

As a Linux user, I practically live in the terminal. My entire workflow depends on it. As I was looking through all the current YouTube clients for the terminal, I realized something. All of them spawned a separate window. I started wondering, "What if I could render a video directly *inside* the terminal?" And that was the birth of this quirky, fun project that I've named teryt.
