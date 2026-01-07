import pygame as pg
from Artist import Artist
from PhysicsObject import PhysicsObject


class Block(PhysicsObject):
    def __init__(self, *args, width=10, height=10, is_static=True, has_gravity=False, **kwargs):
        super().__init__(*args, is_static=is_static, has_gravity=has_gravity, **kwargs)
        self.width = width
        self.height = height
        self.left = self.pos[0]
        self.right = self.left + self.width
        self.top = self.pos[1]
        self.bottom = self.top + self.height
    

    def draw(self, artist: Artist, colour: str, linewidth=0):
        """ Set linewidth > 0 for edge colouring only """
        x, y = self.pos
        w, h = self.width, self.height
        artist.draw_rect(colour, x=x, y=y, w=w, h=h, linewidth=linewidth)
