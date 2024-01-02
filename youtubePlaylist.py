from pytube import Playlist

playlist = Playlist("your-url-here")

print("Total Videos in Playlist:", len(playlist.video_urls))

# Initialize a counter
downloaded_count = 0

for video in playlist.videos:
    # Get the highest resolution stream
    stream = video.streams.get_highest_resolution()
    
    # Download the video
    stream.download()
    
    # Increment the counter
    downloaded_count += 1
    
    # Print the progress
    print(f"Video {downloaded_count}/{len(playlist.video_urls)} downloaded")

print("Download completed.")
