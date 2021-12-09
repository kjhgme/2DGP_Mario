# Gumba
# (필요사항) 굼바가 벽에 부딪힐 때 이동방향 변경. 벽이 없을 때 낙하.
import gumba
from pico2d import *

import collision
import game_framework
import background
import game_world
import server
import game_over
from stage4_ground import Ground
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

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
    def __init__(self, x=0):
        self.image = load_image('image/monster/gumba/gumbaL/0.png')
        self.frame = 0
        self.dir = 0
        self.x = x * GUMBA_PIXEL_PER_METER
        self.y = 85

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y, 'dir': self.dir}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def update(self):
        self.frame = (self.frame + GUMBA_SPEED_PPS * game_framework.frame_time) % 5

        if self.dir <= 0:
            self.x += game_framework.frame_time * GUMBA_SPEED_PPS
            self.image = load_image('image/monster/gumba/gumbaR/' + str(int(self.frame)) + '.png')
        elif self.dir >= 1:
            self.x -= game_framework.frame_time * GUMBA_SPEED_PPS
            self.image = load_image('image/monster/gumba/gumbaL/' + str(int(self.frame)) + '.png')

        if self.x >= 800 - 25:
            self.dir += 1
        elif self.x <= 25:
            self.dir -= 1

        if self.x > 532:
            self.y -= 200 * game_framework.frame_time

        if collision.collide_foot_and_head(server.mario, self):
            self.image = load_image('image/monster/gumba/dead.png')
            game_world.remove_object(self)

        if collision.collide(self, server.mario):
            if server.mario.mode == 0:
                if server.mario.time == 0:
                    game_framework.change_state(game_over)
            elif server.mario.mode == 1:
                server.mario.mode = 0
                server.mario.timer()
            elif server.mario.mode == 2:
                server.mario.mode = 1
                server.mario.timer()





    def draw(self):
        self.image.clip_draw(0, 0, 40, 40, self.x, self.y)

    def get_bb(self):
        return self.x-20, self.y-20, self.x+20, self.y+20

    def gumba_head(self):
        return self.x-20, self.y+20, self.x+20, self.y+20