from TDAPositivo.Positivo import Positivo

class Fecha:
    __slots__ = '_dia', '_mes', '_agno'
    _dia: Positivo
    _mes: Positivo
    _agno: Positivo

    def __init__(self, dia: int, mes: int, agno: int):
        self.set_agno(agno)
        self.set_mes(mes)
        self.set_dia(dia)

    def set_agno(self, agno: int) -> None:
        self._agno = Positivo(agno)

    def get_agno(self) -> Positivo:
        return self._agno

    def set_mes(self, mes: int) -> None:
        assert 0 < mes <= 12, "El mes dado no figura en el calendario"
        self._mes = Positivo(mes)

    def get_mes(self) -> Positivo:
        return self._mes

    def set_dia(self, dia: int) -> None:
        if self.get_mes() in [4, 6, 9, 11]:
            assert 1 <= dia <= 30, "El mes " + str(self.get_mes()) + " solo tiene 30 días. "
            self._dia = Positivo(dia)
        elif self.get_mes() == 2:
            assert 1 <= dia <= 28, "El mes " + str(self.get_mes()) + " solo tiene 28 días. "
            self._dia = Positivo(dia)
        else:
            assert 1 <= dia <= 31, "El mes " + str(self.get_mes()) + " solo tiene 31 días. "
            self._dia = Positivo(dia)

    def get_dia(self) -> Positivo:
        return self._dia

    def __str__(self) -> str:
        return str(self.get_dia()) + "/" + str(self.get_mes()) + "/" + str(self.get_agno())


def prueba():
    fecha1 = Fecha(3,8,2030)
    print(fecha1)
    fecha2 = Fecha(17,2,2010)
    print(fecha2)


if __name__ == '__main__':
    prueba()
