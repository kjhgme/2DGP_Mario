# Mushroom
from pico2d import *

import collision
import game_framework
import server
import game_world
import stage4

# Mushroom Move Speed
MUSHROOM_PIXEL_PER_METER = (10.0 / 0.3)
MUSHROOM_SPEED_KMPH = 10.0
MUSHROOM_SPEED_MPM = (MUSHROOM_SPEED_KMPH * 1000.0 / 60.0)
MUSHROOM_SPEED_MPS = (MUSHROOM_SPEED_MPM / 60.0)
MUSHROOM_SPEED_PPS = (MUSHROOM_SPEED_MPS * MUSHROOM_PIXEL_PER_METER)

# Gumba Action Speed
TIME_PER_ACTION = 5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Mushroom:
    def __init__(self, x=0, y=0):
        self.image = load_image('image/mushroom.png')
        self.frame = 0
        self.dir = 0
        self.fallingspeed = 0
        self.x = x
        self.y = y
        self.Touching = 0

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y, 'dir': self.dir}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def update(self):
        self.frame = (self.frame + MUSHROOM_SPEED_PPS * game_framework.frame_time) % 5


        if self.dir <= 0:
            self.x += game_framework.frame_time * MUSHROOM_SPEED_PPS
        elif self.dir >= 1:
            self.x -= game_framework.frame_time * MUSHROOM_SPEED_PPS

        if self.x >= 800 - 25:
            self.dir += 1
        elif self.x <= 25:
            self.dir -= 1

        if collision.collide(self, server.mario):
            game_world.remove_object(self)
            if server.mario.mode == 2:
                pass
            elif server.mario.mode == 0:
                server.mario.mode = 1


    def draw(self):
        self.image.clip_draw(0, 0, 64, 64, self.x, self.y)

    def get_bb(self):
        return self.x-32, self.y-32, self.x+32, self.y+32
