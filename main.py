import dearpygui.dearpygui as dpg
from youtube_converter import YouTubeManager


def image_loader(file_name, texture_tage):
    w, h, channels, data = dpg.load_image(file_name)

    with dpg.texture_registry(show=True):
        dpg.add_static_texture(width=w, height=h, default_value=data, tag=texture_tage)


class MainApplication:

    def __init__(self):
        dpg.create_context()

        self.youtube_manager = YouTubeManager()

        image_loader("data/images/logo.png", "logo")

        dpg.create_viewport(title="YouTube Converter", width=1000, height=600, resizable=False)
        self.current_viewport_width = dpg.get_viewport_width()
        self.current_viewport_height = dpg.get_viewport_height()
        self.url = None
        dpg.setup_dearpygui()
        dpg.show_viewport()

    def menu_callback(self):
        print("callback")
        print(self.current_viewport_width)

    def convert(self):
        url = dpg.get_value("url_tag")
        self.youtube_manager.download(url)

    def draw(self):
        with dpg.window(label="Example Window", width=self.current_viewport_width,
                        height=self.current_viewport_height, no_title_bar=True, no_resize=True, no_move=True):
            with dpg.menu_bar():
                with dpg.menu(label="File"):
                    dpg.add_menu_item(label="Open Download Location", callback=self.menu_callback())

                with dpg.menu(label="Settings"):
                    dpg.add_menu_item(label="File Format", callback=self.menu_callback())
                    dpg.add_menu_item(label="Set Download Location", callback=self.menu_callback())

                with dpg.menu(label="Help"):
                    dpg.add_menu_item(label="Version", callback=self.menu_callback())
                    dpg.add_menu_item(label="About", callback=self.menu_callback())

            dpg.add_image("logo", width=350, height=300, pos=[self.current_viewport_width // 3,
                                                              (self.current_viewport_height // 2) - 300])

            dpg.add_input_text(tag="url_tag", label="Video URL", default_value="https://music.youtube.com/watch?v="
                                                                               "b1HsNByXsdc&list=RDAMVMb1HsNByXsdc",
                               width=dpg.get_viewport_width() // 2, pos=[self.current_viewport_width // 4,
                                                                         (
                                                                                 self.current_viewport_height //
                                                                                 2) + 30])

            dpg.add_button(label="Convert", pos=[self.current_viewport_width // 2,
                                                 (self.current_viewport_height // 2) + 80], callback=self.convert)

            dpg.render_dearpygui_frame()

    def destory(self):
        dpg.start_dearpygui()
        dpg.destroy_context()


def main():
    main_app = MainApplication()
    main_app.draw()
    main_app.destory()


main()
