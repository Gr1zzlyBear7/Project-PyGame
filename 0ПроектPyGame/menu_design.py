import sys
import pygame
from btns import Button

pygame.init()

WIDTH, HEIGHT = 960, 550
fps = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('test')
main_backround = pygame.image.load('images/viking960.png')
set_backround = pygame.image.load('images/valkirya960.png')
video_set_backround = pygame.image.load('images/home960.png')
my_cur = pygame.image.load('images/471ab378cf8d4ca5a5f52e68ee61e29f.webp')
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
all_buttons = []


def main_menu():
    """Функция для создания главного меню"""
    global all_buttons
    button_pos_x = WIDTH / 2 - (300 / 2)

    start = Button(
        x=button_pos_x, y=100, width=300, height=100,
        text="Start",
        bg_color=pygame.Color(255, 255, 255, 128), text_color=(0, 0, 0),
        hover_color=pygame.Color(255, 100, 100, 128), border_color=(0, 100, 195),
        sound_path='sounds/btns_sound.mp3')

    # Инициализация кнопки настроек
    settings = Button(
        x=button_pos_x, y=210, width=300, height=100,
        text="Settings",
        bg_color=pygame.Color(0, 0, 255, 128), text_color=(0, 0, 0),
        hover_color=pygame.Color(255, 255, 100, 128), border_color=(100, 100, 0),
        sound_path='sounds/btns_sound.mp3')

    # Инициализация кнопки выхода
    quit = Button(
        x=button_pos_x, y=320, width=300, height=100,
        text="Quit",
        bg_color=pygame.Color(255, 0, 0, 128), text_color=(0, 0, 0),
        hover_color=pygame.Color(255, 100, 255, 128), border_color=(100, 0, 100),
        sound_path='sounds/btns_sound.mp3')

    all_buttons = [start, settings, quit]

    run = True
    while run:
        screen.fill((0, 0, 0))
        screen.blit(main_backround, (-270, 0))

        for event in pygame.event.get():
            run = close_menu(run, event)
            if event.type == pygame.USEREVENT and start.is_hovered:
                fade()
            if event.type == pygame.USEREVENT and settings.is_hovered:
                fade()
                settings_menu()
                for btn in [start, settings, quit]:
                    btn.set_pos(WIDTH / 2 - (300 / 2), btn.y)

            if event.type == pygame.USEREVENT and quit.is_hovered:
                run = False
            for btn in [start, settings, quit]:
                btn.handle_event(event)

        for btn in [start, settings, quit]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        if pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()
            screen.blit(my_cur, pos)
        pygame.display.flip()


def settings_menu():
    """Функция для создания экрана с настройками"""
    global all_buttons
    button_pos_x = WIDTH / 2 - (300 / 2)

    # Инициализация кнопки для изменения громкости звука
    audio = Button(
        x=button_pos_x, y=100, width=300, height=100,
        text="Audio",
        bg_color=(139, 0, 0, 128), text_color=(0, 0, 0),
        hover_color=(165, 42, 42, 128), border_color=(0, 100, 195),
        sound_path='sounds/btns_sound.mp3')

    # Инициализация кнопки настройки расширения
    video = Button(
        x=button_pos_x, y=210, width=300, height=100,
        text="Video",
        bg_color=(106, 27, 27, 128), text_color=(0, 0, 0),
        hover_color=(165, 42, 42, 128), border_color=(100, 100, 0),
        sound_path='sounds/btns_sound.mp3')

    # Инициализация кнопки назад в главное меню
    back = Button(
        x=button_pos_x, y=320, width=300, height=100,
        text="Back",
        bg_color=(230, 10, 10, 128), text_color=(0, 0, 0),
        hover_color=(165, 42, 42, 128), border_color=(100, 0, 100),
        sound_path='sounds/btns_sound.mp3')

    all_buttons = [audio, video, back]

    run = True
    while run:
        screen.fill((0, 0, 0))
        screen.blit(set_backround, (0, -100))

        for set_event in pygame.event.get():
            run = close_menu(run, set_event)
            if set_event.type == pygame.USEREVENT and back.is_hovered:
                fade()
                run = False
            if set_event.type == pygame.KEYDOWN:
                if set_event.key == pygame.K_ESCAPE:
                    back.sound.play()
                    fade()
                    run = False
            if set_event.type == pygame.USEREVENT and video.is_hovered:
                fade()
                video_settings_menu()
                for btn in [audio, video, back]:
                    btn.set_pos(WIDTH / 2 - (300 / 2), btn.y)
            if set_event.type == pygame.USEREVENT and audio.is_hovered:
                fade()
            for btn in [audio, video, back]:
                btn.handle_event(set_event)

        for btn in [audio, video, back]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        if pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()
            screen.blit(my_cur, pos)
        pygame.display.flip()


