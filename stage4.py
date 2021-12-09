# stage 4. test 용
from pico2d import *
import game_framework
import game_world
import server
import json
import pickle

import collision
from background import Background
from stage4_mario import Mario
from stage4_gumba import Gumba
from stage4_ground import Ground
from stage4_brick import Brick
from stage4_Qbrick import QBrick

name = "Stage4"

def enter():
    server.background = Background()
    game_world.add_object(server.background, 0)

    with open('stage4_ground_data.json', 'r') as f:     # 땅
        ground_data_list = json.load(f)
    for data in ground_data_list:
        ground = Ground(data['x'], data['y'])
        game_world.add_object(ground, 1)

    with open('stage4_brick_data.json', 'r') as f:      # 일반 벽돌
        brick_data_list = json.load(f)
    for data in brick_data_list:
        server.bricks = Brick(data['x'], data['y'])
        game_world.add_object(server.bricks, 1)

    with open('stage4_Qbrick_data.json', 'r') as f:      # ? 벽돌
        Qbrick_data_list = json.load(f)
    for data in Qbrick_data_list:
        server.Qbricks = QBrick(data['name'], data['x'], data['y'])
        game_world.add_object(server.Qbricks, 1)

    with open('stage4_gumba_data.json', 'r') as f:      # 굼바
        gumba_data_list = json.load(f)
    for data in gumba_data_list:
        server.gumbas = Gumba(data['x'])
        game_world.add_object(server.gumbas, 1)

    server.grounds = ground_data_list
    server.bricks = brick_data_list
    server.Qbricks = Qbrick_data_list
    server.gumbas = gumba_data_list

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
    global grounds
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

