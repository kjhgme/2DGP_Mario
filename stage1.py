from pico2d import *
import game_framework
import game_world

from mario import Mario
from ground import Ground
from gumba import Gumba

name = "Stage1"
ground = None
mario = None
background = None

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def enter():
    global ground
    ground = Ground()
    game_world.add_object(ground, 0)

    global mario
    mario = Mario()
    game_world.add_object(mario, 1)

    global gumba
    gumba = Gumba()
    game_world.add_object(gumba, 2)

    global background
    if background == None:
        background = load_image('image/background.png')

def exit():
    global background
    del background
    game_world.clear()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                mario.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    background.draw(1300, 350)
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass

