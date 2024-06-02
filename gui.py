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

    resolution_label = tk.Label(root, text="Choose resolution:")
    resolution_label.pack()

    resolution_var = tk.StringVar()
    resolution_var.set("480p")  # default value

    resolution_480p = tk.Radiobutton(
        root, text="480p", variable=resolution_var, value="480p"
    )
    resolution_480p.pack()

    resolution_720p = tk.Radiobutton(
        root, text="720p", variable=resolution_var, value="720p"
    )
    resolution_720p.pack()

    resolution_1080p = tk.Radiobutton(
        root, text="1080p", variable=resolution_var, value="1080p"
    )
    resolution_1080p.pack()

    button_dl = tk.Button(
        root,
        text="Download",
        command=lambda: download_yt_video(entry.get(), resolution_var.get()),
    )
    button_dl.pack()

    return root
