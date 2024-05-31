import tkinter as tk
from tkinter import messagebox
from pytube import YouTube


def download_yt_video():
    url = entry.get()
    yt = YouTube(url)

    try:
        yt.check_availability()
        streams = yt.streams
        # get a 720p video
        video = streams.filter(res="720p").first()

        print(f"Downloading {video.title}")
        video.download()
        print("Download complete!")
        messagebox.showinfo("Success", "Download completed successfully!")
    except Exception as e:
        print(e)
        messagebox.showerror("Error", str(e))


def run_script():
    download_yt_video()


root = tk.Tk()
root.title("YouTube Downloader")

label = tk.Label(root, text="Enter YouTube URL:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Download", command=run_script)
button.pack()

root.mainloop()
