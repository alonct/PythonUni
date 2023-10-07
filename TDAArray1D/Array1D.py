import ctypes
import random


class Array1D:

    __slots__ = '_size', '_array'
    _size: int
    _array: [list]

    def __init__(self, size):
        assert size > 0, "Error, el número de elementos debe ser mayor a 0"
        self._size = size
        ArrayType = ctypes.py_object * size
        self._array = ArrayType()
        self.clear(None)

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index):
        assert index in range(0, self.__len__()), "No existe ese índice"
        return self._array[index]

    def __setitem__(self, index, value) -> None:
        assert index in range(0, self.__len__()), "No existe ese índice"
        self._array[index] = value

    def clear(self, value) -> None:
        for i in range(0, self.__len__()):
            self._array[i] = value

    def __iter__(self) -> iter:

        class _IteradorDeMiLista:

            __slots__ = '_listRef', '_pos', '_actual'
            _pos: int
            _actual: int

            def __init__(self, lista):
                self._pos = 0
                self._listRef = lista
                self._actual = 0

            def __iter__(self):
                return self

            def __next__(self):
                if self._pos < len(self._listRef):
                    self._actual = self._pos
                    self._pos += 1
                    return self._actual
                raise StopIteration

        return _IteradorDeMiLista(self._array)


if __name__ == '__main__':

    miArray = Array1D(5)
    miArray.clear(4)

    for i in miArray:
        miArray.__setitem__(i, random.randint(10, 50))
        print(miArray[i])
