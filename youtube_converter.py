# built in
import os
import time
# third party
from pytube import YouTube
from moviepy.editor import VideoFileClip


class YouTubeManager:

    def __init__(self):
        self.media_format = "MP3"
        self.clip = None
        self.video_title = None
        self.thumbnail_url = None

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
        self.clip.close()
        os.remove(f"data/temp/{self.video_title}.MP4")

        # todo manage for mp4 only

        print("loading default image -----")

        # loading the default texture
        # dpg.hide_item("thumb_box")
        # dpg.show_item("logo_box")
        #
        # print("done delete video")
        # dpg.set_value("progress_text", "Done...")
        # dpg.set_value("progress_bar", 1)
        # time.sleep(5)
        # dpg.set_value("progress_text", "Downloading Video...")
        # dpg.set_value("progress_bar", 0)
        # dpg.show_item("url_tag")
        # dpg.show_item("convert_button")
        # dpg.hide_item("progress_bar")
        # dpg.hide_item("progress_text")

    def on_progress_audio(self, percentage):
        pass

    def on_done(self, something, something_2):
        # check what media format we need to convert to
        # todo if its MP3 we do this we need to pull from the settings object
        time.sleep(5)

        # data = dynamic_image_loader(f"data/temp/temp_images/{self.video_title}.jpg", "thumb")
        # dpg.set_value("thumb_nail", data)
        #
        # dpg.hide_item("logo_box")
        # dpg.show_item("thumb_box")

        # w, h, channels, data = dpg.load_image(f"data/temp/temp_images/{self.video_title}.jpg")
        #
        # with dpg.texture_registry(show=True):
        #     dpg.add_dynamic_texture(width=w, height=h, default_value=data, tag="thumb")
        #
        # dpg.add_image("thumb", width=350, height=300)

        # dpg.set_value("progress_text", "Extracting audio from video...")
        # dpg.set_value("progress_bar", 0)

        video_file = f"data/temp/{self.video_title}.MP4"
        output_ext = "mp3"
        filename = f"data/temp/{self.video_title}"
        self.clip = VideoFileClip(video_file)
        self.clip.audio.write_audiofile(f"{filename}.{output_ext}", self.on_complete, self.on_progress_audio)

    def download(self, url):
        """
        will output audio or video file to user specified location
        :param url:
        :return:
        """
        self.video_title = YouTube(url).title
        self.thumbnail_url = YouTube(url).thumbnail_url

        # might be a hanging here and would need a thread in the further
        # download the thumbnail before the video

        youtube_downloader = YouTube(url, self.on_progress, self.on_done).streams.filter(progressive=True,
                                                                                         file_extension='mp4') \
            .order_by('resolution') \
            .first().download(output_path="data/temp", filename=f"{self.video_title}.MP4")
