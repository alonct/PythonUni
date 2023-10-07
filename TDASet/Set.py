class Set:
    __slots__ = '_conjunto'
    _conjunto: list

    def __init__(self):
        self._conjunto = list()

    def get_set(self) -> list:
        return self._conjunto

    def __len__(self):
        return len(self.get_set())

    def __contains__(self, item) -> bool:
        if item in self.get_set():
            return True
        else:
            return False

    def remove(self, item) -> None:
        assert item in self, "El elemento no se encuentra en el conjunto."
        self.get_set().remove(item)

    def __add__(self, item) -> None:
        if item in self:
            print("Este elemento ya se encuentra en el conjunto. No se añadirá de nuevo. ")
        else:
            self.get_set().append(item)

    def __eq__(self, setb):
        if self.get_set() == setb.getSet():
            return True
        else:
            return False

    def __iter__(self):
        return iter(self.get_set())

    def is_subset_of(self, setb):
        assert type(setb) == type(self), "El parámetro proporcionado debe ser de tipo Set"
        for item in self:
            if item not in setb:
                return False
        return True

    def intersect(self, setb):
        set_intersect = self
        for item in self:
            if item not in setb:
                set_intersect.remove(item)
        return set_intersect

    def __str__(self):
        cadena = str()
        for item in self:
            if item == self.get_set()[len(self)-1]:
                cadena = cadena + str(item) + ". "
            else:
                cadena = cadena + str(item) + ", "
        return cadena


def prueba():
    conjunto1 = Set()
    conjunto2 = Set()
    conjunto1 + "Rana"
    conjunto1 + "Casa"
    conjunto2 + "Rana"
    print(conjunto1)
    print(conjunto2)
    a = conjunto1.is_subset_of(conjunto2)
    print(a)
    b = conjunto2.is_subset_of(conjunto1)
    print(b)
    conjunto2 + "Gato"
    print(conjunto1)
    print(conjunto2)
    conjunto3 = conjunto1.intersect(conjunto2)
    print(conjunto3)


if __name__ == '__main__':
    prueba()
