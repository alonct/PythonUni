class Carta:

    __slots__ = '_tipo'
    _tipo: str

    def __init__(self, tipo: str):
        self._tipo = tipo

    def get_tipo(self):
        return self._tipo


class CartaOrgano(Carta):

    def __init__(self, organo):
        super().__init__('Organo')
        self._organo = organo

    def get_organo(self):
        return self._organo


class CartaVirus(Carta):

    def __init__(self, color):
        super().__init__('Virus')
        self._color = color

    def get_color(self):
        return self._color


class CartaMedicina(Carta):

    def __init__(self, color):
        super().__init__('Medicamento')
        self._color = color

    def get_color(self):
        return self._color

class CartaTratamiento(Carta):

    def __init__(self):
        super().__init__('Tratamiento')