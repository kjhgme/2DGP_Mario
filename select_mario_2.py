from pico2d import *

class Mario:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.image = load_image('image/mario/bigmario/marioR/stand.png')

    def draw(self):
        self.image.clip_draw(0, 0, 70, 90, 400, 300)




mario = Mario()
open_canvas()
mario.draw()
