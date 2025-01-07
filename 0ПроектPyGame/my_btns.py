from btns import Button
from size import *
import pygame
pygame.mixer.init()
button_pos_x = WIDTH / 2 - (300 / 2)

# Инициализвция кнопки старт
start = Button(
    x=button_pos_x, y=100, width=300, height=100,
    text="New Game",
    bg_color=pygame.Color(255, 255, 255, 128), text_color=(0, 0, 0),
    hover_color=pygame.Color(255, 100, 100, 128), border_color=(0, 100, 195),
    sound_path='sounds/btns_sound.mp3')


def to_new_game():
    return start


# Инициализация кнопки настроек
settings = Button(
    x=button_pos_x, y=210, width=300, height=100,
    text="Settings",
    bg_color=pygame.Color(0, 0, 255, 128), text_color=(0, 0, 0),
    hover_color=pygame.Color(255, 255, 100, 128), border_color=(100, 100, 0),
    sound_path='sounds/btns_sound.mp3')


def to_settings():
    return settings


# Инициализация кнопки выхода

quit = Button(
    x=button_pos_x, y=320, width=300, height=100,
    text="Quit",
    bg_color=pygame.Color(255, 0, 0, 128), text_color=(0, 0, 0),
    hover_color=pygame.Color(255, 100, 255, 128), border_color=(100, 0, 100),
    sound_path='sounds/btns_sound.mp3')


def to_crash():
    return quit


# Инициализация кнопки для расширения экрана Full HD
full_hd = Button(
    x=button_pos_x, y=100, width=300, height=100,
    text="Full HD",
    bg_color=(128, 128, 32, 128), text_color=(0, 0, 0),
    hover_color=(32, 64, 64, 128), border_color=(0, 100, 195),
    sound_path='sounds/btns_sound.mp3')


def change_to_large_ext():
    return full_hd


# Инициализация кнопки для расширения экрана 960 на 550
ext_960x550 = Button(
    x=button_pos_x, y=210, width=300, height=100,
    text="960x550",
    bg_color=(32, 64, 64, 128), text_color=(0, 0, 0),
    hover_color=(55, 90, 0, 128), border_color=(100, 100, 0),
    sound_path='sounds/btns_sound.mp3')


def change_to_little_ext():
    return ext_960x550


# Инициализация кнопки назад в меню настроек
back_set = Button(
    x=button_pos_x, y=320, width=300, height=100,
    text="Back",
    bg_color=(128, 10, 10, 128), text_color=(0, 0, 0),
    hover_color=(40, 42, 42, 128), border_color=(100, 0, 100),
    sound_path='sounds/btns_sound.mp3')


def back_to_settings_from_video():
    return back_set


# Инициализация кнопки для изменения громкости звука
audio = Button(
    x=button_pos_x, y=100, width=300, height=100,
    text="Audio",
    bg_color=(139, 0, 0, 128), text_color=(0, 0, 0),
    hover_color=(165, 42, 42, 128), border_color=(0, 100, 195),
    sound_path='sounds/btns_sound.mp3')


def settings_audio_btn():
    return audio


# Инициализация кнопки настройки расширения
video = Button(
    x=button_pos_x, y=210, width=300, height=100,
    text="Video",
    bg_color=(106, 27, 27, 128), text_color=(0, 0, 0),
    hover_color=(165, 42, 42, 128), border_color=(100, 100, 0),
    sound_path='sounds/btns_sound.mp3')


def settings_video_btn():
    return video


# Инициализация кнопки назад в главное меню
back = Button(
    x=button_pos_x, y=320, width=300, height=100,
    text="Back",
    bg_color=(230, 10, 10, 128), text_color=(0, 0, 0),
    hover_color=(165, 42, 42, 128), border_color=(100, 0, 100),
    sound_path='sounds/btns_sound.mp3')


def back_to_menu():
    return back


# Инициализация кнопки назад в меню настроек из настроек аудио
back_set_fa = Button(
    x=button_pos_x, y=320, width=300, height=100,
    text="Back",
    bg_color=(100, 100, 255, 128), text_color=(0, 0, 0),
    hover_color=(40, 42, 42, 128), border_color=(100, 0, 100),
    sound_path='sounds/btns_sound.mp3')


def back_to_settings_from_audio():
    return back_set_fa


global_buttons = [start, settings, quit, audio, back_set, full_hd, ext_960x550, video, back, back_set_fa]
