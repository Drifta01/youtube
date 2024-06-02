import os
from pytube import YouTube


class YouTubeDownloader:
    def __init__(self, url, res, output_path=None):
        self.url = url
        self.res = res
        self.output_path = output_path

    def check_availability(self):
        yt = YouTube(self.url)
        yt.check_availability()

    def get_streams(self):
        yt = YouTube(self.url)
        return yt.streams

    def filter_stream(self):
        streams = self.get_streams()
        return streams.filter(res=self.res).first()

    def get_output_path(self):
        if not self.output_path:
            self.output_path = os.path.expanduser("~/Downloads")
        return self.output_path

    def download_video(self):
        def on_progress(stream, chunk, bytes_remaining):
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage_of_completion = bytes_downloaded / total_size * 100
            print(f"Download Progress: {percentage_of_completion:.2f}%")

        yt = YouTube(self.url, on_progress_callback=on_progress)

        video = yt.streams.filter(res=self.res).first()
        print(f"Downloading...{video.title}")
        video.download(output_path=self.get_output_path(), skip_existing=True)
        print("Download completed!")

    def run(self):
        if not self.url:
            print("no url")
            return False
        try:
            self.check_availability()
            self.download_video()
            return True
        except Exception as e:
            print(e)
            return False
