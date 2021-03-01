import pygame
import configurations as cfg
from copy import deepcopy
import os

def load_player():
    player_images = dict()
    player_dt = deepcopy(cfg.ROLE_IMAGES)
    for name, values in player_dt.items():
        player_images[name] = {}  # {'ninja': }
        img_path = values.pop('image')

        image = pygame.image.load(img_path).convert_alpha()
        for key, value_list in values.items():
            player_images[name][key] = [
                pygame.image.load(value).convert_alpha() for value in value_list
            ]
    for name, values in player_images.items():
        for k, v in values.items():
            player_images[name][k] = [
                pygame.transform.smoothscale(
                    i, (int(i.get_width()/3), int(i.get_height()/3)))
                for i in v
            ]
    return player_images


def load_game_over_images():
    game_over_images = dict()
    game_over_dt = deepcopy(cfg.GAME_OVER_IMAGES)
    for name, values in game_over_dt.items():
        game_over_images[name] = [
                pygame.image.load(value).convert_alpha() for value in values
            ]
    for name, values in game_over_images.items():
        game_over_images[name] = [
            pygame.transform.smoothscale(
                i, (int(i.get_width() / 2), int(i.get_height() / 2)))
            for i in values
        ]
    return game_over_images


def load_sounds():
    sounds = {
        key: pygame.mixer.Sound(value)
        for key, value in cfg.SOUNDS.items()
    }
    for k, v in sounds.items():
        v.set_volume(0.1)
    bgm = {
        key: pygame.mixer.Sound(value)
        for key, value in cfg.BGM.items()
    }
    for k, v in bgm.items():
        v.set_volume(0.1)
    return sounds, bgm

def load_Intro_img():
    dt = deepcopy(cfg.INTRODUCTION_IMG)
    Intro_img = {key: pygame.image.load(value).convert_alpha() for key, value in dt.items()}
    return Intro_img

def load_background():
    dt = deepcopy(cfg.BACKGROUND_IMAGE)
    background = {key: pygame.image.load(value).convert_alpha() for key, value in dt.items()}
    return background

def load_map():
    dt = deepcopy(cfg.MAP_IMAGE)
    map_image = pygame.image.load(dt.get('image'))
    dt.pop('image')
    map = {
        k: map_image.subsurface(pygame.Rect(*v))
        for k, v in dt.items()
    }
    return map

def load_resources():
    player_images = load_player()
    sounds, bgm = load_sounds()
    background = load_background()
    map = load_map()
    intro_img = load_Intro_img()
    return {
        'player': player_images,
        'sounds': sounds,
        'bgm': bgm,
        'background': background,
        'map': map,
        'Intro_img': intro_img
    }
