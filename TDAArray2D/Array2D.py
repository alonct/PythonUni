from TDAArray1D.Array1D import Array1D


class Array2D:
    __slots__ = '_the_rows'
    _the_rows: Array1D

    def __init__(self, *args: int):
        cols = tuple(args)
        rows = len(cols)
        if rows == 0:
            self._the_rows = Array1D(1)
            self._the_rows[0] = Array1D(1)
        else:
            assert rows > 0, "Array rows must be > 0 exception"
            self._the_rows = Array1D(rows)
            for i in range(rows):
                assert cols[i] > 0, "Array cols must be > 0 exception"
                self._the_rows[i] = Array1D(cols[i])

    def add_row(self, row: Array1D, index=-1) -> None:
        assert type(index) == int, "Index should be int type"
        assert index >= -1, "Index should be 0 or bigger"
        if index == -1:
            nuevo_array = Array1D(len(self.get_array()) + 1)
            for i in range(len(self.get_array())):
                nuevo_array[i] = self.get_array()[i]
            nuevo_array[len(nuevo_array) - 1] = row
            self._the_rows = nuevo_array
        else:
            assert index in range(len(self.get_array())), "This index does not exist"
            nuevo_array = Array1D(len(self.get_array()) + 1)
            for i in range(index):
                nuevo_array[i] = self.get_array()[i]
            nuevo_array[index] = row
            for i in range(index + 1, len(nuevo_array)):
                nuevo_array[i] = self.get_array()[i-1]
            self._the_rows = nuevo_array

    def remove_row(self, index: int):
        assert index in range(len(self.get_array())), "This index does not exist"
        nuevo_array = Array1D(len(self.get_array()) - 1)
        for i in range(index):
            nuevo_array[i] = self.get_array()[i]
        for i in range(index, len(nuevo_array)):
            nuevo_array[i] = self.get_array()[i + 1]
        self._the_rows = nuevo_array

    def from2values(self, rows: int, cols: int):
        assert rows >= 1, "Array must be > 0"
        for i in range(rows):
            self.add_row(Array1D(cols))
        self.clear(0)
        for i in range(len(self.get_array()) - rows):
            self.remove_row(i)

    def get_array(self):
        return self._the_rows

    def num_rows(self):
        return len(self.get_array())

    def num_cols(self, row: int):
        assert row in range(self.num_rows()), "This row does not exist within the matrix provided"
        return len(self.get_array()[row])

    def __getitem__(self, index: tuple):
        assert index[0] in range(len(self.get_array())), "This row does not exist within the matrix provided"
        assert index[1] in range(len(self.get_array()[index[0]])), \
            "This column position des not exist in row " + index[0] + ". "
        return self.get_array()[index[0]][index[1]]

    def __setitem__(self, index: tuple, value):
        assert index[0] in range(len(self.get_array())), "This row does not exist within the matrix provided"
        assert index[1] in range(len(self.get_array()[index[0]])), \
            "This column position des not exist in row " + index[0] + ". "
        self.get_array()[index[0]][index[1]] = value

    def clear(self, value):
        for row in range(len(self.get_array())):
            self.get_array()[row].clear(value)

    def __iter__(self):

        class _Iter:
            __slots__ = '_row', '_matrix'
            _row: int

            def __init__(self, array):
                self._row = 0
                self._matrix = array

            def __iter__(self):
                return self._matrix[self._row].__iter__

            def __next__(self):
                if self._row in range(len(self._matrix)):
                    actual = self._matrix[self._row]
                    self._row += 1
                    return actual.__iter__
                raise StopIteration

        return _Iter(self.get_array())

    def __str__(self):
        matrix = str()
        matrix += "[ \n"
        for i in range(self.num_rows()):
            for j in range(self.num_cols(i)):
                if j < self.num_cols(i) - 1:
                    matrix += str(self.get_array()[i][j]) + ", " + "\t"
                else:
                    matrix += str(self.get_array()[i][j]) + "; "
            matrix += "\n"
        matrix += " ]"
        return matrix


def main():
    mi_array = Array2D(2, 4, 6, 2)

    for i in range(mi_array.num_rows()):
        for j in range(mi_array.num_cols(i)):
            mi_array[i, j] = (i + 1) * 10 + (j + 1)

    print(mi_array)

    column = Array1D(3)
    column.clear("Hola")

    mi_array.add_row(column, 2)
    print(mi_array)

    mi_array.remove_row(4)
    print(mi_array)
    array = Array2D()
    print(array)
    array.from2values(3, 4)
    print(array)
    array.clear(False)
    print(array)


if __name__ == '__main__':
    main()
