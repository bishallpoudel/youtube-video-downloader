#! /bin/python3

import os
import pytube
import urllib
from pytube.cli import on_progress

# For downloading video only
def videoDownload(yt):
    stream = yt.streams.filter(only_video=True)

    # Display available streams in tabuular form
    print("Available video format: ")
    print("{}\t{}\t\t{}\t{}".format("Itag", "Type", "Resolution", "Frame Rate"))
    print("------------------------------------------------")

    # Go through each ite of a stream
    for s in stream:
        print("{}\t{}\t{}\t\t{}".format(s.itag, s.mime_type, s.resolution, s.fps))

    # Filter required stream by itag
    choice = input("Enter itag: ")

    # Catch exception, if any
    try:
        print("Connecting...")

        # Get video
        video = yt.streams.get_by_itag(choice)

        # Calculate and display size in MB
        size = video.filesize/(1024*1024)
        print("Size: {0:.2f} MB".format(size))
        print("Downloading...")

        # Download
        dest = "videos/"
        video.download(output_path=dest)
        print("Done!!")

    except:
        print("Can't download.")


# Download video with audio
def videoAudioDownload(yt):
    stream = yt.streams.filter(progressive=True)

    # Display available video streams in tabuular form
    print("Available video format: ")
    print("{}\t{}\t\t{}\t{}".format("Itag", "Type", "Resolution", "Frame Rate"))
    print("------------------------------------------------")

    # Go through each ite of a stream
    for s in stream:
        print("{}\t{}\t{}\t\t{}".format(s.itag, s.mime_type, s.resolution, s.fps))

    # Filter required stream by itag
    choice = input("Enter itag: ")

    # Catch exception, if any
    try:
        print("Connecting...")

        # Get video
        video = yt.streams.get_by_itag(choice)

        # Calculate and display size in MB
        size = video.filesize/(1024*1024)
        print("Size: {0:.2f} MB".format(size))
        print("Downloading...")

        # Download
        dest = "videos/"
        video.download(output_path=dest)
        print("Done!!")

    except:
        print("Can't download.")


# Download audio only
def audioDownload(yt):
    stream = yt.streams.filter(only_audio=True)

    # Display available audio streams in tabuular form
    print("Available audio format: ")
    print("{}\t{}\t\t{}".format("Itag", "Type", "Bit Rate"))
    print("------------------------------------------------")

    # Go through each ite of a stream
    for s in stream:
        print("{}\t{}\t{}".format(s.itag, s.mime_type, s.abr))

    # Filter required stream by itag
    choice = input("Enter itag: ")

    # Catch exception, if any
    try:
        print("Connecting...")

        # Get audio
        audio = yt.streams.get_by_itag(choice)

        # Calculate and display size in MB
        size = audio.filesize/(1024*1024)
        print("Size: {0:.2f} MB".format(size))
        print("Downloading...")

        # Download
        dest = "audios/"
        op_file = audio.download(output_path=dest)

        # Rename to .mp3
        base, ext = os.path.splitext(op_file)
        new_file = base + ".mp3"
        os.rename(op_file, new_file)

        print("Done!!")

    except:
        print("Can't download.")


# Main function
def Main():
    # Try for given url, if not display error
    try:
        url = input("Enter Video url: ")

        yt = pytube.YouTube(url, on_progress_callback=on_progress)

        # Input for user choice
        print("What you want to download? ")
        Format = input("1. Video With Audio\n2. Video\n3. Audio\n")

        try:
            # Display title
            print(yt.title)

            # Divert through user's choice
            if Format == "1" or Format == "Video With Audio":
                print("Connection...")
                videoAudioDownload(yt)
                
            elif Format == "2" or Format == "Video":
                print("Connecting...")
                videoDownload(yt)

            elif Format == "3" or Format == "Audio":
                print("Connecting...")
                audioDownload(yt)

            else:
                print("Invalid Selection")

        except urllib.error.URLError:
            # catch Network error
            print("Network Not Found.")

    # RegExp error catch
    except pytube.exceptions.RegexMatchError:
        print("Invalid Url")

    except KeyboardInterrupt:
        print("\nExiting...")



if __name__ == "__main__":
    # Main function through which program started.
    Main()
    print("Program Terminated.")