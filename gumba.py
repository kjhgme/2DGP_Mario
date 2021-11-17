from pico2d import *
import game_framework

# Gumba Move Speed
GUMBA_PIXEL_PER_METER = (10.0 / 0.3)
GUMBA_SPEED_KMPH = 10.0
GUMBA_SPEED_MPM = (GUMBA_SPEED_KMPH * 1000.0 / 60.0)
GUMBA_SPEED_MPS = (GUMBA_SPEED_MPM / 60.0)
GUMBA_SPEED_PPS = (GUMBA_SPEED_MPS * GUMBA_PIXEL_PER_METER)

# Gumba Action Speed
TIME_PER_ACTION = 5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Gumba:
    def __init__(self):
        self.image = load_image('image/monster/gumba/gumbaL/0.png')
        self.frame = 0
        self.direction = 0
        self.x = 500
        self.y = 80

    def update(self):
        self.frame = (self.frame + GUMBA_SPEED_PPS * game_framework.frame_time) % 5

        if self.direction <= 0:
            self.x += game_framework.frame_time * GUMBA_SPEED_PPS
            self.image = load_image('image/monster/gumba/gumbaR/' + str(int(self.frame)) + '.png')
        elif self.direction >= 1:
            self.x -= game_framework.frame_time * GUMBA_SPEED_PPS
            self.image = load_image('image/monster/gumba/gumbaL/' + str(int(self.frame)) + '.png')

        if self.x >= 800 - 25:
            self.direction += 1
        elif self.x <= 25:
            self.direction -= 1

    def draw(self):
        self.image.clip_draw(0, 0, 50, 60, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        #return self.x-32, self.y-32, self.x+32, self.y+32
        return self.x-10, self.y-10, self.x+10, self.y+10