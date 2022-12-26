'''
Author: Amine Abouothmane
'''

from pytube import YouTube

def DownloadVideo(link):
    youtubeObject=YouTube(link)
    print("*********************Video Title************************")
    print(youtubeObject.title)
    print("********************Tumbnail Image***********************")
    print(youtubeObject.thumbnail_url)
    print("********************Download video*************************")
    youtubeObject=youtubeObject.streams.get_highest_resolution()
    try:
      youtubeObject.download()
      print("downloaded successfully")
    except:
      print("error while downloading video ")
def DownloadMusic(link):
    youtubeObject=YouTube(link)
    print("*********************Video Title************************")
    print(youtubeObject.title)
    print("********************Tumbnail Image***********************")
    print(youtubeObject.thumbnail_url)
    print("********************Download video*************************")
    youtubeObject=youtubeObject.streams.get_audio_only()
    try:
      youtubeObject.download()
      print("downloaded successfully")
    except:
      print("error while downloading video ")



link =input("enter the youtube link URL: ")
DownloadVideo(link)
#DownloadMusic(link)