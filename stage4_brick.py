# stage4용 test tile
from pico2d import *
import collision
import server
import game_world

class Brick:
    def __init__(self, x=0, y=0):
        self.image = load_image('image/Animated Common Tiles.png')
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
            server.mario.Touching = 0

        if collision.collide_foot_and_brick(server.mario, self):
            server.mario.Touching = 0

        if collision.collide_head_and_brick(server.mario, self) and (server.mario.mode == 1 or server.mario.mode == 2):
            game_world.remove_object(self)
            server.mario.Touching = 0
        elif collision.collide_head_and_brick(server.mario, self) and server.mario.mode == 0:
            server.mario.Touching = 0

    def draw(self):
        self.image.clip_draw(320+2, 2048-64+2, 60, 60, self.x, self.y)


    def get_bb(self):
        return self.x-32, self.y-32, self.x+32, self.y+32
