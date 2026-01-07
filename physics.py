import pygame as pg
import time
from Artist import Artist
from CollisionSystem import CollisionSystem
from PhysicsObject import PhysicsObject
from Particle import Particle
from Block import Block


class Engine():
    def __init__(self, artist) -> None:
        self.frame_time = 0
        self.artist = artist


    def frame_dur(self) -> float:
        """ Return the duration of a frame in milliseconds """
        current_time = time.perf_counter()
        dt = current_time - self.frame_time
        self.frame_time = current_time
        return dt


def start_engine():
    artist = Artist(SCREEN_X=400, SCREEN_Y=400)
    engine = Engine(artist)
    collider = CollisionSystem()
    clock = pg.time.Clock()

    # Main loop
    count = 0
    while True:
        engine.frame_time = time.perf_counter() # Keep track of frame time for speed calculations
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return

        artist.fill_screen(colour="#000000")
        artist.draw_border("#FF0000", offset=6)

        if count == 0:
            particle = Particle(
                pos=[artist.SCREEN_X*0.5, artist.SCREEN_Y*0.75],
                vel=[100, -50],
                acc=None,
                radius=4,
                mass=2
            )
            block = Block(
                pos=[artist.SCREEN_X*0.9, artist.SCREEN_Y*0.5],
                width=15,
                height=40,
                # mass=20 # 10 times heavier than particle
            )

        # Collisions
        collider.check_collision(particle, block)

        # Draw objects
        dt = engine.frame_dur()
        particle.move(dt)
        particle.draw(artist, "#FFFFFF")
        block.draw(artist, "#FFFFFF")
        count += 1
        pg.display.update()

if __name__ == "__main__":
    start_engine()
