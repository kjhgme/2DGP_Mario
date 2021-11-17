import game_framework
import select_map_state
from pico2d import *

name = "GameOverState"
image = None

def enter():
    global image
    image = load_image('image/over.png')

def exit():
    global image
    del(image)

def update():
    pass

def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                #game_framework.change_state(select_map_state)
                game_framework.quit()

def pause(): pass


def resume(): pass




