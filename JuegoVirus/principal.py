from jugador import Player
from TDABag.Bag import Bag
from turno import Turno
import carta


class Juego:

    def __init__(self):

        #determinamos el estado actual del juego
        self.running = False

        #cremos la lista donde añadiremos los jugadores
        self.jugadores = Bag()

        print("Bienvenido a un nuevo juego de 'El Virus'")

        #creamos las pilas de cartas
        self.mazo = Bag()
        self.descartes = Bag()
        self.mazo += carta.CartaOrgano('comodin')
        self.mazo += carta.CartaVirus('comodin')
        for i in range(1, 10):
            self.mazo += carta.CartaTratamiento
        for i in range(1,5):
            self.mazo += carta.CartaOrgano('corazon')
            self.mazo += carta.CartaOrgano('estomago')
            self.mazo += carta.CartaOrgano('cerebro')
            self.mazo += carta.CartaOrgano('hueso')
            if i <= 4:
                self.mazo += carta.CartaVirus('rojo')
                self.mazo += carta.CartaVirus('verde')
                self.mazo += carta.CartaVirus('azul')
                self.mazo += carta.CartaVirus('amarillo')
                self.mazo += carta.CartaMedicina('rojo')
                self.mazo += carta.CartaMedicina('verde')
                self.mazo += carta.CartaMedicina('azul')
                self.mazo += carta.CartaMedicina('amarillo')
                self.mazo += carta.CartaMedicina('comodin')

        #acordamos el número de jugadores. Deberá estar comprendido entre 2 y 6.
        self.numplayers = 0
        while 2 <= self.numplayers <= 6:
            self.numplayers = input("Por favor, elija un número de jugadores entre 2 y 6: ")

        for i in range(1,self.numplayers):
            nombre = input("Por favor, escriba el nombre del jugador " + str(i) + ": ")
            self.jugadores += Player(nombre)

        for player in self.jugadores:
            player.dar_cartas(3, self.mazo)

        comienzo = False
        while not comienzo:
            if int(input("Si quiere empezar el juego, escriba 1. Si no, escriba cualquier cosa: ")) == 1:
                comienzo = True
            else:
                comienzo = False

    def run(self):
        turno = Turno()
