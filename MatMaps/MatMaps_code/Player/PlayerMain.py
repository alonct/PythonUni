from MatMaps.MatMaps_code.Extras.Herramientas import Util
from MatMaps.MatMaps_code.Vehicles.VehicleMain import Vehicle
import random


class Player:

    def __init__(self, posicion: str, nombre=None, dinero=None, speed=None):
        self.name = nombre
        self.location = posicion
        self.cartera = dinero
        self.walking_speed = speed
        self.current_speed = self.walking_speed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, nombre=None):
        if nombre is None:
            lista_nombres = r'C:\Users\marco\Desktop\PythonDefinitivo\MatMaps\MatMaps_files\lista_nombres_persona.txt'
            lista = Util.conversor_txt_list(lista_nombres)
            nombre = random.choice(lista)
            self._name = nombre
        else:
            assert type(nombre) is str, "El nombre debe estar en formato str. "
            self._name = nombre

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location: str):
        self._location = location

    @property
    def cartera(self):
        return self._cartera

    @cartera.setter
    def cartera(self, dinero=None):
        if dinero is None:
            self._cartera = int()
            self._cartera = 0
        else:
            assert type(dinero) is int, "El dinero debe ir dado en enteros"
            self._cartera = dinero

    @property
    def walking_speed(self):
        return self._walking_speed

    @walking_speed.setter
    def walking_speed(self, speed=None):
        if speed is None:
            self._walking_speed = random.randint(4, 6)
        else:
            assert type(speed) is int, "La velocidad debe ser dada en enteros km/h. "
            self._walking_speed = speed

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, speed: int):
        self._current_speed = speed

    def use_vehicle(self, vehicle: Vehicle):
        self.current_speed = vehicle.speed

    def viajar(self, lugar: str):
        self.location = lugar

    def pagar(self, pago: int):
        assert self.cartera - pago >= 0, "Raise excepción no tiene suficiente dinero"
        self.cartera -= pago

    def cobrar(self, cobro: int):
        self.cartera += cobro

    def robar(self, jugador: object, cantidad: int):
        pass
