from elements import *
import fonts as fnt
import pygame
import math
import sys
import time
import images
import sounds

resolutions = [
    { "width": 426, "height": 240, "name": "" },
    { "width": 640, "height": 360, "name": "" },
    { "width": 854, "height": 480, "name": "" },
    { "width": 1280, "height": 720, "name": "HD" },
    { "width": 1366, "height": 768, "name": "HD" },
    { "width": 1600, "height": 900, "name": "HD+" },
    { "width": 1920, "height": 1080, "name": "Full HD" },
    { "width": 2560, "height": 1440, "name": "2K" },
    { "width": 3200, "height": 1800, "name": "QHD+" },
    { "width": 3840, "height": 2160, "name": "4K" }
]

# create a pygame window with the first HD resolution
screen = pygame.display.set_mode((resolutions[3]["width"], resolutions[3]["height"]))
pygame.display.set_caption("ElEmEnTaAl")

# set the icon