import pygame
import configurations as cfg
import map
import itertools

class player:
    def __init__(self, images, position, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images['idle'][0]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        # initialise the direction
        self.direction = 'right'

        self.rect.left, self.rect.top = position
        self.rect.top -= 1
        self.isdead = False
        self.state = 'idle'

        self.init_speed()

        self.a_speed = 10 * cfg.FPS / 1000
        self.init_height = cfg.INIT_HEIGHT

        # switch images
        self.role_index = 0
        # use itertools to loop the index
        self.role_idle_index_cycle = itertools.cycle(
            [i for i in range(len(self.images['idle']))])
        self.role_jumpup_index_cycle = itertools.cycle(
            [i for i in range(len(self.images['jumpup']))])
        self.role_jumpdown_index_cycle = itertools.cycle(
            [i for i in range(len(self.images['jumpdown']))])
        self.role_run_index_cycle = itertools.cycle(
            [i for i in range(len(self.images['run']))])
        # set timer to control the animation play speed
        self.role_index_change_count = 0
        self.role_idle_speed = 7
        self.role_jumpup_speed = 10
        self.role_jumpdown_speed = 10
        self.role_run_speed = 3
        self.double_jump = False
        self.running_speed = 5

        self.current_floor = None
    def init_speed(self):
        self.jumpup_speed = 12
        self.jumpdown_speed = 0

    def update(self):
        self.set_base_height()
        if self.state == 'idle':
            self.idle()
        if self.state == 'run':
            self.run()
        if self.state == 'jumpup' or self.state == 'jumpdown':
            self.jump_state()
        if self.isdead:
            return True

    def set_base_height(self):
        # if there is a floor under ninja then set the base height to the top coordinate of the floor
        if self.current_floor:
            self.init_height = self.current_floor.rect.top
        # otherwise set base height to the bottom of screen
        else:
            self.init_height = cfg.SCREEN_HEIGHT
            if self.state != 'jumpup' and self.state != 'jumpdown':
                # self.image = self.jump_image
                self.change_rect_mask()
                self.state = 'jumpdown'
    # flip all the image once change direction
    def change_direction(self, direction):
        if direction == 'right' and self.direction == 'left':
            for i in range(len(self.images['run'])):
                self.images['run'][i] = pygame.transform.flip(self.images['run'][i], True, False)
            for i in range(len(self.images['idle'])):
                self.images['idle'][i] = pygame.transform.flip(self.images['idle'][i], True, False)
            self.direction = 'right'
            for i in range(len(self.images['jumpup'])):
                self.images['jumpup'][i] = pygame.transform.flip(self.images['jumpup'][i], True, False)
            for i in range(len(self.images['jumpdown'])):
                self.images['jumpdown'][i] = pygame.transform.flip(self.images['jumpdown'][i], True, False)
            self.direction = 'right'
        if direction == 'left' and self.direction == 'right':
            for i in range(len(self.images['run'])):
                self.images['run'][i] = pygame.transform.flip(self.images['run'][i], True, False)
            for i in range(len(self.images['idle'])):
                self.images['idle'][i] = pygame.transform.flip(self.images['idle'][i], True, False)
            for i in range(len(self.images['jumpup'])):
                self.images['jumpup'][i] = pygame.transform.flip(self.images['jumpup'][i], True, False)
            for i in range(len(self.images['jumpdown'])):
                self.images['jumpdown'][i] = pygame.transform.flip(self.images['jumpdown'][i], True, False)
            self.direction = 'left'

    def move(self, direction):
        # prevent player moving out of the window
        if self.rect.left - self.running_speed >= 0 and direction == 'left':
            self.rect.left -= self.running_speed
        if self.rect.left + self.running_speed <= cfg.SCREEN_WIDTH - self.rect.width and direction == 'right':
            self.rect.left += self.running_speed

    def idle(self):
        self.role_index_change_count += 1
        # prevent animation too fast
        if self.role_index_change_count % self.role_idle_speed == 0:
            # update index for the image about to display
            self.role_index = next(self.role_idle_index_cycle)
            # update image
            self.image = self.images['idle'][self.role_index]
            self.change_rect_mask()
            self.rect.bottom = self.init_height - 1
            self.role_index_change_count = 0

    def run(self, direction):
        if self.state != 'jumpup' and self.state != 'jumpdown':
            # check if image flipping needed
            self.change_direction(direction)
            self.move(direction)
            self.role_index_change_count += 1
            if self.role_index_change_count % self.role_run_speed == 0:
                self.role_index = next(self.role_run_index_cycle)
                self.image = self.images['run'][self.role_index]
                self.change_rect_mask()
                self.role_index_change_count = 0

    def jump(self, real_jump, direction):
        self.move(direction)
        if real_jump:
            # player can only jump when it is on the floor
            if self.state != 'jumpup' and self.state != 'jumpdown':
                self.state = 'jumpup'
                self.is_jumpup = True
            # or in the sky but can do double jump
            elif not self.double_jump:
                self.jumpup_speed = 0
                self.jumpdown_speed = 0
                self.double_jump = True
                self.state = 'jumpup' # double jump
                self.jumpup_speed = max(self.jumpup_speed, 15)
        else:
            # change direction during jumping
            self.change_direction(direction)

    def jump_state(self):
        if self.state == 'jumpup':
            self.jumpup_state()
        if self.state == 'jumpdown':
            self.jumpdown_state()

    def jumpup_state(self):
        # up speed decay
        self.jumpup_speed -= self.a_speed
        self.rect.top -= self.jumpup_speed
        # animation
        self.role_index_change_count += 1
        if self.role_index_change_count % self.role_jumpup_speed == 0:
            self.role_index = next(self.role_jumpup_index_cycle)
            # only play animation once
            if self.role_index >= len(self.images['jumpup']):
                self.role_index = len(self.images['jumpup'])
            else:
                self.role_index = next(self.role_jumpup_index_cycle)
            self.image = self.images['jumpup'][self.role_index]
            self.change_rect_mask()
            self.role_index_change_count = 0
        # change state to jumpdown if up speed equals to 0
        if self.jumpup_speed <= 0:
            self.init_speed()
            self.state = 'jumpdown'

    def jumpdown_state(self):
        # animation
        self.role_index_change_count += 1
        if self.role_index_change_count % self.role_jumpdown_speed == 0:
            self.role_index = next(self.role_jumpdown_index_cycle)
            # only play animation once
            if self.role_index >= len(self.images['jumpdown']):
                self.role_index = len(self.images['jumpdown'])
            else:
                self.role_index = next(self.role_jumpdown_index_cycle)
            self.image = self.images['jumpdown'][self.role_index]
            self.change_rect_mask()
            self.role_index_change_count = 0

        # down speed decay
        self.jumpdown_speed += self.a_speed
        self.rect.bottom += self.jumpdown_speed
        # let player drop to base height
        if self.rect.bottom >= self.init_height:
            self.rect.bottom = self.init_height
            # finish the game if player touch the bottom of the screen
            if self.init_height == cfg.SCREEN_HEIGHT:
                self.isdead = True
            # self.is_jumpdown = False
            self.double_jump = False
            self.state = 'idle'
            self.init_speed()

    def change_rect_mask(self):
        left, top = self.rect.left, self.rect.top
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top = left, top


    def show_character(self, screen):
        screen.blit(self.image, self.rect)

