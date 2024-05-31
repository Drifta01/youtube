from setuptools import setup

setup(
    name="YouTubeDL",
    version="0.1",
    author="David Poole",
    description="A simple YouTube video downloader",
    packages=["downloader"],
    install_requires=["pytube"],
    entry_points={
        "console_scripts": [
            "youtubedl = downloader.main:main",
        ],
    },
)
