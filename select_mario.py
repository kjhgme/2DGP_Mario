from pico2d import *
import game_framework

# Select_Mario Run Speed
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Select_Mario Run Speed
TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

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
            self.x += int(game_framework.frame_time * RUN_SPEED_PPS)+1
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 22
            self.image = load_image('image/mario/bigmario/marioR/' + str(int(self.frame)) + '.png')
        elif self.selectX == 0:
            if self.x > 400:
                self.x -= int(game_framework.frame_time * RUN_SPEED_PPS)+1
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 22
                self.image = load_image('image/mario/bigmario/marioL/' + str(int(self.frame)) + '.png')
            elif self.x < 400:
                self.x += int(game_framework.frame_time * RUN_SPEED_PPS)+1
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 22
                self.image = load_image('image/mario/bigmario/marioR/' + str(int(self.frame)) + '.png')
        elif self.selectX == -1 and self.x > 200:
            self.x -= int(game_framework.frame_time * RUN_SPEED_PPS)+1
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 22
            self.image = load_image('image/mario/bigmario/marioL/' + str(int(self.frame)) + '.png')
        if self.selectY == 1 and self.y < 450:
            self.y += int(game_framework.frame_time * RUN_SPEED_PPS)+1
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 22
            self.image = load_image('image/mario/bigmario/marioR/' + str(int(self.frame)) + '.png')
        elif self.selectY == 0:
            if self.y > 300:
                self.y -= int(game_framework.frame_time * RUN_SPEED_PPS)+1
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 22
                self.image = load_image('image/mario/bigmario/marioR/' + str(int(self.frame)) + '.png')
            elif self.y < 300:
                self.y += int(game_framework.frame_time * RUN_SPEED_PPS)+1
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 22
                self.image = load_image('image/mario/bigmario/marioR/' + str(int(self.frame)) + '.png')
        elif self.selectY == -1 and self.y > 150:
            self.y -= int(game_framework.frame_time * RUN_SPEED_PPS)+1
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 22
            self.image = load_image('image/mario/bigmario/marioR/' + str(int(self.frame)) + '.png')


    def draw(self):
        self.image.clip_draw(0, 0, 70, 90, self.x, self.y)

    def get_bb(self):
        pass

    def hadle_event(self, event):
        pass
