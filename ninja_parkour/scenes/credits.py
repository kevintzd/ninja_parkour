import pygame
from scenes import scene
import configurations as cfg

class credits_menu(scene.scenes):
    def __init__(self):
        scene.scenes.__init__(self)
        self.next_scene = "starting"
        self.state = 'none'
        self.buttons_locations = {}
        self.current_time = 0.0
        self.isplay = False

    def start(self, sources, *args):
        self.state = 'none'
        self.done = False
        self.sources = sources
        self.background_image = self.sources['background']['menu_background']
        self.bg_rect = self.background_image.get_rect()
        self.bg_rect.left, self.bg_rect.top = (0, 0)

    def update(self, screen, event):
        self.press(event)
        if not self.done:
            screen.fill('grey')
            screen.blit(self.background_image, self.bg_rect)
            # self.game.check_events()
            # self.check_input()
            self.draw_text("Credits", screen, 80, cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT * 1 / 8, 'white', False)
            self.draw_text("Ioannis Gkountelas", screen, 40, cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT * 3 / 8, 'white', False)
            self.draw_text("Wendy Martinez", screen, 40, cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT * 4 / 8, 'white', False)
            self.draw_text("Zhida Tian", screen, 40, cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT * 5 / 8, 'white', False)
            if self.state == 'Back':
                self.draw_text("Back", screen, 40, cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT * 7 / 8, 'red', True)
            else:
                self.draw_text("Back", screen, 30, cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT * 7 / 8, 'white', True)

    def press(self, event):
        key_list = {
            cfg.UP_ARROW: {
                'func': self.move_cursor,
            },
            cfg.DOWN_ARROW: {
                'func': self.move_cursor,
            },
            cfg.ENTER_KEY: {
                'func': 'Go back to start menu'
            },
            cfg.MOUSE_CLICKED: {
                'func': 'Go back to start menu'
            }
        }
        for key, values in key_list.items():
            # print(self.key_press)
            if pygame.mouse.get_rel() == (0, 0):
                if event['key_press'].get(key):
                    self.key_press[key] = True
                    if key == cfg.UP_ARROW:
                        self.UP_KEY = True
                        values['func']()
                    if key == cfg.DOWN_ARROW:
                        self.DOWN_KEY = True
                        values['func']()
                    if key == cfg.ENTER_KEY:
                        self.key_press[key] = False
                        self.key_press.pop(key)
                        if self.state != 'none':
                            self.done = True
            else:
                self.mouse_cursor()
            if event['mouse_click'][0] and self.state != 'none':
                if self.state == 'Back':
                    self.done = True

            if event['key_up'].get(key):
                self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
                self.key_press[key] = False
                self.key_press.pop(key)

    def draw_text(self, text, screen, size, x, y, color, isbutton):
        self.font = pygame.font.Font(cfg.FONT_PATH, size)
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        if isbutton:
            self.buttons_locations[text] = [text_rect.left, text_rect.right, text_rect.top, text_rect.bottom]
        screen.blit(text_surface, text_rect)

    def move_cursor(self):
        # if self.state == 'none':
        self.state = 'Back'
        self.next_scene = "starting"

    def mouse_cursor(self):
        mouse_pos = pygame.mouse.get_pos()
        for button, location in self.buttons_locations.items():
            if location[0] <= mouse_pos[0] <= location[1] and location[2] <= mouse_pos[1] <= location[3]:
                # if button == 'Back':
                    self.state = button
                    self.next_scene = "starting"
            else:
                self.state = 'none'
                self.next_scene = "none"




