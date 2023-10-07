from TDAJuegodelaVida.JuegoVidaEngine import JuegoVida
from TDAJuegodelaVida.JuegoVidaInterface import InterfazGrafica
import pygame as p


class GameMain:
    __slots__ = '_game', '_graphics', 'maxFPS'
    _game: JuegoVida
    _graphics: InterfazGrafica
    maxFPS: int

    def __init__(self, dimension: int):
        p.init()
        self.maxFPS = 15
        self._game = JuegoVida()
        self._game.setup_game(dimension)
        self._graphics = InterfazGrafica(self._game)
        InterfazGrafica(self._game).draw_game_state()

    def setup(self):
        clock = p.time.Clock()
        setup = True
        while setup:
            for e in p.event.get():
                if e.type == p.QUIT:
                    setup = False
                # mouse handler
                elif e.type == p.MOUSEBUTTONDOWN:
                    location = p.mouse.get_pos()
                    col = location[0] // self._graphics.sq_size
                    row = location[1] // self._graphics.sq_size
                    self._game.reverse_cell_value((row, col))
                    print(self._game)
                elif e.type == p.KEYDOWN:
                    if e.key == p.K_SPACE:
                        setup = False
                    if e.key == p.K_ESCAPE:
                        setup = False
            InterfazGrafica(self._game).draw_game_state()
            clock.tick(self.maxFPS)
            p.display.flip()

    def run(self):
        clock = p.time.Clock()
        running = True
        while running:
            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
                # mouse handler
                elif e.type == p.MOUSEBUTTONDOWN:
                    self._game.evolve()
                    print(self._game)
                elif e.type == p.KEYDOWN:
                    if e.key == p.K_ESCAPE:
                        running = False
            InterfazGrafica(self._game).draw_game_state()
            clock.tick(self.maxFPS)
            p.display.flip()


def main():
    juego = GameMain(25)
    juego.setup()
    juego.run()


if __name__ == '__main__':
    main()
