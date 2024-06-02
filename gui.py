import tkinter as tk

from yt import download_yt_video


def create_gui():
    root = tk.Tk()
    root.title("YouTube Downloader")

    label = tk.Label(root, text="Enter YouTube URL:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    def paste_from_clipboard():
        entry.insert(tk.END, root.clipboard_get())

    entry.bind("<Control-v>", lambda event: paste_from_clipboard())

    button_paste = tk.Button(root, text="Paste URL", command=paste_from_clipboard)
    button_paste.pack()

    button_dl = tk.Button(
        root, text="Download", command=lambda: download_yt_video(entry.get())
    )
    button_dl.pack()

    return root
