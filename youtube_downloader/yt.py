import threading
import os
from pytube import YouTube


class YouTubeDownloader:
    def __init__(self, url, res, output_path=None):
        self.url = url
        self.res = res
        self.output_path = output_path
        self.yt = YouTube(self.url, on_progress_callback=self.on_progress)

    def check_availability(self):
        self.yt.check_availability()

    def get_output_path(self):
        if not self.output_path:
            self.output_path = os.path.expanduser("~/Downloads")
        return self.output_path

    def filter_stream(self):
        print(self.yt.streams)
        stream = self.yt.streams.filter(res=self.res).first()
        print(stream)
        return stream

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        self.progress_bar["value"] = percentage_of_completion

        print(
            "█" * int(percentage_of_completion / 2)
            + " " * (50 - int(percentage_of_completion / 2)),
            f"{int(percentage_of_completion)}%",
            end="\r",
        )

    def download_video(self):
        video = self.filter_stream()

        print(f"Downloading... {video.title}")
        video.download(output_path=self.get_output_path(), skip_existing=True)
        print("Download completed!")

    def run(self):
        if not self.url:
            print("no url")
            return False
        try:
            self.check_availability()
            thread = threading.Thread(target=self.download_video)
            thread.start()
            return True
        except Exception as e:
            print(e)
            return False
