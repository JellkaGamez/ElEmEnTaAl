import pygame
import src

def load_sound(name):
    sound = src.pygame.mixer.Sound(name)
    return sound

def play_sound(sound):
    src.pygame.mixer.Sound.play(sound)

def set_music(name):
    music = src.pygame.mixer.music.load(name)
    return music

def play_music():
    src.pygame.mixer.music.play()

def stop_all_music():
    src.pygame.mixer.music.stop()