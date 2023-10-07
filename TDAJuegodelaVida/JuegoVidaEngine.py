from TDAArray2D.Array2D import Array2D


class JuegoVida:
    __slots__ = '_life_grid', '_running', '_setup'
    _life_grid: Array2D
    _running: bool
    _setup: bool

    def __init__(self):
        self.set_game_state(False)
        self._life_grid = Array2D()
        self._life_grid.clear(False)

    def set_grid(self, grid: Array2D):
        self._life_grid = grid

    """        dimension = 0
            while dimension <= 0:
                dimension = int(input("Introduzca un numero positivo que será el número de filas y columnos: "))"""
    def setup_game(self, dimension: int):
        self._life_grid.from2values(dimension, dimension)
        self._life_grid.clear(False)

    """def run(self):
        self.set_game_state(True)
        print("Presione 'e' para pasar a la siguiente iteración. Presione 'f' para terminarla.\n")
        while self.get_game_state():
            if keyboard.read_key() == 'e':
                self.evolve()
                print(self)
                print("\nPresione 'e' para pasar a la siguiente iteración. Presione 'f' para terminarla.\n")
            if keyboard.read_key() == 'f':
                self.set_game_state(False)"""

    def get_grid_dimension(self) -> int:
        return self.get_grid().num_rows()

    def reverse_cell_value(self, pos: tuple):
        assert pos[0] in range(self.num_rows()), "This row does not exist"
        assert pos[1] in range(self.num_cols()), "This column does not exist"
        if self.is_live_cell(pos[0], pos[1]):
            self.kill_cel(pos[0], pos[1])
        else:
            self.revive_cel(pos[0], pos[1])

    def get_game_state(self):
        return self._running

    def set_game_state(self, state: bool):
        self._running = state

    def get_setup_state(self):
        return self._setup

    def set_setup_state(self, state: bool):
        self._setup = state

    def get_grid(self):
        return self._life_grid

    def num_rows(self) -> int:
        return self.get_grid().num_rows()

    def num_cols(self) -> int:
        return self.get_grid().num_cols(0)

    def kill_cel(self, i: int, j: int):
        assert i in range(self.num_rows()), "This row does not exist"
        assert j in range(self.num_cols()), "This column does not exist"
        self.get_grid()[i, j] = False

    def revive_cel(self, i: int, j: int):
        assert i in range(self.num_rows()), "This row does not exist"
        assert j in range(self.num_cols()), "This column does not exist"
        self.get_grid()[i, j] = True

    def is_live_cell(self, i: int, j: int) -> bool:
        assert i in range(self.num_rows()), "This row does not exist"
        assert j in range(self.num_cols()), "This column does not exist"
        return self.get_grid()[i, j]

    def num_live_neighbors(self, i: int, j: int) -> int:
        assert i in range(self.num_rows()), "This row does not exist"
        assert j in range(self.num_cols()), "This column does not exist"
        count = 0

        def above_under(value: int, row: int) -> int:
            if row == 0:
                if self.is_live_cell(self.num_rows() - 1, j):
                    value += 1
                if self.is_live_cell(row + 1, j):
                    value += 1
            elif row == self.num_rows() - 1:
                if self.is_live_cell(row - 1, j):
                    value += 1
                if self.is_live_cell(0, j):
                    value += 1
            else:
                if self.is_live_cell(row - 1, j):
                    value += 1
                if self.is_live_cell(row + 1, j):
                    value += 1
            return value

        def right_left(value: int, row: int, col: int) -> int:
            if col == 0:
                if self.is_live_cell(row, self.num_cols()-1) is True:
                    value += 1
                if self.is_live_cell(row, col+1) is True:
                    value += 1
            elif col == self.num_rows() - 1:
                if self.is_live_cell(row, 0) is True:
                    value += 1
                if self.is_live_cell(row, col-1) is True:
                    value += 1
            else:
                if self.is_live_cell(row, col-1) is True:
                    value += 1
                if self.is_live_cell(row, col+1) is True:
                    value += 1
            return value

        count = above_under(count, i)
        count = right_left(count, i, j)
        if i == 0:
            count = right_left(count, self.num_rows() - 1, j)
            count = right_left(count, i+1, j)
        elif i == self.num_rows() - 1:
            count = right_left(count, 0, j)
            count = right_left(count, i-1, j)
        else:
            count = right_left(count, i + 1, j)
            count = right_left(count, i - 1, j)

        return count

    def __str__(self):
        return self.get_grid().__str__()

    def evolve(self):
        h = JuegoVida()
        h.setup_game(self.get_grid_dimension())
        print(self.num_live_neighbors(4, 2))
        print(self.num_live_neighbors(4, 3))
        print(self.num_live_neighbors(4, 4))
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                if self.num_live_neighbors(i, j) <= 1:
                    h.kill_cel(i, j)
                elif self.num_live_neighbors(i, j) > 3:
                    h.kill_cel(i, j)
                elif self.num_live_neighbors(i, j) == 3:
                    h.revive_cel(i, j)
                else:
                    h.get_grid()[i, j] = self.get_grid()[i, j]
        print(h)
        self.set_grid(h.get_grid())


def prueba():
    game = JuegoVida()
    game.revive_cel(0, 0)
    game.revive_cel(1, 2)
    game.revive_cel(0, 3)
    print(game)
    print(game.num_live_neighbors(0, 1))
    print(game.num_live_neighbors(0, 4))
    print(game.num_live_neighbors(5, 3))
    print(game.num_live_neighbors(0, 5))
    print(game.num_live_neighbors(7, 2))
