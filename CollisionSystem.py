import pygame as pg
from Artist import Artist
from PhysicsObject import PhysicsObject


class CollisionSystem():
    def __init__(self):
        pass
    

    def check_collision(self, a: PhysicsObject, b: PhysicsObject):
        """ Check whether two PhysicsObjects have collided """
        