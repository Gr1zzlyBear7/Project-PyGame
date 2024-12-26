import pygame


class Button:
    """В данном классе реализованно: отрисовка кнопки с указанными параметрами, и обработка нажатия на кнопку"""
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

    def set_pos(self, x, y=0):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, screen):
        button_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        current_color = self.hover_color if self.is_hovered else self.bg_color
        button_surface.fill(current_color)
        pygame.draw.rect(button_surface, self.border_color, button_surface.get_rect(), width=5)
        screen.blit(button_surface, (self.x, self.y))
        font = pygame.font.Font(None, 40)
        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=(self.width // 2, self.height // 2))
        button_surface.blit(text_surf, text_rect)
        screen.blit(button_surface, (self.x, self.y))

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button_start=self))
