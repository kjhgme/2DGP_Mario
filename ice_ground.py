from pico2d import *

class IceGround:
    def __init__(self):
        #self.image = load_image('image/Tilesets/Pa1_1-1_1.png')
        self.image = load_image('image/Tilesets/Pa1_1-13_2.png')
        self.x, self.y = 32*2, 32

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 448, 64*4, 64, self.x, self.y)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-(64*2), self.y-32, self.x+(64*2), self.y+32
