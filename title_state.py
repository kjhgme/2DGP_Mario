import game_framework
import select_map_state
from pico2d import *

name = "TitleState"
image = None
start_image = None

def enter():
    global image, start_image
    image = load_image('image/main.jpg')
    start_image = load_image('image/press_space_to_start.png')

def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(select_map_state)

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






