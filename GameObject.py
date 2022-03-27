from pygame.math import Vector2
from pygame.transform import rotozoom
from settings import *

UP = Vector2(0, 1)


class GameObject:
    def __init__(self, pos, vel, sprite):
        self.pos = Vector2(pos)
        self.sprite = sprite
        self.radius = sprite.get_width()/2
        self.vel = Vector2(vel)

    def obj_move(self):
        self.pos = self.pos + self.vel

    def obj_draw(self, surface):
        blit_pos = self.pos - Vector2(self.radius)
        surface.blit(self.sprite, blit_pos)

    def obj_collide(self, other):
        dis = self.pos.distance_to(other.pos)
        return dis < self.radius + other.radius


class Player(GameObject):
    MANEUV = 3

    def __init__(self, position):
        self.dir = Vector2(UP)
        super().__init__(position, Vector2(0, 0), loader("player"))

    def rotate(self, clockwise):
        if clockwise == True:
            sign = 1
        else:
            sign = -1
        angle = float(self.MANEUV*sign)
        self.dir.rotate_ip(angle)

    def draw(self, surface):
        angle = self.dir.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_pos = self.pos - rotated_surface_size*0.5
        surface.blit(rotated_surface, blit_pos)

class Meteor(GameObject):
    def __init__(self, position):
        super().__init__(position, Vector2(0, 0), loader("meteor"))
