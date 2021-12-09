# stage4용 test tile
from pico2d import *
import collision
import server
import game_world
from stage4_mushroom import Mushroom
from stage4_fireflower import FireFlower

class QBrick:
    def __init__(self, name='NONAME', x=0, y=0, num=0):
        self.image = load_image('image/Animated Common Tiles.png')
        self.name = name
        self.x, self.y = x, y
        self.num = num
        self.imagePartX = 320
        self.imagePartY = 1024-64
        self.m, self.f = 0, 0

    def __getstate__(self):
        state = {'name': self.name, 'x': self.x, 'y': self.y, 'num': self.num}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def update(self):
        if self.m == 1:
            server.mushrooms = Mushroom(x=self.x, y=(self.y+64))
            game_world.add_object(server.mushrooms, 1)

        if self.f == 1:
            server.fireflowers = FireFlower(x=self.x, y=(self.y+64))
            game_world.add_object(server.fireflowers, 1)

        if collision.collide(self, server.mario):
            server.mario.Touching = 0

        if collision.collide_foot_and_brick(server.mario, self):
            server.mario.Touching = 0

        if collision.collide_head_and_brick(server.mario, self):
            self.imagePartX = 0
            self.imagePartY = 2048-(64*4)

            if self.name == "mushroom":
                self.m += 1
            elif self.name == "fireflower":
                self.f += 1
                pass

    def draw(self):
        self.image.clip_draw(self.imagePartX+2, self.imagePartY+2, 60, 60, self.x, self.y)


    def get_bb(self):
        return self.x-32, self.y-32, self.x+32, self.y+32
