import pygame


class Button:
    def __init__(self, x, y, width, height, text, bg_color, text_color, hover_color, border_color, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.bg_color = bg_color
        self.text_color = text_color
        self.hover_color = hover_color
        self.border_color = border_color
        self.is_hovered = False
        self.rect = pygame.Rect(x, y, width, height)
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)
        self.is_hovered = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.border_color, self.rect)
        current_color = self.hover_color if self.is_hovered else self.bg_color
        inner_rect = self.rect.inflate(-5, -5)
        pygame.draw.rect(screen, current_color, inner_rect)

        font = pygame.font.Font(None, 30)
        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button_start=self))


class Buttons:
    def __init__(self):
        self.start = Button(
            x=200, y=100, width=200, height=100,
            text="Start",
            bg_color=(255, 255, 255), text_color=(0, 0, 0),
            hover_color=(255, 100, 100), border_color=(0, 100, 195),
            sound_path='sounds/btns_sound.mp3')
        self.settings = Button(
            x=200, y=220, width=200, height=100,
            text="Settings",
            bg_color=(0, 0, 255), text_color=(0, 0, 0),
            hover_color=(255, 255, 100), border_color=(100, 100, 0),
            sound_path='sounds/btns_sound.mp3')
        self.quit = Button(
            x=200, y=340, width=200, height=100,
            text="Quit",
            bg_color=(255, 0, 0), text_color=(0, 0, 0),
            hover_color=(255, 100, 255), border_color=(100, 0, 100),
            sound_path='sounds/btns_sound.mp3')
