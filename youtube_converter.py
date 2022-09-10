from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
import time

video_file = "data/temp/temp_video.mp4"
output_ext = "mp3"
filename = "data/temp/done_temp_"


class YouTubeManager:

    def __init__(self):

        self.media_format = "MP3"
        self.clip = VideoFileClip(video_file)

    # todo   create settings object that holds all the states of the app such as user settings

    def on_progess(self, something, something_2, bit):
        print("%%")


    def callback(self):
        print("deleting file")
        os.remove("data/temp/temp_video.mp4")
        print("done delete video")

    def on_done(self, something, something_2):


        clip.audio.write_audiofile(f"{filename}.{output_ext}", self.callback)
        clip.reader.close()
        clip.close()
        del clip.reader
        del clip
        clip.__del__()
        clip.reader.__del__()




    def download(self, url):
        """
        will output audio or video file to user specified location
        :param url:
        :return:
        """
        youtube_downloader = YouTube(url, self.on_progess, self.on_done).streams.filter(progressive=True,
                                                                                        file_extension='mp4') \
            .order_by('resolution') \
            .first().download(output_path="data/temp", filename="temp_video.mp4")
