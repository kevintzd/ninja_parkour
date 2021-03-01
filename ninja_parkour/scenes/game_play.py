import pygame
from scenes import scene
import configurations as cfg
import character
import map

class game_playscene(scene.scenes):
    def __init__(self):
        scene.scenes.__init__(self)
        self.next_scene = 'game_over'
        self.timer = pygame.time.Clock()
        self.current_time = 0.0
        self.font = pygame.font.Font(cfg.FONT_PATH, 40)
        self.isplay = True


    def start(self, sources, isplay, *args):
        print('game_playscene start')
        self.current_time = 0.0
        self.done = False
        self.bgm = sources['bgm']['play_bgm']
        self.player_name = 'ninja'
        # get all the image resources needed in running scene
        self.player, self.floor_sprites, self.BG, self.mountains, self.fogs = self.init_sprites(
            self.player_name, sources)
        self.sources = sources
        self.mountains_rects = []
        self.fogs_rects = []
        # get the rect of background items
        for i in range(len(self.mountains)):
            self.mountains_rects += [self.mountains[i].get_rect()]
            self.mountains_rects[i].left = i * 30

        for i in range(len(self.fogs)):
            self.fogs_rects += [self.fogs[i].get_rect()]
            self.fogs_rects[i].left = i * 20
        # play background music
        if self.bgm:
            self.bgm.play(-1)
        self.timer.tick()

    def init_sprites(self, role_name, sources):
        role_images = sources['player'][role_name]
        role_pos = [
            cfg.SCREEN_WIDTH * 0.15,
            cfg.INIT_HEIGHT / 2
        ]
        role = character.player(role_images, role_pos)

        floor_first_pos = [0, cfg.INIT_HEIGHT]
        # floor image is a single block use relative variable in configuration file draw different combination of floor
        floor_imgae = sources['map']['floor']
        imgae_width = floor_imgae.get_width()
        floor_sprites = pygame.sprite.Group()
        x = 0
        y = cfg.INIT_HEIGHT
        for width_level, height_level, gap_level in cfg.FLOOR_LIST:
            y = cfg.INIT_HEIGHT + height_level * cfg.FLOOR_GAP_HEIGHT
            # instantiate a floor
            floor = map.Floor(floor_imgae, (x, y), width_level)
            # calculate the gap between two blocks
            x += imgae_width * width_level + gap_level * cfg.FLOOR_GAP_WIDTH
            floor_sprites.add(floor)
        BG = sources['background']['running_background']
        mountains = []
        fogs = []
        mountains += [sources['background']['mountain1']]
        mountains += [sources['background']['mountain2']]
        mountains += [sources['background']['mountain3']]
        mountains += [sources['background']['mountain4']]
        fogs += [sources['background']['fog1']]
        fogs += [sources['background']['fog2']]
        fogs += [sources['background']['fog3']]
        return role, floor_sprites, BG, mountains, fogs

    def press(self, event):
        key_list = {
            cfg.JUMP_KEY: {
                'sound': 'jump',
                'func': self.player.jump,
                'direction': 'none'
            },
            cfg.LEFT_ARROW: {
                'func': self.player.run,
                'direction': 'left',
                'false_jump': self.player.jump
            },
            cfg.RIGHT_ARROW: {
                'func': self.player.run,
                'direction': 'right',
                'false_jump': self.player.jump
            },
            pygame.K_p:{
                'func': self.player.isdead,
            }
        }

        for key, values in key_list.items():
            if event['key_press'].get(key):
                self.key_press[key] = True
                if key == cfg.JUMP_KEY:
                    self.sources['sounds'][values['sound']].play()
                    direction = values['direction']
                    values['func'](True, direction)
                if key == cfg.RIGHT_ARROW or key == cfg.LEFT_ARROW:
                    direction = values['direction']
                    values['false_jump'](False, direction)
                    values['func'](direction)
                if key == cfg.pygame.K_p:
                    self.player.isdead = True

            if event['key_up'].get(key):
                self.key_press[key] = False
                self.key_press.pop(key)


    def update(self, screen, event):
        self.press(event)
        self.player.current_floor = None
        self.timer.tick()
        self.current_time += self.timer.get_time()/1000

        for floor in self.floor_sprites:
            is_del = floor.update()
            # check if there is a floor depends on the location of player
            if floor.rect.left <= (
                    self.player.rect.right - self.player.rect.width /
                    4) and floor.rect.right >= self.player.rect.centerx:
                self.player.current_floor = floor
            # delete the floor block if it's out of screen
            if is_del:
                self.floor_sprites.remove(floor)

        if self.player.update():
            self.bgm.stop()
            self.done = True

        # prevent player go inside the floor from left or right sides
        for floor in self.floor_sprites:
            if pygame.sprite.collide_mask(self.player, floor):
                self.player.rect.right = floor.rect.left

        if not self.done:
            screen.fill('gray')
            # draw background image
            screen.blit(self.BG, self.BG.get_rect())
            # move mountains and fog in different speed
            self.move_mountain_fog(screen)

            self.player.show_character(screen)
            for floor in self.floor_sprites:
                floor.draw(screen)
            # draw the survival time
            surf = self.font.render(("{:.1f}".format(self.current_time)), False, 'Black')
            screen.blit(surf, ((cfg.SCREEN_WIDTH-surf.get_width())/2, 20))


    def move_mountain_fog(self, screen):
        for i in range(len(self.mountains_rects)):
            speed = 0.5 * (i+5)
            self.mountains_rects[i].left -= speed
            if self.mountains_rects[i].right < 0:
                self.mountains_rects[i].left = cfg.SCREEN_WIDTH
            screen.blit(self.mountains[i], self.mountains_rects[i])
        for i in range(len(self.fogs_rects)):
            speed = 0.5 * (i+5)
            self.fogs_rects[i].left -= speed
            if self.fogs_rects[i].right < 0:
                self.fogs_rects[i].left = cfg.SCREEN_WIDTH
            screen.blit(self.fogs[i], self.fogs_rects[i])