def video_settings_menu():
    """Функция с кнопками для настроек расширения экрана"""
    global all_buttons
    button_pos_x = WIDTH / 2 - (300 / 2)

    # Инициализация кнопки для расширения экрана Full HD
    full_hd = Button(
        x=button_pos_x, y=100, width=300, height=100,
        text="Full HD",
        bg_color=(128, 128, 32, 128), text_color=(0, 0, 0),
        hover_color=(32, 64, 64, 128), border_color=(0, 100, 195),
        sound_path='sounds/btns_sound.mp3')

    # Инициализация кнопки для расширения экрана 960 на 550
    ext_960x550 = Button(
        x=button_pos_x, y=210, width=300, height=100,
        text="960x550",
        bg_color=(32, 64, 64, 128), text_color=(0, 0, 0),
        hover_color=(55, 90, 0, 128), border_color=(100, 100, 0),
        sound_path='sounds/btns_sound.mp3')

    # Инициализация кнопки назад в меню настроек
    back_set = Button(
        x=button_pos_x, y=320, width=300, height=100,
        text="Back",
        bg_color=(128, 10, 10, 128), text_color=(0, 0, 0),
        hover_color=(40, 42, 42, 128), border_color=(100, 0, 100),
        sound_path='sounds/btns_sound.mp3')

    all_buttons = [full_hd, ext_960x550, back_set]
    run = True
    while run:
        screen.fill((0, 0, 0))
        screen.blit(video_set_backround, (0, -100))

        for video_set_event in pygame.event.get():
            run = close_menu(run, video_set_event)
            if video_set_event.type == pygame.USEREVENT and back_set.is_hovered:
                fade()
                run = False

            if video_set_event.type == pygame.KEYDOWN:
                if video_set_event.key == pygame.K_ESCAPE:
                    back_set.sound.play()
                    fade()
                    run = False

            if video_set_event.type == pygame.USEREVENT and ext_960x550.is_hovered:
                change_video_mode(960, 550)

            if video_set_event.type == pygame.USEREVENT and full_hd.is_hovered:
                change_video_mode(1920, 1080, pygame.FULLSCREEN)

            for btn in [ext_960x550, full_hd, back_set]:
                btn.handle_event(video_set_event)

        for btn in [ext_960x550, full_hd, back_set]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        if pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()
            screen.blit(my_cur, pos)
        pygame.display.flip()


def new_game():
    """Функция работает после нажатия на кнопку старт"""
    pass


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


def close_menu(run, event):
    """Если нажали на крестик, то выходит из приложения"""
    if event.type == pygame.QUIT:
        run = False
        sys.exit()
    return run


def change_video_mode(w, h, full_screen=0):
    """В функции представленна сменя расщирения экрана"""
    global WIDTH, HEIGHT, screen, main_backround, set_backround, video_set_backround, all_buttons
    WIDTH, HEIGHT = w, h
    screen = pygame.display.set_mode((WIDTH, HEIGHT), full_screen)
    main_backround = pygame.image.load(f'images/viking{WIDTH}.png')
    set_backround = pygame.image.load(f'images/valkirya{WIDTH}.png')
    video_set_backround = pygame.image.load(f'images/home{WIDTH}.png')
    if WIDTH == 1920:
        WIDTH = 1300
    button_pos_x = WIDTH / 2 - (300 / 2)
    for btn in all_buttons:
        btn.set_pos(button_pos_x, btn.y)
    fade()
