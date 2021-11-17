from pico2d import *
import game_framework
import game_world

# gamestage들 추가하기
import stage1
import stage3

from select_mario import SelectMario

name = "SelectMapState"
image = None
background = None
mario = None

def enter():
    global image, background
    global mario
    mario = SelectMario()
    game_world.add_object(mario, 0)
    background = load_image('image/background.png')
    image = load_image('image/select_map.png')

def exit():
    global image, background
    del background
    del image
    game_world.clear()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                if mario.selectX == 1:
                    pass
                else:
                    mario.selectX += 1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                if mario.selectX == -1:
                    pass
                else:
                    mario.selectX -= 1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                if mario.selectY == 1:
                    pass
                else:
                    mario.selectY += 1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                if mario.selectY == -1:
                    pass
                else:
                    mario.selectY -= 1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if (mario.selectX, mario.selectY) == (-1, 1):
                    game_framework.change_state(stage1)
                elif (mario.selectX, mario.selectY) == (0, 1):
                    print(2)
                elif (mario.selectX, mario.selectY) == (1, 1):
                    game_framework.change_state(stage3)
                elif (mario.selectX, mario.selectY) == (-1, 0):
                    print(4)
                elif (mario.selectX, mario.selectY) == (0, 0):
                    print(5)
                elif (mario.selectX, mario.selectY) == (1, 0):
                    print(6)
                elif (mario.selectX, mario.selectY) == (-1, -1):
                    print(7)
                elif (mario.selectX, mario.selectY) == (0, -1):
                    print(8)
                elif (mario.selectX, mario.selectY) == (1, -1):
                    print(9)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    background.draw(1300, 350)
    image.draw(400, 300)
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass

