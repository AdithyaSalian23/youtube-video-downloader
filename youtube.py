import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',  
        'format': 'best',  
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("✅ Video downloaded successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")

def open_file_dialog():
    folder = filedialog.askdirectory(title="Select Download Folder")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  

    video_url = input("Please enter a YouTube URL: ").strip()
    save_dir = open_file_dialog()

    if save_dir:
        print("⬇️  Downloading video...")
        download_video(video_url, save_dir)
    else:
        print("❌ Invalid save location.")
