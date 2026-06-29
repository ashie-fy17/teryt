#!/usr/bin/env python3

import subprocess, questionary, shutil, sys

if not shutil.which("yt-dlp"):
    print("Error: 'yt-dlp' is not installed on this system.")
    print("Please install it using your system package manager (e.g., 'sudo pacman -S yt-dlp').")
    sys.exit(1)

def makelist(search_query):
    result = subprocess.run(
        [
            "yt-dlp",
            "--flat-playlist",
            "--extractor-args",
            "youtubetab:approximate_date",
            "--print",
            "%(title)s - %(uploader)s (Uploaded: %(upload_date)s) [%(id)s]",
            f"ytsearch15:{search_query}",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    search_results = result.stdout.splitlines()
    return search_results

search_query = questionary.text("What do you want to watch?").ask()

print("Searching for videos...")

if not search_query:
    print("Error: No search query provided.")
    sys.exit(1)

search_results = makelist(search_query)

if not search_results:
    print("No results found.")
    sys.exit(1)

selected_video = questionary.select(
    "Select a video to watch:",
    choices=search_results,
).ask()

selected_ID = selected_video.split("[")[-1].rstrip("]")

if not questionary.confirm("Have you fully zoomed out your terminal? (required for best quality)").ask():
    sys.exit(1)

subprocess.run(
    f"yt-dlp -S 'res:360,fps:24' -o - '{selected_ID}' | mpv --vo=tct --hwdec=auto --profile=low-latency --framedrop=vo -",
	shell=True
)
