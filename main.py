from elements import *
import fonts as fnt
import pygame
import math
import sys
import time
import images as img
import sounds as snd
import random
from colours import *

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

# initialize pygame
pygame.init()
pygame.font.init()

# set the settings
resolution = 3
vsync = False

# create a pygame window with the first HD resolution
screen = pygame.display.set_mode((resolutions[resolution]["width"], resolutions[resolution]["height"]))
pygame.display.set_caption("ElEmEnTaAl")

# set the icon
icon = img.load_image("assets\\icon.png")
pygame.display.set_icon(icon)

# set the font
font_tiny = fnt.load_font("assets\\main.ttf", 15)
font_small = fnt.load_font("assets\\main.ttf", 20)
font = fnt.load_font("assets\\main.ttf", 40)
font_big = fnt.load_font("assets\\main.ttf", 60)
font_logo = fnt.load_font("assets\\main.ttf", 100)

# set the music
snd.set_music("assets\\lobby-time.mp3")

# set the type of boxes
boxes = ['basic', 'dice']

# set the box
box = img.load_image(f"assets\\boxes\\{boxes[0]}.png")

# play the music
snd.play_music()

# set the clock
clock = pygame.time.Clock()

# set the background
background = img.load_image("assets\\wood.png")

# scale the background
background = img.scale_image(background, resolutions[3]["width"], resolutions[3]["height"])

# set the cursor
cursor = img.load_image("assets\\cursor.png")

# hide the cursor
pygame.mouse.set_visible(False)

# create new buffer screen
buffer = pygame.Surface((resolutions[3]["width"], resolutions[3]["height"]))

