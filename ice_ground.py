# stage3용 ice tile
from pico2d import *
import collision
import server

n = 4
class IceGround:
    def __init__(self):
        global n
        self.image = load_image('image/Tilesets/Pa1_1-13_2.png')
        self.x, self.y = 32*n, 32
        n += 8

    def update(self):
        if collision.collide(self, server.mario):
            server.mario.stop_falling()

    def draw(self):
        self.image.clip_draw(0, 448, 64*4, 64, self.x, self.y)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-(64*2), self.y-32, self.x+(64*2), self.y+32
