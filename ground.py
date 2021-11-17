from pico2d import *

n = 1
class Ground:
    def __init__(self):
        global n
        self.image = load_image('image/Tilesets/Pa1_1-1_1.png')
        self.x, self.y = 32*n, 32
        n += 2

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(1280, 0, 64, 64, self.x, self.y)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-32, self.y-32, self.x+32, self.y+32