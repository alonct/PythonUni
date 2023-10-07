class Bag:
    __slots__ = '_bag'
    _bag: list

    def __init__(self):
        self._bag = list()

    def get_bag(self) -> list:
        return self._bag

    def __len__(self) -> int:
        return len(self.get_bag())

    def __contains__(self, item) -> bool:
        if item in self.get_bag():
            return True
        else:
            return False

    def remove_item(self, item) -> None:
        assert item in self, "Este item no se encuentra en la bolsa"
        self.get_bag().pop(item)

    def __add__(self, item) -> None:
        self.get_bag().append(item)

    def __iter__(self):
        return iter(self.get_bag())

    def __getitem__(self, index):
        assert index in range(0, len(self.get_bag())), "Este ímdice no se encuentra disponible"
        return self.get_bag()[index]


def prueba():
    bolsa = Bag()
    bolsa + "Rana"
    bolsa + "Casa"
    for item in bolsa:
        print(item)
    bolsa.remove_item("Rana")
    for item in bolsa:
        print(item)


if __name__ == '__main__':
    prueba()
