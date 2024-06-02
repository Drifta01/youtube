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
        video = self.filter_stream()
        video.download(output_path=self.get_output_path(), skip_existing=True)

    def run(self):
        try:
            self.check_availability()
            self.download_video()
            return True
        except Exception as e:
            print(e)
            return False
