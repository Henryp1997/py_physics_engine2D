import pygame as pg
import time
from Artist import Artist
from CollisionSystem import CollisionSystem
from PhysicsObject import PhysicsObject
from Particle import Particle
from Block import Block


class Engine():
    def __init__(self, artist) -> None:
        self.artist = artist


def start_engine():
    artist = Artist(SCREEN_X=400, SCREEN_Y=400)
    collider = CollisionSystem()
    clock = pg.time.Clock()

    # Main loop
    count = 0
    while True:
        dt = clock.tick(60) / 1000 # Frame duration in seconds

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return

        artist.fill_screen(colour="#000000")
        artist.draw_border("#FF0000", offset=6)

        if count == 0:
            particle = Particle(
                pos=[artist.SCREEN_X*0.7, artist.SCREEN_Y*0.75],
                vel=[240, -288],
                acc=None,
                radius=4,
                mass=2
            )
            blocks = [
                Block(
                    pos=[artist.SCREEN_X*0.9, artist.SCREEN_Y*0.5],
                    width=15,
                    height=40,
                    # mass=20 # 10 times heavier than particle
                ),
                Block(
                    pos=[artist.SCREEN_X*0.5, artist.SCREEN_Y*0.1],
                    width=60,
                    height=5,
                    # mass=20 # 10 times heavier than particle
                ),
                Block( 
                    pos=[artist.SCREEN_X*0.1, artist.SCREEN_Y*0.6],
                    width=5,
                    height=80,
                    # mass=20 # 10 times heavier than particle
                )
            ]

        # Move objects
        particle.move(dt)

        # Collisions
        for block in blocks:
            collider.check_collision(particle, block, dt)
            collider.check_collision(particle, block, dt)
            collider.check_collision(particle, block, dt)

        # Draw objects
        particle.draw(artist, "#FFFFFF")
        
        for block in blocks:
            block.draw(artist, "#FFFFFF")

        count += 1
        pg.display.update()

if __name__ == "__main__":
    start_engine()
