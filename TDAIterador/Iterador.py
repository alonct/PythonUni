class MiLista:

    __slots__ = '_lista'
    _lista: list

    def __init__(self, lista: list):
        self._lista = lista

    def __iter__(self) -> iter:

        class _IteradorDeMiLista:
            __slots__ = '_listRef', '_pos'
            _pos: int

            def __init__(self, lista: list):
                self._pos = 0
                self._listRef = lista

            def __iter__(self):
                return self

            def __next__(self):
                if self._pos < len(self._listRef):
                    actual = self._pos
                    self._pos += 1
                    return actual
                raise StopIteration
        return _IteradorDeMiLista(self._lista)


if __name__ == '__main__':
    miLista = MiLista([0, 1, 2, 3, 4, 5, 6, 7, 8])
    for elem in miLista:
        print(elem)