# set logo colours
colours = [
    (255, 111, 97),   # coral
    (0, 168, 168),    # teal
    (241, 209, 0),    # sunflower yellow
    (62, 74, 137),    # indigo
    (144, 190, 109),  # moss Green
    (194, 84, 227)    # vibrant purple
]
random.shuffle(colours)
colours_dark = []
for color in colours:
    colours_dark.append((color[0] // 2, color[1] // 2, color[2] // 2))

# logo drawing code
def render_logo():
    # draw elements
    i = 0
    for element in ['El', 'Em', 'En', 'Ta', 'Al']:
        # tint a box
        my_box = box.copy()
        my_box.fill(colours[i], None, pygame.BLEND_MULT)
        my_box = img.scale_image(my_box, 130, 130)

        text = font_logo.render(element, True, (255, 255, 255))
        text.fill(colours_dark[i], None, pygame.BLEND_MULT)

        if element == 'Em':
            my_box.blit(text, (10, 20))
        else:
            my_box.blit(text, (20, 20))

        buffer.blit(my_box, (i * 130 + ((my_box.get_width() * 5) // 2), 150))
        i += 1

class Layer:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.objs = []

    def add(self, obj):
        self.objs.append(obj)

    def remove(self, obj):
        self.objs.remove(obj)

    def update(self):
        for obj in self.objs:
            obj.update()
    
    def render(self):
        for obj in self.objs:
            obj.render()
class ImgButton:
    def __init__(self, image, x, y, width, height, tint):
        self.o_image = img.load_image(image)
        self.o_image = img.scale_image(self.o_image, width, height)
        self.o_image.fill(tint, None, pygame.BLEND_MULT)
        self.image = self.o_image.copy()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.size = 1

    def hover(self, mouse_x, mouse_y):
        if self.x - self.width // 2 <= mouse_x <= self.x + self.width // 2 and \
           self.y - self.height // 2 <= mouse_y <= self.y + self.height // 2:
            return True
        return False
        
    def update(self):
        pass

    def render(self):
        self.image = img.scale_image(self.image, self.width * self.size, self.height * self.size)
        buffer.blit(self.image, (self.x - (self.width * self.size) // 2, self.y - (self.height * self.size) // 2))

def empty_button():
    print('empty button')
class MenuButton (ImgButton):
    def __init__(self, image, x, y, width, height, tint, func=empty_button, layer: Layer = None):
        super().__init__(image, x, y, width, height, tint)
        self.original_width = width
        self.original_height = height
        self.func = func
        self.clicked = False
        self.layer = layer

    def update(self):
        if self.hover(buffer_mouse_x, buffer_mouse_y) and current_layer == self.layer :
            self.size += (1.2 - self.size) * 0.1
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                self.size = 1.5
                self.func()
            elif not pygame.mouse.get_pressed()[0] and self.clicked:
                self.clicked = False
        else:
            self.size += (1 - self.size) * 0.1

        self.image = img.scale_image(self.o_image, self.width, self.height)

current_layer = None

class BG:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.image = img.load_image('assets\\wood.png')
        self.image = img.scale_image(self.image, width - 20, height - 20)
        self.screen = pygame.Surface((width, height))

    def render(self, ox=0, oy=0):
        # render a square filling self
        self.screen.fill(c_burly_wood)
        self.screen.blit(self.image, (10, 10))
        buffer.blit(self.screen, (self.x + ox, self.y + oy))

class PopupLayer (Layer):
    def __init__(self, x, y, target, width, height, layer: Layer = None):
        super().__init__(x, y, width, height)
        self.target = target
        self.layer = layer

    def update(self):
        if current_layer == self.layer:
            self.x += (self.target[0] - self.x) * 0.1
            self.y += (self.target[1] - self.y) * 0.1
        else:
            self.x += (self.target[0] - self.x) * 0.1
            self.y += (self.target[1] + self.width - self.y) * 0.1
    
    def render(self):
        for obj in self.objs:
            obj.render(ox = self.x, oy = self.y)

def set_settings():
    global current_layer
    current_layer = settings_layer

def init_settings():
    global current_layer, settings_layer
    print('init settings')
    settings_layer = PopupLayer(buffer.get_width() // 2 - 1100 // 2, (buffer.get_height() // 2 - 620 // 2) + 620, (buffer.get_width() // 2 - 1100 // 2, buffer.get_height() // 2 - 620 // 2), 1100, 620)
    settings_layer.layer = settings_layer
    settings_layer.add(BG(0, 0, 1100, 620))
    return settings_layer

def init_menu():
    menu_layer = Layer(0, 0, buffer.get_width(), buffer.get_height())

    play = MenuButton('assets\\play.png', buffer.get_width() // 2, buffer.get_height() // 2 + 100, 300, 300, colours[1], layer=menu_layer)
    settings = MenuButton('assets\\settings.png', buffer.get_width() // 2 + 300, buffer.get_height() // 2 + 100, 200, 200, colours[3], set_settings, menu_layer)
    jukebox = MenuButton('assets\\jukebox.png', buffer.get_width() // 2 - 300, buffer.get_height() // 2 + 100, 200, 200, colours[2], layer=menu_layer)

    menu_layer.add(play)
    menu_layer.add(settings)
    menu_layer.add(jukebox)

    return menu_layer

fps = 60 if vsync else 0

menu_layer = init_menu()
settings_layer = init_settings()
current_layer = menu_layer

# main loop
running = True
while running:
    # get the mouse position
    mouse = pygame.mouse.get_pos()

    # scale mouse coordinates to buffer space
    buffer_mouse_x = mouse[0] * (buffer.get_width() / screen.get_width())
    buffer_mouse_y = mouse[1] * (buffer.get_height() / screen.get_height())

    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # clear the screen
    buffer.fill((0, 0, 0))

    # draw the background
    img.render_image(background, buffer, 0, 0)

    # draw the logo
    render_logo()

    # draw the buttons
    menu_layer.update()
    menu_layer.render()

    # update the settings layer IF settings layer is the current layer
    settings_layer.update()
    settings_layer.render()

    # render the fps
    text = font_small.render("FPS: " + str(int(clock.get_fps())), True, (255, 255, 255))
    buffer.blit(text, (0, 0))

    # calculate buffer scale offset
    offset = (resolutions[resolution]["width"] - buffer.get_width()) // 2

    # render the credits
    credits = None
    with open("credits.txt", "r") as f:
        credits = f.read()

    credits = f"Credits\n{credits}"
    credits_lines = credits.split("\n")

    # remove everything in brackets
    for i, line in enumerate(credits_lines):
        if "(" in line:
            credits_lines[i] = line[:line.find("(")]

    for i, line in enumerate(credits_lines):
        text = font_tiny.render(line, True, (255, 255, 255))
        buffer.blit(text, (10, (buffer.get_height() - len(credits_lines) * 15) + (i * 15)))

    # draw the cursor
    img.render_image(cursor, buffer, buffer_mouse_x, buffer_mouse_y)

    # scale the buffer
    buffer_scaled = pygame.transform.smoothscale(buffer, (screen.get_width(), screen.get_height()))

    # draw the buffer to the screen
    screen.blit(buffer_scaled, (0, 0))

    # update the screen
    pygame.display.flip()

    # limit the frame rate
    clock.tick(fps)