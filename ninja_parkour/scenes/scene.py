import pygame
from abc import abstractmethod
class scenes():
    def __init__(self):
        self.done = False
        self.next_scene = None
        # self.next_loading_time = 0
        self.bgm = None
        self.bg_image = None
        self.key_press = {}


    @abstractmethod
    def start(self, source):
        '''abstract method'''

    # def cleanup(self):
    #     self.done = False
    #     return self.persist
    #
    @abstractmethod
    def update(self, screen, event):
        '''abstract method'''
    #
    @abstractmethod
    def set_sources(self, sources):
        '''abstract method'''