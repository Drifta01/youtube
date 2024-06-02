import os
from pytube import YouTube


def download_yt_video(url, res, output_path=None):
    yt = YouTube(url)

    try:
        yt.check_availability()
        streams = yt.streams
        video = streams.filter(res=res).first()

        if not output_path:
            output_path = os.path.expanduser("~/Downloads")

        video.download(output_path=output_path, skip_existing=True)
        return True

    except Exception as e:
        print(e)
        return False
