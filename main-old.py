import dearpygui.dearpygui as dpg
from youtube_converter import YouTubeManager
from util import dynamic_image_loader


class MainApplication:

    def __init__(self):
        dpg.create_context()

        self.youtube_manager = YouTubeManager(dpg)

        dynamic_image_loader("data/images/logo.png", "logo")
        dynamic_image_loader("data/images/default.jpg", "thumb_nail")

        dpg.create_viewport(title="YouTube Converter", width=1000, height=600, resizable=False,
                            max_width=1000,
                            max_height=600)
        self.current_viewport_width = dpg.get_viewport_width()
        self.current_viewport_height = dpg.get_viewport_height()
        self.url = None
        dpg.setup_dearpygui()
        dpg.show_viewport()

    def menu_callback(self):
        print("callback")
        print("me")

    def convert(self):
        dpg.hide_item("url_tag")
        dpg.hide_item("convert_button")
        dpg.show_item("progress_bar")
        dpg.show_item("progress_text")
        url = dpg.get_value("url_tag")
        self.youtube_manager.download(url)

    def draw(self):
        with dpg.viewport_menu_bar(label="Menu_Bar", tag="Menu_bar_tag", parent="main_window"):
            with dpg.menu(label="File"):
                dpg.add_menu_item(label="Open Download Location", callback=self.menu_callback)

            with dpg.menu(label="Settings"):
                dpg.add_menu_item(label="File Format", callback=self.menu_callback)
                dpg.add_menu_item(label="Set Download Location", callback=self.menu_callback)

            with dpg.menu(label="Help"):
                dpg.add_menu_item(label="Version", callback=self.menu_callback)
                dpg.add_menu_item(label="About", callback=self.menu_callback)

        with dpg.window(label="Example Window", width=self.current_viewport_width,
                        height=self.current_viewport_height, no_title_bar=True, no_resize=True, no_move=True,
                        tag="main_window", pos=[0, 19]):
            dpg.add_image("logo", tag="logo_box", width=350, height=300, pos=[self.current_viewport_width // 3,
                                                              (self.current_viewport_height // 2) - 300])

            dpg.add_image("thumb_nail", tag="thumb_box", width=350, height=250, show=False,
                          pos=[self.current_viewport_width // 3,
                               (self.current_viewport_height // 2) - 270])

            dpg.add_progress_bar(tag="progress_bar", width=350, show=False, pos=[
                (self.current_viewport_width // 3) - 4,
                (self.current_viewport_height // 2) + 80])

            dpg.add_text(default_value="Downloading Video...", pos=[
                self.current_viewport_width // 3,
                (self.current_viewport_height // 2) + 30], show=False, tag="progress_text")

            dpg.add_input_text(tag="url_tag", label="Video URL", default_value="https://music.youtube.com/watch?v="
                                                                               "b1HsNByXsdc&list=RDAMVMb1HsNByXsdc",
                               width=dpg.get_viewport_width() // 2, pos=[self.current_viewport_width // 4,
                                                                         (
                                                                                 self.current_viewport_height //
                                                                                 2) + 30])

            dpg.add_button(tag="convert_button", label="Convert", pos=[self.current_viewport_width // 2,
                                                                       (self.current_viewport_height // 2) + 80],
                           callback=self.convert)

            dpg.render_dearpygui_frame()

    def destory(self):
        dpg.start_dearpygui()
        dpg.destroy_context()


def main():
    main_app = MainApplication()
    main_app.draw()
    main_app.destory()


main()
