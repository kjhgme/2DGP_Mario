from pico2d import *
import select_map_state

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, UP_DOWN, UP_UP, SPACE = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}

class IdleState:
    pass

class RunState:
    pass

class JumpState:
    pass

class FireballState:
    pass

next_state_table = {

}

class Mario:
    def __init__(self):
        pass

    def change_state(self, state):
        pass

    def add_event(self, event):
        self.event_que.insert(0, event)
        pass

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        # fill here
        self.cur_state.draw(self)
        debug_print('Velocity : ' + str(self.velocity) + ' Dir : ' + str(self.dir) + 'State : ' + str(self.cur_state.__name__))
        pass

    def handle_event(self, event):
        # fill here
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        pass