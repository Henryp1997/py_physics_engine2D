import pygame as pg
from Artist import Artist
from PhysicsObject import PhysicsObject
from Particle import Particle
from Block import Block


class CollisionSystem():
    def __init__(self):
        pass
    

    def check_collision(self, a: PhysicsObject, b: PhysicsObject, dt):
        """ Check whether two PhysicsObjects have collided """
        if isinstance(a, Particle) and isinstance(b, Block):
            return self.particle_block(dt)
        
    
    def particle_block(self, a: PhysicsObject, b: PhysicsObject, dt):
        if a.is_static and b.is_static:
            # Don't compute collisions for static objects
            return
        
        # Particle center at start of frame and particle velocity
        r = a.radius
        cx, cy = a.prev_pos[0] + r, a.prev_pos[1] + r
        vx, vy = a.vel

        # Expand block coords by particle radius
        left = b.left - r
        right = b.right + r
        top = b.top - r
        bottom = b.bottom + r

        # tx1 and tx2 describe at what time the particle hits the
        # left and right coordinates respectively (in the interval 0 --> dt)
        # tx_entry and tx_exit pick either tx1 or tx2 depending on left->right or right-> left motion
        # These equations come from solving x(t) = cx + vx * t, where t = tx1 or tx2
        tx1 = (left - cx) / vx
        tx2 = (right - cx) / vx
        tx_entry = min(tx1, tx2)
        tx_exit = max(tx1, tx2)

        # Same for top and bottom
        ty1 = (top - cy) / vy
        ty2 = (bottom - cy) / vy
        ty_entry = min(ty1, ty2)
        ty_exit = max(ty1, ty2)

        # Pick the latest time that the particle is inside the block
        # This guarantees that the particle is within both the x-axis AND y-axis bounds
        # And vice versa - pick the earliest time the particle leaves the block
        t_entry = max(tx_entry, ty_entry)
        t_exit = min(tx_exit, ty_exit)

        ### No collision this frame
        # t_entry > t_exit means there was never an overlap where
        # the particle was both in the x-axis bounds AND the y-axis bounds
        if t_entry > t_exit:
            return False

        # t_exit < 0 means the overlap interval occurred before the frame started
        if t_exit < 0:
            return False
        
        # t_entry > dt means the overlap interval will occur after this frame
        if t_entry > dt:
            return False            

        t_hit = max(t_entry, 0.0) # Collision time

        # Calculate normal vector
        if tx_entry > ty_entry:
            # If entered the x-axis bounds latest
            nx = -1.0 if vx > 0 else 1.0
            ny = 0.0
        else:
            # If entered the y-axis bounds latest
            nx = 0.0
            ny = -1.0 if vy > 0 else 1.0

        # Snap to contact point
        a.pos[0] = cx - r + vx*t_hit
        a.pos[1] = cy - r + vy*t_hit

        # Reflect velocity (elastic)
        dot = vx*nx + vy*ny
        if dot >= 0:
            # Don't reflect velocity if not moving INTO the block
            return False

        a.vel[0] -= 2 * dot*nx
        a.vel[1] -= 2 * dot*ny

        # Move remaining time
        remaining = dt - t_hit
        a.pos[0] += a.vel[0]*remaining
        a.pos[1] += a.vel[1]*remaining

        return True
