from TDABag.Bag import Bag
import random

class Player:

    def __init__(self, nombre):
        self.mano = Bag()
        self.pila_huesos = Bag()
        self.pila_corazon = Bag()
        self.pila_cerebro = Bag()
        self.pila_estomago = Bag()

    def colocar_carta_monton(self, monton):
        pass

    def usar_tratamiento(self):
        pass

    def descartar_cartas(self):
        pass

    def dar_cartas(self, numcartas: int, mazo: Bag):
        assert 1 <= numcartas <= len(mazo), "No hay suficientes cartas en el mazo"
        for i in range(1, numcartas):
            carta = mazo[random.randint(0, len(mazo))]
            self.mano += carta
            mazo.remove_item(carta)
