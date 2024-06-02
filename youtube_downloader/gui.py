import tkinter as tk
from tkinter import messagebox
from .yt import YouTubeDownloader


class YouTubeDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")

        self.create_widgets()

    def create_widgets(self):
        # Create URL label and entry
        url_label = tk.Label(self.root, text="Enter YouTube URL:")
        url_label.grid(row=0, column=0, padx=10, pady=10)

        self.url_entry = tk.Entry(self.root)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create Paste URL button
        paste_button = tk.Button(
            self.root, text="Paste URL", command=self.paste_from_clipboard
        )
        paste_button.grid(row=0, column=2, padx=10, pady=10)

        # Create resolution label and radio buttons
        resolution_label = tk.Label(self.root, text="Choose resolution:")
        resolution_label.grid(row=1, column=0, padx=10, pady=10)

        self.resolution_var = tk.StringVar()
        self.resolution_var.set("720p")  # default value

        resolution_480p = tk.Radiobutton(
            self.root, text="480p", variable=self.resolution_var, value="480p"
        )
        resolution_480p.grid(row=1, column=1, padx=10, pady=0)

        resolution_720p = tk.Radiobutton(
            self.root, text="720p", variable=self.resolution_var, value="720p"
        )
        resolution_720p.grid(row=2, column=1, padx=10, pady=0)

        resolution_1080p = tk.Radiobutton(
            self.root, text="1080p", variable=self.resolution_var, value="1080p"
        )
        resolution_1080p.grid(row=3, column=1, padx=10, pady=10)

        # Create Download button
        download_button = tk.Button(
            self.root, text="Download", command=self.download_video
        )
        download_button.grid(row=1, column=2, columnspan=3, padx=10, pady=10)

    def paste_from_clipboard(self):
        self.url_entry.delete(0, tk.END)
        try:
            self.url_entry.insert(0, self.root.clipboard_get())
        except tk.TclError:
            print("Failed to paste from clipboard.")

    def download_video(self):
        url = self.url_entry.get()
        res = self.resolution_var.get()

        downloader = YouTubeDownloader(url, res)
        if downloader.run():
            messagebox.showinfo("Download", "Video downloaded successfully.")
        else:
            messagebox.showerror("Error", "Failed to download the video.")


def create_gui():
    root = tk.Tk()

    window_height = 180
    window_width = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    YouTubeDownloaderGUI(root)
    root.mainloop()

    return root
