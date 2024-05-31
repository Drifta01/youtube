from .gui import create_gui
from .yt import download_yt_video


def main():
    root = create_gui()
    entry = root.children["entry"]
    button = root.children["button"]
    button.config(command=lambda: download_yt_video(entry.get()))
    root.mainloop()


if __name__ == "__main__":
    main()
