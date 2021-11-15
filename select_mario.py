from pico2d import *
import game_framework

class SelectMario:
    def __init__(self):
        self.image = load_image('image/mario/bigmario/marioR/stand.png')
        self.x = 400
        self.y = 300
        self.selectX = 0
        self.selectY = 0
        self.frame = 0

    def update(self):
        self.image = load_image('image/mario/bigmario/marioR/stand.png')
        if self.selectX == 1 and self.x < 600:
            self.x += 1
            self.frame = (self.frame + 1) % 22
            self.image = load_image('image/mario/bigmario/marioR/' + str(self.frame) + '.png')
        elif self.selectX == 0:
            if self.x > 400:
                self.x -= 1
                self.frame = (self.frame + 1) % 22
                self.image = load_image('image/mario/bigmario/marioL/' + str(self.frame) + '.png')
            elif self.x < 400:
                self.x += 1
                self.frame = (self.frame + 1) % 22
                self.image = load_image('image/mario/bigmario/marioR/' + str(self.frame) + '.png')
        elif self.selectX == -1 and self.x > 200:
            self.x -= 1
            self.frame = (self.frame + 1) % 22
            self.image = load_image('image/mario/bigmario/marioL/' + str(self.frame) + '.png')
        if self.selectY == 1 and self.y < 450:
            self.y += 1
            self.frame = (self.frame + 1) % 22
            self.image = load_image('image/mario/bigmario/marioR/' + str(self.frame) + '.png')
        elif self.selectY == 0:
            if self.y > 300:
                self.y -= 1
                self.frame = (self.frame + 1) % 22
                self.image = load_image('image/mario/bigmario/marioR/' + str(self.frame) + '.png')
            elif self.y < 300:
                self.y += 1
                self.frame = (self.frame + 1) % 22
                self.image = load_image('image/mario/bigmario/marioR/' + str(self.frame) + '.png')
        elif self.selectY == -1 and self.y > 150:
            self.y -= 1
            self.frame = (self.frame + 1) % 22
            self.image = load_image('image/mario/bigmario/marioR/' + str(self.frame) + '.png')


    def draw(self):
        self.image.clip_draw(0, 0, 70, 90, self.x, self.y)

    def get_bb(self):
        pass

    def hadle_event(self, event):
        pass
