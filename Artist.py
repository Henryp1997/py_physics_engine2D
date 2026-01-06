import pygame as pg

class Artist():
    def __init__(self, SCREEN_X, SCREEN_Y) -> None:
        self.screen = pg.display.set_mode((SCREEN_X, SCREEN_Y))
        self.SCREEN_X = SCREEN_X
        self.SCREEN_Y = SCREEN_Y
 

    def fill_screen(self, colour) -> None:
        self.screen.fill(colour)


    def draw_rect(self, colour, x, y, w, h, linewidth=0, border_radius=0):
        pg.draw.rect(
            self.screen,
            colour,
            pg.Rect((x, y, w, h)),
            border_radius=border_radius,
            width=linewidth
        )


    def draw_border(self, colour, linewidth=1, border_radius=0, offset=0) -> None:
        w, h = self.screen.get_size()
        self.draw_rect(
            colour, x=offset, y=offset, w=w-2*offset, h=h-2*offset,
            linewidth=linewidth, border_radius=border_radius
        )


    def draw_circle(self, colour, cx, cy, radius, linewidth=0):
        """
        Draw a circle. Default is to fill with the specified
        colour (linewidth=0). Set linewidth > 0 to draw just the outline
        """
        pg.draw.circle(self.screen, colour, (cx, cy), radius, width=linewidth)
