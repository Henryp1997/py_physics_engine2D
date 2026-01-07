import pygame as pg
from Artist import Artist
from PhysicsObject import PhysicsObject
from Particle import Particle
from Block import Block


class CollisionSystem():
    def __init__(self):
        pass
    

    def check_collision(self, a: PhysicsObject, b: PhysicsObject):
        """ Check whether two PhysicsObjects have collided """
        if isinstance(a, Particle) and isinstance(b, Block):
            if a.is_static and b.is_static:
                # Don't compute collisions for static objects
                return
            
            # Particle coordinates
            pl = a.pos[0]
            pr = a.pos[0] + 2*a.radius
            pt = a.pos[1]
            pb = a.pos[1] + 2*a.radius

            if pr < b.left or pl > b.right or pb < b.top or pt > b.bottom:
                # No overlap
                return

            # Candidates for collisions with block. Computes penetration values
            candidates = [
                #   n       penetration
                ((-1, 0),   pr - b.left), # Push particle left
                ((+1, 0),  b.right - pl), # Push particle right
                ((0, -1),    pb - b.top), # Push particle up
                ((0, +1), b.bottom - pt), # Push particle down
            ]

            # Pick normal vector corresponding to smallest penetration
            (nx, ny), _ = min(candidates, key=lambda item: item[1])

            vx, vy = a.vel
            dot = vx*nx + vy*ny
            if dot >= 0:
                # Don't collide if particle is already moving away from block
                return
            
            # Elastic collision (TODO - inelastic collisions)
            a.vel = [vx - 2*dot*nx, vy - 2*dot*ny]

