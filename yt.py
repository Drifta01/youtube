import os
from tkinter import messagebox
from pytube import YouTube


def download_yt_video(url, res):
    yt = YouTube(url)

    try:
        yt.check_availability()
        streams = yt.streams
        print(streams)
        video = streams.filter(res=res).first()

        print(f"Downloading {video.title}")
        downloads_folder = os.path.expanduser("~/Downloads")
        video.download(output_path=downloads_folder, skip_existing=True)

        print("Download complete!")
        messagebox.showinfo("Success", "Download completed successfully!")

    except Exception as e:
        print(e)
        messagebox.showerror("Error", str(e))
