# stage4용 test tile
from pico2d import *
import collision
import server

class Ground:
    def __init__(self, x=0, y=0):
        self.image = load_image('image/Tilesets/Pa1_1-13_2.png')
        self.x, self.y = x, y
        self.bgm = load_music('sound/mario.wav')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()


    def __getstate__(self):
        state = {'x': self.x, 'y': self.y}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def update(self):
        if collision.collide_foot_and_brick(server.mario, self):
            server.mario.Touching = 0
        if collision.collide(server.mario, self):
            server.mario.Touching = 0


    def draw(self):
        self.image.clip_draw(0, 448, 64*4, 64, self.x, self.y)


    def get_bb(self):
        return self.x-(64*2), self.y-32, self.x+(64*2), self.y+32
