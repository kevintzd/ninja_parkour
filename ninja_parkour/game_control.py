import pygame
import configurations as cfg
import loadResource

class control:
    def __init__(self):
        self.done = False
        self.screen, self.clock = self.init_game()
        # load all the resources in this game
        self.sources = loadResource.load_resources()
        self.scene = None
        self.scene_dict = {}
        self.scene_name = None
        self.current_time = 0.0


    def init_game(self):
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(size=(cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
        pygame.display.set_caption(cfg.CAPTION)
        return screen, clock

    # read the scene dict and initialize the first game scene
    def init_scene(self, scnen_dic, start_scene):
        self.scene_dict = scnen_dic
        self.scene_name = start_scene
        self.scene = self.scene_dict[self.scene_name]
        # isplay represent whether play the background music
        isplay = self.scene.isplay
        cuurent_time = self.scene.current_time
        self.scene.start(self.sources, cuurent_time, isplay)

    def update_scene(self):
        if self.scene:
            # if current scene is finished then go to next scene
            if self.scene.done:
                self.flip_scene()
            # keep updating current scene until self.done == true
            self.scene.update(self.screen, self.event)

    def flip_scene(self):
        record_time = self.scene.current_time
        isplay = self.scene.isplay  # isplay means whether to play bgm
        # change the name of scene into next scene
        previous, self.scene_name = self.scene_name, self.scene.next_scene
        # reset resource before continue the next round
        if previous == 'game_over':
            self.sources = loadResource.load_resources()
        self.scene = self.scene_dict[self.scene_name]
        # prepare the next scene, passing resources to the next scene
        self.scene.start(self.sources, record_time, isplay)

    # detect keyboard and mouse event and store the event in self.even dictionary
    def event_loop(self):
        self.init_event()
        # detect whether a  key constantly been pressed
        key_list = pygame.key.get_pressed()
        # prevent press left and right at the same time
        if key_list[pygame.K_RIGHT] and not key_list[pygame.K_LEFT]:
            self.event['key_press'][pygame.K_RIGHT] = True
        if key_list[pygame.K_LEFT] and not key_list[pygame.K_RIGHT]:
            self.event['key_press'][pygame.K_LEFT] = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.done = True
                # press p  can skip running scene to game over scene
                elif event.key == pygame.K_SPACE \
                        or event.key == pygame.K_p \
                        or event.key == pygame.K_UP \
                        or event.key == pygame.K_DOWN \
                        or event.key == pygame.K_RETURN:
                    self.event['key_press'][event.key] = True
            # release a key change the corresponding value in the dict into True means this key is not pressed
            elif event.type == pygame.KEYUP:
                self.event['key_up'][event.key] = True
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                self.event['mouse_click'] = pygame.mouse.get_pressed()



    def init_event(self):
        self.event = {
            'key_press': {},
            'key_up': {},
            'mouse_click': (0, 0, 0),
        }

    def main(self):
        while not self.done:
            self.event_loop()
            self.update_scene()
            pygame.display.update()
            self.clock.tick(cfg.FPS)
        print('game exit')
