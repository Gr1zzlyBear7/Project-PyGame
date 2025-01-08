import sys
import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from btns import Button
from my_btns import *

pygame.init()
loud = 1
fps = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('test')
main_backround = pygame.image.load('images/viking960.png')
set_backround = pygame.image.load('images/valkirya960.png')
video_set_backround = pygame.image.load('images/home960.png')
new_game_bg = pygame.image.load('images/newgame960.png')
my_cur = pygame.image.load('images/471ab378cf8d4ca5a5f52e68ee61e29f.webp')
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
all_buttons = []


def main_menu():
    """Функция для создания главного меню"""
    global all_buttons
    start = to_new_game()
    settings = to_settings()
    quit = to_crash()

    all_buttons = [start, settings, quit]
    arr = [start, settings, quit]

    run = True
    while run:
        screen.fill((0, 0, 0))
        screen.blit(main_backround, (-270, 0))
        events = pygame.event.get()
        for event in events:
            run = close_menu(run, event)
            if event.type == pygame.USEREVENT and start.is_hovered:
                fade()
                new_game()
            if event.type == pygame.USEREVENT and settings.is_hovered:
                fade()
                settings_menu()
                for btn in [start, settings, quit]:
                    btn.set_pos(WIDTH / 2 - (300 / 2), btn.y)

            if event.type == pygame.USEREVENT and quit.is_hovered:
                run = False
            for btn in [start, settings, quit]:
                btn.handle_event(event)
        draw_btns(arr)

        cur_image()
        pygame.display.update()


def settings_menu():
    """Функция для создания экрана с настройками"""
    global all_buttons
    audio = settings_audio_btn()
    video = settings_video_btn()
    back = back_to_menu()

    all_buttons = [audio, video, back]
    arr = [audio, video, back]

    run = True
    while run:
        screen.fill((0, 0, 0))
        screen.blit(set_backround, (0, -100))

        for set_event in pygame.event.get():
            run = close_menu(run, set_event, back)

            if set_event.type == pygame.USEREVENT and video.is_hovered:
                fade()
                video_settings_menu()
                for btn in [audio, video, back]:
                    btn.set_pos(WIDTH / 2 - (300 / 2), btn.y)
            if set_event.type == pygame.USEREVENT and audio.is_hovered:
                fade()
                audoi_settings_menu()
            for btn in [audio, video, back]:
                btn.handle_event(set_event)

        draw_btns(arr)
        cur_image()
        pygame.display.flip()


def video_settings_menu():
    """Функция с кнопками для настроек расширения экрана"""
    global all_buttons
    full_hd = change_to_large_ext()
    ext_960x550 = change_to_little_ext()
    back_from_video = back_to_settings_from_video()

    all_buttons = [full_hd, ext_960x550, back_from_video]
    arr = [full_hd, ext_960x550, back_from_video]
    run = True
    while run:
        screen.fill((0, 0, 0))
        screen.blit(video_set_backround, (0, -100))

        for video_set_event in pygame.event.get():
            run = close_menu(run, video_set_event, back_from_video)

            if video_set_event.type == pygame.USEREVENT and ext_960x550.is_hovered:
                change_video_mode(960, 550)

            if video_set_event.type == pygame.USEREVENT and full_hd.is_hovered:
                change_video_mode(1920, 1080, pygame.FULLSCREEN)

            for btn in [ext_960x550, full_hd, back_from_video]:
                btn.handle_event(video_set_event)

        draw_btns(arr)

        cur_image()
        pygame.display.flip()


def audoi_settings_menu():
    """Функция для настроек звука игры"""
    global all_buttons, loud
    slider = Slider(screen, 100, 100, 600, 40, min=0, max=100, step=1)
    slider.setValue(loud * 100)
    back_from_audio = back_to_settings_from_audio()
    all_buttons = [back_from_audio]
    arr = [back_from_audio]
    output = TextBox(screen, 800, 100, 50, 50, fontSize=15)
    output.disable()

    run = True
    while run:
        screen.fill((0, 0, 0))
        loud = slider.getValue() / 100
        pygame.mixer.music.set_volume(loud)
        output.setText(int(loud * 100))
        screen.blit(video_set_backround, (0, -100))
        for button in global_buttons:
            if button.sound:
                button.sound.set_volume(loud)
        events = pygame.event.get()

        for event in events:
            run = close_menu(run, event, back_from_audio)
            back_from_audio.handle_event(event)

        draw_btns(arr)

        cur_image()

        pygame_widgets.update(events)
        pygame.display.update()


