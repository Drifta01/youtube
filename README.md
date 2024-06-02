# YouTube Downloader

## Run

Use a Conda virtual environment:
```sh
conda create -n youtube-dl python=3.11
conda activate youtube-dl
pip install -r requirements.txt
```

or to install globally:
```sh
pip install .
```

## Build an executable
(or download the latest [release](https://github.com/davidlpoole/YoutubeDownloader/releases/latest))

```sh
pip install pyinstaller  # if not already installed
```

```sh
pyinstaller main.py -F --windowed -n 'Youtube Downloader' --noconfirm
```

```sh
cp -r "dist/Youtube Downloader.app" /Applications/  # for macOS
```