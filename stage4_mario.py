# stage4용 마리오
from pico2d import *

import collision
import game_framework
import game_over
import server
import fireball
import game_world

from stage4_brick import Brick

# Mario Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
FALL_SPEED = 200

# Mario Action Speed
TIME_PER_ACTION = 0.15
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# Mario Event
RIGHT_DOWN, RIGHT_UP, LEFT_DOWN, LEFT_UP, UP_DOWN,  SPACE = range(6)
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}

# Mario States
class IdleState:
    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.velocity += RUN_SPEED_PPS
        elif event == UP_DOWN:
            mario.jump += 1
            mario.Touching = 1

        elif event == SPACE and mario.mode == 2:
            mario.fireball()

    def exit(mario, event):
        pass

    def do(mario):
        if mario.mode == 0:
            if mario.dir == 1:
                mario.image = load_image('image/mario/smallmario/marioR/stand.png')
                if mario.jump >= 1:
                    t = mario.i / 100
                    mario.y = (2 * t ** 2 - 3 * t + 1) * mario.JumpPoint + (-4 * t ** 2 + 4 * t) * (mario.JumpPoint+200) + (2 * t ** 2 - t) * mario.JumpPoint
                    mario.image = load_image('image/mario/smallmario/marioR/jump.png')
                    mario.i += 0.5
                    if mario.i >= 100:
                        if mario.Touching == 0:
                            mario.jump = 0
                            mario.i = 0
            elif mario.dir == -1:
                mario.image = load_image('image/mario/smallmario/marioL/stand.png')
                if mario.jump >= 1:
                    t = mario.i / 100
                    mario.y = (2 * t ** 2 - 3 * t + 1) * mario.JumpPoint + (-4 * t ** 2 + 4 * t) * (mario.JumpPoint+200) + (2 * t ** 2 - t) * mario.JumpPoint
                    mario.image = load_image('image/mario/smallmario/marioL/jump.png')
                    mario.i += 0.5
                    if mario.i >= 100:
                        if mario.Touching == 0:
                            mario.jump = 0
                            mario.i = 0
        elif mario.mode == 1:
            if mario.dir == 1:
                mario.image = load_image('image/mario/bigmario/marioR/stand.png')
                if mario.jump >= 1:
                    t = mario.i / 100
                    mario.y = (2 * t ** 2 - 3 * t + 1) * mario.JumpPoint + (-4 * t ** 2 + 4 * t) * (mario.JumpPoint+200) + (2 * t ** 2 - t) * mario.JumpPoint
                    mario.image = load_image('image/mario/bigmario/marioR/jump.png')
                    mario.i += 0.5
                    if mario.i >= 100:
                        if mario.Touching == 0:
                            mario.jump = 0
                            mario.i = 0
            elif mario.dir == -1:
                mario.image = load_image('image/mario/bigmario/marioL/stand.png')
                if mario.jump >= 1:
                    t = mario.i / 100
                    mario.y = (2 * t ** 2 - 3 * t + 1) * mario.JumpPoint + (-4 * t ** 2 + 4 * t) * (mario.JumpPoint+200) + (2 * t ** 2 - t) * mario.JumpPoint
                    mario.image = load_image('image/mario/bigmario/marioL/jump.png')
                    mario.i += 0.5
                    if mario.i >= 100:
                        if mario.Touching == 0:
                            mario.jump = 0
                            mario.i = 0
        elif mario.mode == 2:
            if mario.dir == 1:
                mario.image = load_image('image/mario/bigmario/marioR/stand.png')
                if mario.jump >= 1:
                    t = mario.i / 100
                    mario.y = (2 * t ** 2 - 3 * t + 1) * mario.JumpPoint + (-4 * t ** 2 + 4 * t) * (mario.JumpPoint+200) + (2 * t ** 2 - t) * mario.JumpPoint
                    mario.image = load_image('image/mario/bigmario/marioR/jump.png')
                    mario.i += 0.5
                    if mario.i >= 100:
                        if mario.Touching == 0:
                            mario.jump = 0
                            mario.i = 0
            elif mario.dir == -1:
                mario.image = load_image('image/mario/bigmario/marioL/stand.png')
                if mario.jump >= 1:
                    t = mario.i / 100
                    mario.y = (2 * t ** 2 - 3 * t + 1) * mario.JumpPoint + (-4 * t ** 2 + 4 * t) * (mario.JumpPoint+200) + (2 * t ** 2 - t) * mario.JumpPoint
                    mario.image = load_image('image/mario/bigmario/marioL/jump.png')
                    mario.i += 0.5
                    if mario.i >= 100:
                        if mario.Touching == 0:
                            mario.jump = 0
                            mario.i = 0
        if mario.Touching == 1:
            mario.y -= FALL_SPEED * game_framework.frame_time

    def draw(mario):        # mode 에 따라서 변경필요
        if mario.mode == 0:
            mario.image.clip_draw(0, 0, 50, 80, mario.x, mario.y)
        elif mario.mode == 1:
            mario.image.clip_draw(0, 0, 80, 100, mario.x, mario.y)
        elif mario.mode == 2:
            mario.image.clip_draw(0, 0, 80, 100, mario.x, mario.y)


