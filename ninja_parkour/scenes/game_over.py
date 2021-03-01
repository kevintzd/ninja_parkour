import pygame
from scenes import scene
import configurations as cfg
import loadResource


class game_overscene(scene.scenes):
    def __init__(self):
        scene.scenes.__init__(self)
        self.next_scene = 'startmenu'
        self.buttons_locations = {}
        self.state = 'none'
        self.next_scene = 'none'
        self.current_time = 0.0
        self.isplay = True

    def start(self, source, record_time, *args):
        self.done = False
        self.record_time = "{:.1f} s".format(record_time)
        self.images = loadResource.load_game_over_images()
        self.image =  self.images['images'][0]
        self.rect = self.image.get_rect()
        self.rect.left = (cfg.SCREEN_WIDTH - self.rect.width)/2
        self.rect.top = cfg.SCREEN_HEIGHT/8
        self.animation_speed = 2
        self.animation_index = 0
        self.animation_index_change_count = 0
        self.sounds, self.bgm = loadResource.load_sounds()
        self.is_sounds_played = False
        self.timer = pygame.time.Clock()
        self.time_delay = 0


    def update(self, screen, event):
        self.press(event)
        self.timer.tick()
        self.time_delay += self.timer.get_time()
        screen.fill('black')
        self.draw_text("Game Over", screen, 80, cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT * 3.3 / 8, 'white', False)
        self.draw_text(self.record_time, screen, 60, cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT * 5 / 8, 'white', False)
        if self.state == 'Back To Start Menu':
            self.draw_text('Back To Start Menu', screen, 40, cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT * 7 / 8, 'red', True)
        else:
            self.draw_text('Back To Start Menu', screen, 30, cfg.SCREEN_WIDTH / 2, cfg.SCREEN_HEIGHT * 7 / 8, 'white', True)
        if not self.is_sounds_played:
            self.sounds['game_over'].play()
            self.is_sounds_played = True

        # play animation
        if self.time_delay >= 500.0:
            screen.blit(self.image, self.rect)
            self.animation_index_change_count += 1
            if self.animation_index_change_count % self.animation_speed == 0:
                if self.animation_index >= len(self.images['images'])-1:
                    self.animation_index = len(self.images['images'])-1
                else:
                    self.animation_index += 1

                self.image = self.images['images'][self.animation_index]

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
                            self.current_time = 0.0
                            self.done = True
            else:
                self.mouse_cursor()
            if event['mouse_click'][0] and self.state != 'none':
                if self.state == 'Back To Start Menu':
                    self.current_time = 0.0
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
        self.state = 'Back To Start Menu'
        self.next_scene = "starting"

    def mouse_cursor(self):
        mouse_pos = pygame.mouse.get_pos()
        for button, location in self.buttons_locations.items():
            if location[0] <= mouse_pos[0] <= location[1] and location[2] <= mouse_pos[1] <= location[3]:
                    self.state = button
                    self.next_scene = "starting"
            else:
                self.state = 'none'
                self.next_scene = "none"


