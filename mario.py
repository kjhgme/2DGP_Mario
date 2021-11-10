from pico2d import *

stance = 0
num = 0
x = 20
y = 90
class Backgrond:
    def __init__(self):
        self.image = load_image('image/background.png')

    def draw(self):
        self.image.draw(0, 400, 2666, 728)

class Small_mario:
    global dir
    global num
    def __init__(self):
        self.x, self.y = 20, 90
        self.image = load_image('image/mario/smallmario/marioR/stand.png')
        self.frame = 0

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.frame, 0, 50, 80, x, y)

class Gumba:
    def __init__(self):
        self.x, self.y = 700, 80
        self.image = load_image('image/monster/monsterL/0.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 5
        self.image = load_image('image/monster/monsterL/'+str(self.frame)+'.png')
        self.x -= 2

    def draw(self):
        self.image.clip_draw(0, 0, 50, 60, self.x, self.y)

class Turtle:
    def __init__(self):
        self.x, self.y = 500, 80
        self.image = load_image('image/tortoise/tortoiseL/0.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 12
        self.image = load_image('image/tortoise/tortoiseL/' + str(self.frame) + '.png')
        self.x -= 2

    def draw(self):
        self.image.clip_draw(0, 0, 55, 70, self.x, self.y)

def Handle_events():
    global running
    global x
    global y
    global dir
    global stance

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                stance = 1
            elif event.key == SDLK_LEFT:
                dir -= 1
                stance = 2
            elif event.key == SDLK_UP:
                y += 10
                stance = 3
            elif event.key == SDLK_UP:
                y += 10
                stance = 4
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                stance = 0
            elif event.key == SDLK_LEFT:
                dir += 1
                stance = 5
            elif event.key == SDLK_UP:
                y -= 10
                stance = 0

open_canvas()
background =Backgrond()
small_mario = Small_mario()
gumba = Gumba()
turtle = Turtle()
running = True
dir = 0

def mario_stance():
    global num
    if stance == 0:
        small_mario.image = load_image('image/mario/smallmario/marioR/stand.png')
    elif stance == 1:
        num = (num + 1) % 22
        small_mario.image = load_image('image/mario/smallmario/marioR/' + str(num) + '.png')
    elif stance == 2:
        num = (num + 1) % 22
        small_mario.image = load_image('image/mario/smallmario/marioL/' + str(num) + '.png')
    elif stance == 3:
        small_mario.image = load_image('image/mario/smallmario/marioR/jump.png')
    elif stance == 4:
        small_mario.image = load_image('image/mario/smallmario/marioL/jump.png')
    elif stance == 5:
        small_mario.image = load_image('image/mario/smallmario/marioL/stand.png')

while running:
    clear_canvas()
    background.draw()
    small_mario.draw()
    gumba.draw()
    turtle.draw()
    update_canvas()
    small_mario.update()
    gumba.update()
    turtle.update()
    Handle_events()
    x += dir * 5
    mario_stance()
    delay(0.01)

close_canvas()
