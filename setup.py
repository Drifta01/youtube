from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ytdl",
    version="0.3",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ytdl = youtube_downloader.main:main",
        ],
    },
)
