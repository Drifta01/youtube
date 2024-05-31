import click
from pytube import YouTube


@click.command()
@click.argument("url")
def download_yt_audio(url):
    yt = YouTube(url)

    try:
        yt.check_availability()
        streams = yt.streams
        # get a 720p video
        video = streams.filter(res="720p").first()

        print(f"Downloading {video.title}")
        video.download()
        print("Download complete!")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    download_yt_audio()
