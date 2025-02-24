import pygame

def load_sound(name):
    sound =     pygame.mixer.Sound(name)
    return sound

def play_sound(sound):
        pygame.mixer.Sound.play(sound)

def set_music(name):
    music =     pygame.mixer.music.load(name)
    return music

def play_music():
        pygame.mixer.music.play()

def stop_all_music():
        pygame.mixer.music.stop()