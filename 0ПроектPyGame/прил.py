import pygame
from btns import Buttons

pygame.init()
size = WIDTH, HEIGHT = 600, 550
screen = pygame.display.set_mode(size)


def main():
    pygame.init()
    pygame.display.set_caption("Main_Menu")
    clock = pygame.time.Clock()

    buttons = Buttons()
    button_start = buttons.start
    button_settings = buttons.settings
    button_quit = buttons.quit

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button_start.handle_event(event)
            button_settings.handle_event(event)
            button_quit.handle_event(event)

        mouse_pos = pygame.mouse.get_pos()
        button_start.check_hover(mouse_pos)
        button_settings.check_hover(mouse_pos)
        button_quit.check_hover(mouse_pos)

        button_start.draw(screen)
        button_settings.draw(screen)
        button_quit.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


