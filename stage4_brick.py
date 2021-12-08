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
            pass

        if collision.collide_foot_and_brick(self, server.mario):
            server.mario.Touching = 0
            server.mario.JumpPoint = server.mario.y

        if collision.collide(self, server.mario) and server.mario.mode == 1:
            game_world.remove_object(self)

    def draw(self):
        self.image.clip_draw(320, 2048-64, 64, 64, self.x, self.y)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-32, self.y-32, self.x+32, self.y+32
