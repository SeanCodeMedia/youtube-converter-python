import xml.etree.ElementTree as et
import os


class Settings:

    def __init__(self):
        self.file_name = "data/app_settings.xml"
        self.settings_path = "data/"

        try:
            open("data/app_settings.xml", "x")
            self.generate_xml()
        except FileExistsError as e:
            print("exist ---")

    def generate_xml(self):
        root = et.Element("Settings")
        tree = et.ElementTree(root)

        with open(self.file_name, "wb") as files:
            tree.write(files)

    def set_audio_format(self, video_format):
        pass

    def get_audio_format(self):
        pass

    def set_download_location(self, location):
        pass

    def get_download_location(self):
        pass
