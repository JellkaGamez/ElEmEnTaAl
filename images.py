import pygame

def load_image(name):
    img = pygame.image.load(name)
    return img

def scale_image(image, width, height):
    img = pygame.transform.smoothscale(image, (width, height))
    return img

def render_image(image, surface, x, y, ox=0, oy=0):
    surface.blit(image, (x + ox, y + oy))

def render_square(surface, color, x, y, width, height, alpha=0):
    s = pygame.Surface((width, height))
    s.set_alpha(alpha)
    s.fill(color)
    surface.blit(s, (x, y))