class RunState:
    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.velocity += RUN_SPEED_PPS
        elif event == UP_DOWN:
            mario.jump += 1
            mario.Touching = 1
        elif event == SPACE and mario.mode == 2:
            mario.fireball()
        mario.dir = clamp(-1, mario.velocity, 1)

    def exit(mario, event):
        if event == SPACE and mario.mode == 1:  # mode 숫자 변경필요
            pass

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 22
        mario.x += mario.velocity * game_framework.frame_time
        mario.x = clamp(25, mario.x, 1600 - 25)
        if mario.mode == 0:
            if mario.dir == 1:
                mario.image = load_image('image/mario/smallmario/marioR/' + str(int(mario.frame)) + '.png')
                if mario.jump >= 1:
                    t = mario.i / 100
                    mario.y = (2 * t ** 2 - 3 * t + 1) * mario.JumpPoint + (-4 * t ** 2 + 4 * t) * (mario.JumpPoint+200) + (2 * t ** 2 - t) * mario.JumpPoint
                    mario.image = load_image('image/mario/smallmario/marioR/jump.png')
                    mario.i += 0.5
                    if mario.i >= 100:
                        if mario.Touching == 0:
                            mario.jump = 0
                            mario.i = 0
            elif mario.dir == -1:
                mario.image = load_image('image/mario/smallmario/marioL/' + str(int(mario.frame)) + '.png')
                if mario.jump >= 1:
                    t = mario.i / 100
                    mario.y = (2 * t ** 2 - 3 * t + 1) * mario.JumpPoint + (-4 * t ** 2 + 4 * t) * (mario.JumpPoint+200) + (2 * t ** 2 - t) * mario.JumpPoint
                    mario.image = load_image('image/mario/smallmario/marioL/jump.png')
                    mario.i += 0.5
                    if mario.i >= 100:
                        if mario.Touching == 0:
                            mario.jump = 0
                            mario.i = 0
        elif mario.mode == 1:
            if mario.dir == 1:
                mario.image = load_image('image/mario/bigmario/marioR/' + str(int(mario.frame)) + '.png')
                if mario.jump >= 1:
                    t = mario.i / 100
                    mario.y = (2 * t ** 2 - 3 * t + 1) * mario.JumpPoint + (-4 * t ** 2 + 4 * t) * (mario.JumpPoint+200) + (2 * t ** 2 - t) * mario.JumpPoint
                    mario.image = load_image('image/mario/bigmario/marioR/jump.png')
                    mario.i += 0.5
                    if mario.i >= 100:
                        if mario.Touching == 0:
                            mario.jump = 0
                            mario.i = 0
            elif mario.dir == -1:
                mario.image = load_image('image/mario/bigmario/marioL/' + str(int(mario.frame)) + '.png')
                if mario.jump >= 1:
                    t = mario.i / 100
                    mario.y = (2 * t ** 2 - 3 * t + 1) * mario.JumpPoint + (-4 * t ** 2 + 4 * t) * (mario.JumpPoint+200) + (2 * t ** 2 - t) * mario.JumpPoint
                    mario.image = load_image('image/mario/bigmario/marioL/jump.png')
                    mario.i += 0.5
                    if mario.i >= 100:
                        if mario.Touching == 0:
                            mario.jump = 0
                            mario.i = 0
        elif mario.mode == 2:
            if mario.dir == 1:
                mario.image = load_image('image/mario/bigmario/marioR/' + str(int(mario.frame)) + '.png')
                if mario.jump >= 1:
                    t = mario.i / 100
                    mario.y = (2 * t ** 2 - 3 * t + 1) * mario.JumpPoint + (-4 * t ** 2 + 4 * t) * (mario.JumpPoint+200) + (2 * t ** 2 - t) * mario.JumpPoint
                    mario.image = load_image('image/mario/bigmario/marioR/jump.png')
                    mario.i += 0.5
                    if mario.i >= 100:
                        if mario.Touching == 0:
                            mario.jump = 0
                            mario.i = 0
            elif mario.dir == -1:
                mario.image = load_image('image/mario/bigmario/marioL/' + str(int(mario.frame)) + '.png')
                if mario.jump >= 1:
                    t = mario.i / 100
                    mario.y = (2 * t ** 2 - 3 * t + 1) * mario.JumpPoint + (-4 * t ** 2 + 4 * t) * (mario.JumpPoint+200) + (2 * t ** 2 - t) * mario.JumpPoint
                    mario.image = load_image('image/mario/bigmario/marioL/jump.png')
                    mario.i += 0.5
                    if mario.i >= 100:
                        if mario.Touching == 0:
                            mario.jump = 0
                            mario.i = 0

        if mario.Touching == 1:
            mario.y -= FALL_SPEED * game_framework.frame_time

    def draw(mario):
        if mario.mode == 0:
            mario.image.clip_draw(0, 0, 50, 80, mario.x, mario.y)
        elif mario.mode == 1:
            mario.image.clip_draw(0, 0, 80, 100, mario.x, mario.y)
        elif mario.mode == 2:
            mario.image.clip_draw(0, 0, 80, 100, mario.x, mario.y)

