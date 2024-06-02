import subprocess
from setuptools import setup, Command


class BuildCommand(Command):
    description = "Build the project using PyInstaller"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.run(
            ["pyinstaller", "main.py", "-F", "--windowed", "-n", "Youtube Downloader"]
        )


setup(
    name="YouTubeDL",
    version="0.2",
    author="David Poole",
    description="A simple YouTube video downloader",
    packages=[],
    install_requires=["pytube"],
    entry_points={
        "console_scripts": ["downloader = main:main"],
    },
    cmdclass={
        "build": BuildCommand,
    },
)
