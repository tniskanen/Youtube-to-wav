from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=4mBVHerH-dU')
#stream = yt.streams.filter(only_audio=True)
stream = yt.streams.get_by_itag(251)
stream.download(output_path='C:\\Users\\niska\\OneDrive\\Documents\\FL-Samples\\Youtube-MP4s')