from btns import Button
from size import *
import pygame

button_pos_x = WIDTH / 2 - (300 / 2)


def to_new_game():
    start = Button(
        x=button_pos_x, y=100, width=300, height=100,
        text="New Game",
        bg_color=pygame.Color(255, 255, 255, 128), text_color=(0, 0, 0),
        hover_color=pygame.Color(255, 100, 100, 128), border_color=(0, 100, 195),
        sound_path='sounds/btns_sound.mp3')
    return start


# Инициализация кнопки настроек
def to_settings():
    settings = Button(
        x=button_pos_x, y=210, width=300, height=100,
        text="Settings",
        bg_color=pygame.Color(0, 0, 255, 128), text_color=(0, 0, 0),
        hover_color=pygame.Color(255, 255, 100, 128), border_color=(100, 100, 0),
        sound_path='sounds/btns_sound.mp3')
    return settings


# Инициализация кнопки выхода
def to_crash():
    quit = Button(
        x=button_pos_x, y=320, width=300, height=100,
        text="Quit",
        bg_color=pygame.Color(255, 0, 0, 128), text_color=(0, 0, 0),
        hover_color=pygame.Color(255, 100, 255, 128), border_color=(100, 0, 100),
        sound_path='sounds/btns_sound.mp3')
    return quit


# Инициализация кнопки для расширения экрана Full HD
def change_to_large_ext():
    full_hd = Button(
        x=button_pos_x, y=100, width=300, height=100,
        text="Full HD",
        bg_color=(128, 128, 32, 128), text_color=(0, 0, 0),
        hover_color=(32, 64, 64, 128), border_color=(0, 100, 195),
        sound_path='sounds/btns_sound.mp3')
    return full_hd


# Инициализация кнопки для расширения экрана 960 на 550
def change_to_little_ext():
    ext_960x550 = Button(
        x=button_pos_x, y=210, width=300, height=100,
        text="960x550",
        bg_color=(32, 64, 64, 128), text_color=(0, 0, 0),
        hover_color=(55, 90, 0, 128), border_color=(100, 100, 0),
        sound_path='sounds/btns_sound.mp3')
    return ext_960x550


# Инициализация кнопки назад в меню настроек
def back_to_settings_from_video():
    back_set = Button(
        x=button_pos_x, y=320, width=300, height=100,
        text="Back",
        bg_color=(128, 10, 10, 128), text_color=(0, 0, 0),
        hover_color=(40, 42, 42, 128), border_color=(100, 0, 100),
        sound_path='sounds/btns_sound.mp3')
    return back_set


# Инициализация кнопки для изменения громкости звука
def settings_audio_btn():
    audio = Button(
        x=button_pos_x, y=100, width=300, height=100,
        text="Audio",
        bg_color=(139, 0, 0, 128), text_color=(0, 0, 0),
        hover_color=(165, 42, 42, 128), border_color=(0, 100, 195),
        sound_path='sounds/btns_sound.mp3')
    return audio


# Инициализация кнопки настройки расширения
def settings_video_btn():
    video = Button(
        x=button_pos_x, y=210, width=300, height=100,
        text="Video",
        bg_color=(106, 27, 27, 128), text_color=(0, 0, 0),
        hover_color=(165, 42, 42, 128), border_color=(100, 100, 0),
        sound_path='sounds/btns_sound.mp3')
    return video


# Инициализация кнопки назад в главное меню
def back_to_menu():
    back = Button(
        x=button_pos_x, y=320, width=300, height=100,
        text="Back",
        bg_color=(230, 10, 10, 128), text_color=(0, 0, 0),
        hover_color=(165, 42, 42, 128), border_color=(100, 0, 100),
        sound_path='sounds/btns_sound.mp3')
    return back
