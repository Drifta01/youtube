# YouTube Downloader

## Run
```bash
conda create -n youtube-dl python=3.11
conda activate youtube-dl
pip install -r requirements.txt
```

## Build

```bash
pyinstaller --onefile --windowed YouTubeDL.py
```