next_state_table = {
    IdleState: {RIGHT_DOWN: RunState, RIGHT_UP: IdleState, LEFT_DOWN: RunState, LEFT_UP: IdleState, UP_DOWN: IdleState, SPACE: IdleState},
    RunState: {RIGHT_DOWN: RunState, RIGHT_UP: IdleState, LEFT_DOWN: RunState, LEFT_UP: IdleState, UP_DOWN: RunState, SPACE: RunState}
}

class Mario:
    def __init__(self):
        self.mode = 0       # mode 0 = small, 1 = big, 2 = flower
        self.x, self.y = 20, 104
        self.image = load_image('image/mario/smallmario/marioR/stand.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.jump = 0
        self.Touching = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.time = 0
        self.JumpPoint = 100
        self.i = 0


    def get_bb(self):
        if self.mode == 0:
            return self.x - 20, self.y - 20, self.x + 20, self.y + 20
        elif self.mode == 1:
            return self.x - 30, self.y - 20, self.x + 30, self.y + 20
        elif self.mode == 2:
            return self.x - 30, self.y - 20, self.x + 30, self.y + 20

    def mario_foot(self):
        if self.mode == 0:
            return self.x - 15, self.y - 40, self.x + 15, self.y - 20
        elif self.mode == 1:
            return self.x - 25, self.y - 50, self.x + 25, self.y - 20
        elif self.mode == 2:
            return self.x - 25, self.y - 50, self.x + 25, self.y - 20

    def mario_head(self):
        if self.mode == 0:
            return self.x - 20, self.y - 20, self.x + 20, self. y + 40
        elif self.mode == 1:
            return self.x - 30, self.y - 20, self.x + 30, self. y + 50
        elif self.mode == 2:
            return self.x - 30, self.y - 20, self.x + 30, self.y + 50

    def timer(self):
        print(self.time)
        self.time += 1
        if self.time == 100:
            self.time = 0

    def fireball(self):
        fb = fireball.FireBall(self.x, self.y, self.dir * 3)
        game_world.add_object(fb, 1)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        if self.y <= -10:
            game_framework.change_state(game_over)

        self.x = clamp(50, self.x, server.background.w - 50)
        self.y = clamp(50, self.y, server.background.h - 50)



    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        debug_print(
            'Velocity : ' + str(self.velocity) + ' Dir : ' + str(self.dir) + 'State : ' + str(self.cur_state.__name__))


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)