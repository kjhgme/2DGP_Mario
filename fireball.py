from pico2d import *
import game_world

class FireBall:
    image = None

    def __init__(self, x=20, y=20, velocity = 1):
        if FireBall.image == None:
            FireBall.image = load_image('image/fireball.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.clip_draw(0, 0, 20, 20, self.x, self.y)


    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-10, self.y-10, self.x+10, self.y+10
