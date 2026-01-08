from copy import deepcopy
import pygame as pg
from abc import ABC, abstractmethod


class PhysicsObject(ABC):
    def __init__(self, pos, vel=None, acc=None, mass=None, is_static=True, has_gravity=True):
        self.pos = pos # Position vector
        self.vel = vel # Velocity vector
        self.acc = acc # Acceleration vector TODO - implement
        self.mass = mass
        self.is_static = is_static     # Will the object move
        self.has_gravity = has_gravity # Is the object affected by gravity

        if not self.is_static and self.vel is None:
            raise ValueError("PhysicsObject: cannot set is_static=False and vel=None")
    
        if self.is_static and self.vel is not None:
            raise ValueError("PhysicsObject: cannot set is_static=True and a real velocity. Velocity must be set to None")
        
        if self.mass is not None and self.is_static:
            print(
                f"PhysicsObject: Warning - mass={mass} has no effect because is_static=True. "\
                "Set is_static to False if this object's velocity is to be affected by collisions"
            )

        elif self.mass is None and not self.is_static:
            raise ValueError(f"PhysicsObject. Cannot set mass=None if is_static=False. Must set a positive mass.")


    def move(self, dt):
        """ Update the object's position in 2D space """
        self.prev_pos = deepcopy(self.pos) # Previous (frame before current) position vector
        self.pos[0] += dt * self.vel[0]
        self.pos[1] += dt * self.vel[1]


    @abstractmethod
    def draw(self, artist):
        pass
