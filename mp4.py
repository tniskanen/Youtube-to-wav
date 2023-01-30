from pytube import YouTube

def get_mp4(url, save_location, file_type):
    x = str(url)
    yt = YouTube(x)
    #stream = yt.streams.filter(only_audio=True) webm(251) mp4(140)
    stream = yt.streams.get_by_itag(file_type)
    stream.download(output_path=save_location)