def new_game():
    """Функция работает после нажатия на кнопку старт"""
    global all_buttons
    new_game = create_new()
    continue_btn = play_cont()
    back_from_game = back_from_game_cred_to_menu()

    all_buttons = [new_game, continue_btn, back_from_game]
    arr = [new_game, continue_btn, back_from_game]

    run = True
    while run:
        screen.fill((0, 0, 0))
        screen.blit(main_backround, (-270, 0))
        events = pygame.event.get()
        for event in events:
            run = close_menu(run, event, back_from_game)
            if event.type == pygame.USEREVENT and new_game.is_hovered:
                fade()
                play_new()
            if event.type == pygame.USEREVENT and continue_btn.is_hovered:
                fade()

            for btn in all_buttons:
                btn.handle_event(event)

        draw_btns(arr)
        cur_image()
        pygame.display.update()


def previous_game():
    """Запускает предыдущую игру"""
    pass


def play_new():
    """Запускает новую игру"""
    global all_buttons

    easy = easy_toggle()
    medium = medium_toggle()
    back_from_game_creating = back_from_game_creating_to_menu()
    arr = [easy, medium, back_from_game_creating]
    all_buttons = [easy, medium, back_from_game_creating]

    run = True
    while run:
        screen.fill((0, 0, 0))
        screen.blit(new_game_bg, (0, -100))

        for event in pygame.event.get():
            run = close_menu(run, event, back_from_game_creating)
            if event.type == pygame.USEREVENT and easy.is_hovered:
                fade()
            if event.type == pygame.USEREVENT and medium.is_hovered:
                fade()
            for btn in arr:
                btn.handle_event(event)

        draw_btns(arr)

        cur_image()
        pygame.display.flip()


def fade():
    """Функция отвечает за плавный переход в кнопках"""
    run = True
    fade_alpha = 0  # отвечает за прозрачность

    while run:
        for set_event in pygame.event.get():
            if set_event.type == pygame.QUIT:
                run = False

        fade_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        fade_alpha += 5
        if fade_alpha >= 110:
            fade_alpha = 255
            run = False

        pygame.display.flip()
        clock.tick(fps)


def close_menu(run, event, btn=None):
    """Если нажали на крестик, то выходит из приложения, а если на кнопку Back, то возвращает в предыдущее меню"""
    if event.type == pygame.QUIT:
        run = False
        sys.exit()
    if btn:
        if event.type == pygame.USEREVENT and btn.is_hovered:
            fade()
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                btn.sound.play()
                fade()
                run = False
    return run


def change_video_mode(w, h, full_screen=0):
    """В функции представленна сменя расщирения экрана"""
    global WIDTH, HEIGHT, screen, main_backround, set_backround, video_set_backround, new_game_bg, all_buttons
    WIDTH, HEIGHT = w, h
    screen = pygame.display.set_mode((WIDTH, HEIGHT), full_screen)
    main_backround = pygame.image.load(f'images/viking{WIDTH}.png')
    set_backround = pygame.image.load(f'images/valkirya{WIDTH}.png')
    video_set_backround = pygame.image.load(f'images/home{WIDTH}.png')
    new_game_bg = pygame.image.load(f'images/newgame{WIDTH}.png')
    if WIDTH == 1920:
        WIDTH = 1300
    for btn in all_buttons:
        btn.set_pos(button_pos_x, btn.y)
    fade()


def cur_image():
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        screen.blit(my_cur, pos)


def draw_btns(arr):
    for btn in arr:
        btn.check_hover(pygame.mouse.get_pos())
        btn.draw(screen)
