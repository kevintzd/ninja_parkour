import os
import pygame

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

FLOOR_HEIGHT = 150
FLOOR_GAP_WIDTH = 150
# the gap of height between levels
FLOOR_GAP_HEIGHT = 30
INIT_HEIGHT = SCREEN_HEIGHT - FLOOR_HEIGHT
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
RESOURCES_PATH = os.path.join(BASE_DIR, 'resources')
CAPTION = 'Ninja Parkour'
FPS = 60

print(BASE_DIR)
print(RESOURCES_PATH)

BACKGROUND_IMAGE = {
    'background': os.path.join(RESOURCES_PATH, 'Sprites', 'Background', 'backgroundninja.png'),
    'menu_background': os.path.join(RESOURCES_PATH, 'Sprites', 'Background', 'menu_background.png'),
    'running_background': os.path.join(RESOURCES_PATH, 'Sprites', 'Background', 'BG.png'),
    'mountain1': os.path.join(RESOURCES_PATH, 'Sprites', 'Background', 'mountain1.png'),
    'mountain2': os.path.join(RESOURCES_PATH, 'Sprites', 'Background', 'mountain2.png'),
    'mountain3': os.path.join(RESOURCES_PATH, 'Sprites', 'Background', 'mountain3.png'),
    'mountain4': os.path.join(RESOURCES_PATH, 'Sprites', 'Background', 'mountain4.png'),
    'fog1': os.path.join(RESOURCES_PATH, 'Sprites', 'Background', 'fog1.png'),
    'fog2': os.path.join(RESOURCES_PATH, 'Sprites', 'Background', 'fog2.png'),
    'fog3': os.path.join(RESOURCES_PATH, 'Sprites', 'Background', 'fog3.png')
}
# store the path of images
ROLE_IMAGES = {
    'ninja': {
        'image':
            os.path.join(RESOURCES_PATH, 'Sprites', 'ninja', 'ninja_spritesheet-0.png'),
        'run': [
            os.path.join(RESOURCES_PATH, 'Sprites', 'ninja', 'ninja_spritesheet-1.png'),
            os.path.join(RESOURCES_PATH, 'Sprites', 'ninja', 'ninja_spritesheet-2.png'),
            os.path.join(RESOURCES_PATH, 'Sprites', 'ninja', 'ninja_spritesheet-3.png'),
            os.path.join(RESOURCES_PATH, 'Sprites', 'ninja', 'ninja_spritesheet-5.png'),
            os.path.join(RESOURCES_PATH, 'Sprites', 'ninja', 'ninja_spritesheet-10.png')
            ],
        'jumpup': [
            os.path.join(RESOURCES_PATH, 'Sprites', 'ninja', 'ninja_spritesheet-9.png'),
            os.path.join(RESOURCES_PATH, 'Sprites', 'ninja', 'ninja_spritesheet-11.png'),
            ],
        'jumpdown': [
            os.path.join(RESOURCES_PATH, 'Sprites', 'ninja', 'ninja_spritesheet-11.png'),
            os.path.join(RESOURCES_PATH, 'Sprites', 'ninja', 'ninja_spritesheet-6.png'),
            ],
        'idle': [
            os.path.join(RESOURCES_PATH, 'Sprites', 'ninja', 'ninja_spritesheet-0.png'),
            os.path.join(RESOURCES_PATH, 'Sprites', 'ninja', 'ninja_spritesheet-4.png'),
            os.path.join(RESOURCES_PATH, 'Sprites', 'ninja', 'ninja_spritesheet-8.png'),
        ]
    }
}

MAP_IMAGE = {
    'image': os.path.join(RESOURCES_PATH, 'Sprites', 'map', 'floor.png'),
    'floor': (74, 5, 120, 320)
}

# floor_width_level, floor_height_level, floor_gap_level
FLOOR_LIST = [(6, 0, 1), (2, -1, 2), (3, 0, 1), (2, 1, 1), (2, 2, 0), (2, -1, 0), (2, -2, 0), (2, -4, 4), (1, 0, 3), (1, -1, 4), (1, -2, 3), [5, -3, 2]] * 10

GAME_OVER_IMAGES = {
    'images': [
        os.path.join(RESOURCES_PATH, 'Sprites', 'game_over', 'game_over_0.png'),
        os.path.join(RESOURCES_PATH, 'Sprites', 'game_over', 'game_over_1.png'),
        os.path.join(RESOURCES_PATH, 'Sprites', 'game_over', 'game_over_2.png'),
        os.path.join(RESOURCES_PATH, 'Sprites', 'game_over', 'game_over_3.png'),
        os.path.join(RESOURCES_PATH, 'Sprites', 'game_over', 'game_over_4.png'),
        os.path.join(RESOURCES_PATH, 'Sprites', 'game_over', 'game_over_5.png'),
        os.path.join(RESOURCES_PATH, 'Sprites', 'game_over', 'game_over_6.png'),
    ]
}

SOUNDS_PATH = os.path.join(RESOURCES_PATH, 'Sounds')
SOUNDS = {
    'jump': os.path.join(SOUNDS_PATH, 'jump.wav'),
    'game_over': os.path.join(SOUNDS_PATH, 'gameover.wav')
}
BGM = {
    'play_bgm': os.path.join(SOUNDS_PATH, 'NARUTO Main Theme.mp3'),
    'menu_bgm': os.path.join(SOUNDS_PATH, 'bgm.mp3')
}

INTRODUCTION_IMG = {
    'space1':  os.path.join(RESOURCES_PATH, 'Sprites', 'Introduction', 'space1.png'),
    'arrow2': os.path.join(RESOURCES_PATH, 'Sprites', 'Introduction', 'arrow2.png'),
    'esc2': os.path.join(RESOURCES_PATH, 'Sprites', 'Introduction', 'esc2.png'),
    'text': os.path.join(RESOURCES_PATH, 'Sprites', 'Introduction', 'text.png')
}

FONT_PATH = 'resources/ninja.otf'


JUMP_KEY = pygame.K_SPACE
LEFT_ARROW = pygame.K_LEFT
RIGHT_ARROW = pygame.K_RIGHT
UP_ARROW = pygame.K_UP
DOWN_ARROW = pygame.K_DOWN
ENTER_KEY = pygame.K_RETURN
MOUSE_CLICKED = pygame.MOUSEBUTTONDOWN