import pygame as pg
from Artist import Artist
from PhysicsObject import PhysicsObject


class Particle(PhysicsObject):
    def __init__(self, *args, radius=10, is_static=False, **kwargs):
        super().__init__(*args, is_static=is_static, **kwargs)
        self.radius = radius
    

    def draw(self, artist: Artist, colour: str, linewidth=0):
        """ Set linewidth > 0 for edge colouring only """
        cx = self.pos[0] + self.radius
        cy = self.pos[1] + self.radius
        artist.draw_circle(colour, cx, cy, self.radius, linewidth=linewidth)
