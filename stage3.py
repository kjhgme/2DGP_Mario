# stage 3.
# ( 필요사항 ) 정확한 위치에 객체생성.
from pico2d import *
import game_framework
import game_world
import server
import collision
from background import ClassicBackground as Background

from test2 import Mario
from ice_ground import IceGround


name = "Stage3"


def enter():
    server.background = Background()
    game_world.add_object(server.background, 0)

    server.grounds = [IceGround() for i in range(2)]
    game_world.add_objects(server.grounds, 1)

    server.mario = Mario()
    game_world.add_object(server.mario, 1)


def exit():
    game_world.clear()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            server.mario.handle_event(event)

def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass

