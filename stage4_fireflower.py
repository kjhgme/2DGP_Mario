# stage4용 test tile
from pico2d import *
import collision
import server
import game_world

class FireFlower:
    def __init__(self, x=0, y=0):
        self.image = load_image('image/fireflower.png')
        self.x, self.y = x, y
        self.frame = 0

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def update(self):
        if collision.collide(self, server.mario):
            game_world.remove_object(self)
            server.mario.mode = 2

    def draw(self):
        self.image.clip_draw(0, 0, 64, 64, self.x, self.y)


    def get_bb(self):
        return self.x-32, self.y-32, self.x+32, self.y+32
