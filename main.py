from pytube import Channel
from pytube import YouTube
from moviepy.editor import *
import os 


def mp3(titre):
    print("Convertion ...")
    
    list = os.listdir('temp')
    mp4_file = "temp/"+list[0]
    
    print(mp4_file)

    mp3_file = "mp3/"+ list[0].replace(".mp4",".mp3")
    print(mp3_file)

    videoclip = VideoFileClip(mp4_file)

    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)

    audioclip.close()
    videoclip.close()


def clean(titre):
    list = os.listdir('temp')
    mp4_file = list[0]
    os.remove("temp/"+ mp4_file)


c = Channel('https://www.youtube.com/c/ABCRap/videos')

print("Downloading video by" , c.channel_name)
for video in c.videos:
    print("Telechargement de {} ...".format(video.title))
    video.streams.get_by_itag(18).download("temp/")
  
    mp3(video.title)
    clean(video.title)