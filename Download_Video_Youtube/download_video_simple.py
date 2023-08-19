# Coding With Kien

from pytube import YouTube

# Get the YouTube video URL from the user
url = input('Enter the YouTube video URL: ')

# Create a YouTube object with the video URL
yt = YouTube(url)

# Select the highest quality video stream
stream = yt.streams.get_highest_resolution()

# Download the video to the current working directory
stream.download()
