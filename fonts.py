import pygame

def load_font(name, size):
    font = pygame.font.Font(name, size)
    return font

def render_text(text, font, color, surface, x, y):
    text = font.render(text, True, color)
    surface.blit(text, (x, y))