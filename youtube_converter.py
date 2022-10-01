# built in
import os
import time
# third party
from pytube import YouTube
from moviepy.editor import VideoFileClip
from PyQt6.QtGui import *
import requests
from concurrent.futures import ThreadPoolExecutor
from PyQt6.QtCore import QRunnable,QThreadPool


# https://www.pythontutorial.net/python-concurrency/python-threadpoolexecutor/


# def thread_pool_handler(method_name):
#     with ThreadPoolExecutor() as executor:
#         task = executor.submit(method_name)


class AppThreadPool(QRunnable):

    def __init__(self, fun):
        super(AppThreadPool, self).__init__()
        self.fun = fun

    def run(self):
        self.fun()



class YouTubeManager:

    def __init__(self, py_qt_widgets):
        self.media_format = "MP3"
        self.clip = None
        self.video_title = None
        self.thumbnail_url = None
        self.url = None
        self.py_qt_widgets = py_qt_widgets
        self.threadpool = QThreadPool()

    # todo   create settings object that holds all the states of the app such as user settings

    # def on_progess(self, something, something_2, bit):
    #     print(type(something))
    #     print(type(something_2))
    #
    #     print("something" + str(something_2))
    #     # print("Something 1 " + something)
    #     # print("Something 2" + something_2)
    #     # print(bit)

    # def thumb_loader(self):

    def on_progress(self, vid, chunk, bytes_remaining):
        total_size = vid.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        totalsz = (total_size / 1024) / 1024
        totalsz = round(totalsz, 1)
        remain = (bytes_remaining / 1024) / 1024
        remain = round(remain, 1)
        dwnd = (bytes_downloaded / 1024) / 1024
        dwnd = round(dwnd, 1)
        percentage_of_completion = round(percentage_of_completion, 2)
        # dpg.set_value("progress_bar", percentage_of_completion // 100)

        # print(f'Total Size: {totalsz} MB')
        # print( f'Download Progress: {percentage_of_completion}%, Total Size:{totalsz} MB, Downloaded: {dwnd} MB,
        # Remaining:{remain} MB')

    def on_complete(self):
        print("deleting file")
        self.py_qt_widgets.get("bottom_status_label").setText("Cleaning up....")
        self.py_qt_widgets.get("bottom_status_label").setStyleSheet("color: yellow")
        self.clip.close()
        time.sleep(5)
        os.remove(f"data/temp/{self.video_title}.MP4")

        # todo manage for mp4 only

        print("loading default image -----")

        self.py_qt_widgets.get("spinner").hide()
        self.py_qt_widgets.get("convert_button").show()
        self.py_qt_widgets.get("text_box").show()
        self.py_qt_widgets.get("status_label").hide()
        pixmap = QPixmap('data/images/logo.png')
        self.py_qt_widgets.get("logo").setPixmap(pixmap.scaled(400, 300))
        self.py_qt_widgets.get("bottom_status_label").show()
        self.py_qt_widgets.get("bottom_status_label").setStyleSheet("color: green")
        self.py_qt_widgets.get("bottom_status_label").setText("Done...")
        time.sleep(5)
        self.py_qt_widgets.get("bottom_status_label").hide()
        self.py_qt_widgets.get("bottom_status_label").setStyleSheet("color: white")



    def on_progress_audio(self, percentage):
        pass

    def load_image(self):
        thumbnail_image_data = QImage()
        thumbnail_image_data.loadFromData(requests.get(self.thumbnail_url).content)
        print(thumbnail_image_data)
        print(self.thumbnail_url)
        self.py_qt_widgets.get("logo").setPixmap(QPixmap(thumbnail_image_data).scaled(300, 200))

    def extract_audio(self):
        video_file = f"data/temp/{self.video_title}.MP4"
        output_ext = "mp3"
        filename = f"data/temp/{self.video_title}"
        self.clip = VideoFileClip(video_file)
        self.clip.audio.write_audiofile(f"{filename}.{output_ext}", self.on_complete, self.on_progress_audio)

    def on_done(self, something, something_2):
        # check what media format we need to convert to
        # todo if its MP3 we do this we need to pull from the settings object

        self.py_qt_widgets.get("bottom_status_label").setText("Extracting Audio...")
        self.py_qt_widgets.get("bottom_status_label").setStyleSheet("color: red")
        self.py_qt_widgets.get("bottom_status_label").show()

        extract_audio_worker = AppThreadPool(self.extract_audio)
        self.threadpool.start(extract_audio_worker)

        # thread_pool_handler(self.download_video_thread)

    def download_video_thread(self):
        youtube_downloader = YouTube(self.url, self.on_progress, self.on_done) \
            .streams.filter(progressive=True, file_extension='mp4').order_by('resolution') \
            .first().download(output_path="data/temp", filename=f"{self.video_title}.MP4")

    def download(self, url):
        """
        will output audio or video file to user specified location
        :param url:
        :return:
        """
        self.video_title = YouTube(url).title
        self.thumbnail_url = YouTube(url).thumbnail_url
        self.py_qt_widgets.get("spinner").show()
        self.py_qt_widgets.get("convert_button").hide()
        self.py_qt_widgets.get("text_box").hide()
        self.py_qt_widgets.get("status_label").setText(self.video_title)
        self.py_qt_widgets.get("status_label").show()
        self.py_qt_widgets.get("status_bar").show()
        self.py_qt_widgets.get("bottom_status_label").setText("Downloading Video....")
        self.py_qt_widgets.get("bottom_status_label").show()
        self.url = url
        self.load_image()

        download_video_worker = AppThreadPool(self.download_video_thread)
        self.threadpool.start(download_video_worker)


        # might be a hanging here and would need a thread in the further
        # download the thumbnail before the video
        # thread_pool_handler(self.download_video_thread)

