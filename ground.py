from pico2d import *

class Ground:
    def __init__(self):
        #self.image = load_image('image/Tilesets/Pa1_1-1_1.png')
        self.image = load_image('image/ground.png')
        #self.x, self.y = 32, 32

    def update(self):
        pass

    def draw(self):
        #self.image.clip_draw(1280, 0, 64, 64, self.x, self.y)
        self.image.draw(400, 30)
        self.image.draw(1588, 73)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        #return self.x-32, self.y-32, self.x+32, self.y+32
        return 0, 0, 1588, 73