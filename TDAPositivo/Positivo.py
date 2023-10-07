class Positivo:
    __slots__ = '_num'
    _num: int

    def __init__(self, num: int) -> None:
        assert num > 0, "El numero proporcionado no es positivo"
        self.set_num(num)

    def set_num(self, num: int) -> None:
        self._num = num

    def get_num(self) -> int:
        return self._num

    def __str__(self) -> str:
        return str(self.get_num())


def prueba():
    el_tres = Positivo(3)
    print(el_tres)
    '''
    el_cero = Positivo(0)
    print(el_cero)
    el_pi = Positivo(3.14)
    '''


if __name__ == '__main__':
    prueba()
