from pico2d import *
import game_framework
import title_state
import game_world
from select_mario import Select_Mario

name = "SelectMapState"
image = None
background = None
mario = None

def enter():
    global image, background
    global mario
    mario = Select_Mario()
    background = load_image('image/background.png')
    image = load_image('image/select_map.png')

def exit():
    global image, background
    global mario
    del background
    del image
    del mario
    game_world.clear()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            mario.handle_event(event)

def update():
    mario.update()
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    background.draw(1300, 350)
    image.draw(400, 300)
    mario.draw()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass

