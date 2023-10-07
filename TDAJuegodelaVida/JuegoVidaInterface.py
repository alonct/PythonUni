from TDAJuegodelaVida.JuegoVidaEngine import JuegoVida
import pygame as p


class InterfazGrafica:

    def __init__(self, juego: JuegoVida):
        p.init()
        self.grid = juego.get_grid()
        self.width = self.height = 625
        self.dimension = juego.get_grid_dimension()
        self.sq_size = self.height // self.dimension
        self.screen = p.display.set_mode((self.width, self.height))
        self.screen.fill(p.Color("white"))

    def draw_game_state(self):
        colors = [p.Color("white"), p.Color("black")]
        for r in range(self.dimension):
            for c in range(self.dimension):
                if self.grid[r, c] is True:
                    color = colors[0]
                else:
                    color = colors[1]
                p.draw.rect(self.screen, color, p.Rect(c * self.sq_size, r * self.sq_size, self.sq_size, self.sq_size))
