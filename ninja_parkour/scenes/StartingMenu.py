import pygame
from scenes import scene
import configurations as cfg

class startingmenu(scene.scenes):
    def __init__(self):
        scene.scenes.__init__(self)
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.is_bgm_played = False
        self.buttons_locations = {}
        self.current_time = 0.0
        self.isplay = True

    def start(self, sources, current_time, isplay, *args):
        self.done = False
        # prevent time information from last round of game pass into new round
        self.current_time = 0.0
        # state control which button is selected and the information about next scene
        self.state = 'none'
        self.next_scene = "none"
        self.sources = sources
        self.background_image = self.sources['background']['background']
        self.bg_rect = self.background_image.get_rect()
        self.bg_rect.left, self.bg_rect.top = (0, 0)
        self.bgm = self.sources['bgm']['menu_bgm']
        if isplay:
            self.bgm.play(-1)

    def press(self, event):
        # store different respond depends one the key event
        key_list = {
            cfg.UP_ARROW: {
                'func': self.move_cursor,
            },
            cfg.DOWN_ARROW: {
                'func': self.move_cursor,
            },
            cfg.ENTER_KEY: {
                'func': 'Go to next scene'
            },
            cfg.MOUSE_CLICKED: {
                'func': 'Go to next scene'
            }
        }

        for key, values in key_list.items():
            # use keyboard control the button selection when mouse is not moving
            if pygame.mouse.get_rel() == (0, 0):
                if event['key_press'].get(key):
                    self.key_press[key] = True
                    if key == cfg.UP_ARROW:
                        self.UP_KEY = True
                        values['func']()
                    if key == cfg.DOWN_ARROW:
                        self.DOWN_KEY = True
                        values['func']()
                    # go to next scene when press enter
                    if key == cfg.ENTER_KEY:
                        if not self.state == 'none':
                            if self.state == 'Start Game':
                                self.bgm.stop()
                            self.done = True
            else:
                self.mouse_cursor()

            # go to next scene when mouse selects a button and click
            if event['mouse_click'][0] and self.state != 'none':
                if self.state == 'Start Game':
                    self.bgm.stop()
                self.done = True

            # reset all the corresponding flags
            if event['key_up'].get(key):
                self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
                self.key_press[key] = False
                self.key_press.pop(key)

    def update(self, screen, event):
        self.press(event)
        if not self.done:
            screen.fill('grey')
            screen.blit(self.background_image, self.bg_rect)

            # draw the title and button
            self.draw_text('Ninja Parkour', screen, 100, cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT / 2 - 20, 'white', False)
            # turn red when selected
            if not self.state == 'Start Game':
                self.draw_text("Start Game", screen, 40, cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT * 5 / 8, 'white', True)
            else:
                self.draw_text("Start Game", screen, 50, cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT * 5 / 8, 'red', True)

            if not self.state == 'Introduction':
                self.draw_text("Introduction", screen, 40, cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT * 6 / 8, 'white',True)
            else:
                self.draw_text("Introduction", screen, 50, cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT * 6 / 8, 'red', True)

            if not self.state == 'Credits':
                self.draw_text("Credits", screen, 40, cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT * 7 / 8, 'white', True)
            else:
                self.draw_text("Credits", screen, 50, cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT * 7 / 8, 'red', True)

    # draw text, 'isbutton' represent whether this text is a button
    def draw_text(self, text, screen, size, x, y, color, isbutton):
        self.font = pygame.font.Font(cfg.FONT_PATH, size)
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        if isbutton:
            self.buttons_locations[text] = [text_rect.left, text_rect.right, text_rect.top, text_rect.bottom]
        screen.blit(text_surface, text_rect)

    # choose button by changing state when press up and down key
    def move_cursor(self):
        if self.DOWN_KEY:
            if self.state == 'none':
                self.state = 'Start Game'
                self.next_scene = "runing_scene"
            elif self.state == 'Start Game':
                self.state = 'Introduction'
                self.next_scene = "Introduction"
            elif self.state == 'Introduction':
                self.state = 'Credits'
                self.next_scene = "Credits"
            elif self.state == 'Credits':
                self.state = 'Start Game'
                self.next_scene = "runing_scene"
        elif self.UP_KEY:
            if self.state == 'Start Game':
                self.state = 'Credits'
                self.next_scene = "credits"
            elif self.state == 'Introduction':
                self.state = 'Start Game'
                self.next_scene = "runing_scene"
            elif self.state == 'Credits':
                self.state = 'Introduction'
                self.next_scene = "Introduction"

    # select button when mouse move into buttons' rect
    def mouse_cursor(self):
        mouse_pos = pygame.mouse.get_pos()
        for button, location in self.buttons_locations.items():
            if location[0] <= mouse_pos[0] <= location[1] and location[2] <= mouse_pos[1] <= location[3]:
                if button != 'Ninja Parkour':
                    self.state = button
                    if self.state == 'Credits':
                        self.next_scene = "Credits"
                    elif self.state == 'Start Game':
                        self.next_scene = "runing_scene"
                    elif self.state == 'Introduction':
                        self.next_scene = "Introduction"
                    break
            else:
                self.state = 'none'
                self.next_scene = 'none'





