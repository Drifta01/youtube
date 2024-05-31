import tkinter as tk


def create_gui():
    root = tk.Tk()
    root.title("YouTube Downloader")

    label = tk.Label(root, text="Enter YouTube URL:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Download")
    button.pack()

    root.children = {"entry": entry, "button": button}

    return root
