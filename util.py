import dearpygui.dearpygui as dpg


text_holder = None

def static_image_loader(file_name, texture_tage):
    w, h, channels, data = dpg.load_image(file_name)

    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=w, height=h, default_value=data, tag=texture_tage)

    return data


def dynamic_image_loader(file_name, texture_tage):
    w, h, channels, data = dpg.load_image(file_name)

    with dpg.texture_registry(show=False):
        dpg.add_dynamic_texture(width=w, height=h, default_value=data, tag=texture_tage)

    return data
