class Map:
    __slots__ = '_dict'
    _dict: list

    class _MapEntry:
        __slots__ = 'key', 'value'

        def __init__(self, key: object, value: object) -> None:
            self.key = key
            self.value = value

    def __init__(self):
        self._dict = list()

    def get_map(self):
        return self._dict

    def __len__(self) -> int:
        return len(self.get_map())

    def __contains__(self, key: object) -> bool:
        for map_entry in self:
            if map_entry.key == key:
                return True
        return False

    def remove(self, key: object):
        assert key in self, "Esta clave no existe en el diccionario"
        self.get_map().pop(self._find_position(key))

    def add(self, key, value) -> bool:
        if key in self:
            self.get_map()[self._find_position(key)].value = value
            return False
        else:
            self.get_map().append(self._MapEntry(key, value))
            return True

    def value_of(self, key: object) -> object:
        assert key in self, "Esta clave no existe en el diccionario"
        return self.get_map()[self._find_position(key)].value

    def __iter__(self):
        return iter(self.get_map())

    def _find_position(self, key: object):
        for i in range(len(self)):
            if self._dict[i].key == key:
                return i
        return None

    def __str__(self):
        cadena = str()
        for entry in self:
            cadena += str(entry.key) + ": " + str(entry.value) + "\n"
        return cadena


def prueba():
    mapa = Map()
    mapa.add('Murcia', 400)
    mapa.add('Cartagena', 200)
    mapa.add('Madrid', 6000)
    mapa.add('Barcelona', 3000)
    print(mapa)
    print(mapa.value_of('Cartagena'))
    print(len(mapa))
    mapa.remove('Madrid')
    print(mapa)


if __name__ == '__main__':
    prueba()
