from pico2d import *

RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_UP,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_UP
}

class IdleState:
    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity_x -= 1
        elif event == LEFT_DOWN:
            mario.velocity_x += 1
        elif event == RIGHT_UP:
            mario.velocity_x += 1
        elif event == LEFT_UP:
            mario.velocity_x -= 1
        elif event == UP_DOWN:
            mario.velocity_y -= 1
        elif event == DOWN_DOWN:
            mario.velocity_y += 1
        elif event == UP_UP:
            mario.velocity_y += 1
        elif event == DOWN_UP:
            mario.velocity_y -= 1

    def exit(mario, event):
        pass

    def do(mario):
        if mario.dir == 1:
            mario.image = load_image('image/mario/bigmario/marioR/stand.png')
        else:
            mario.image = load_image('image/mario/bigmario/marioL/stand.png')

    def draw(mario):
        mario.image.clip_draw(0, 0, 70, 90, mario.x, mario.y)

class RunState:
    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity_x += 1
        elif event == LEFT_DOWN:
            mario.velocity_x -= 1
        elif event == RIGHT_UP:
            mario.velocity_x -= 1
        elif event == LEFT_UP:
            mario.velocity_x += 1
        elif event == UP_DOWN:
            mario.velocity_y += 1
        elif event == DOWN_DOWN:
            mario.velocity_y -= 1
        elif event == UP_UP:
            mario.velocity_y -= 1
        elif event == DOWN_UP:
            mario.velocity_y += 1
        mario.dir = mario.velocity_x

    def exit(mario, event):
        pass

    def do(mario):
        mario.frame = (mario.frame + 1) % 21
        if mario.velocity_x == 1:
            mario.image = load_image('image/mario/bigmario/marioR/' + str(mario.frame) + '.png')
        elif mario.velocity_x == -1:
            mario.image = load_image('image/mario/bigmario/marioL/' + str(mario.frame) + '.png')

    def draw(mario):
        mario.image.clip_draw(0, 0, 70, 90, 400, 300)

next_state_table = {
    IdleState: {RIGHT_DOWN: RunState, LEFT_DOWN: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState,
                RIGHT_UP: IdleState, LEFT_UP: IdleState, UP_UP: IdleState, DOWN_UP: IdleState
                },
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, UP_UP: IdleState, DOWN_UP: IdleState,
               RIGHT_DOWN: RunState, LEFT_DOWN: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState}
}

class Select_Mario:
    def __init__(self):
        self.x, self.y = 400, 300
        self.image = load_image('image/mario/bigmario/marioR/stand.png')
        self.dir = 1
        self.frame = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def change_state(self,  state):
        # fill here
        pass

    def add_event(self, event):
        # fill here
        self.event_que.insert(0, event)
        pass

    def update(self):
        # fill here
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        # fill here
        self.cur_state.draw(self)
        debug_print('Velocity : ' + str(self.velocity_x) + ', ' + str(self.velocity_y) + ' Dir : ' + str(self.dir) + 'State : ' + str(self.cur_state.__name__))
        pass

    def handle_event(self, event):
        # fill here
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        pass
