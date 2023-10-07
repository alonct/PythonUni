# from MatMaps.MatMaps_code.Interfaces.Interfaces_PI import IService

from MatMaps.MatMaps_code.TDAs.Set import Set
import random
from MatMaps.MatMaps_code.Extras.Herramientas import Util


class PuntoInt:

    def __init__(self, name=None, adress=None, city=None, coordinates=None, capacity=None):
        self.name = name
        self.adress = adress
        self.city = city
        self.coordinates = coordinates
        self.closePI = list()
        self.capacity = capacity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name=None):
        self._name = Util.name_creator(None, name)

    @property
    def adress(self):
        return self._adress

    @adress.setter
    def adress(self, adress: str):
        self._adress = adress

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city: str):  # Tal vez cambiar el tipo de objeto
        self._city = city

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self._coordinates = coordinates

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity=int):
        if type(capacity) is int:
            self._capacity = capacity
        else:
            self._capacity = random.randint(20, 100)

    def print_gps_info(self) -> None:
        print("Nombre: " + self.name)
        print("Dirección: " + self.adress)
        print("Ciudad: " + self.city)
        print("Coordenadas: " + str(self.coordinates) + "\n")


class Parking(PuntoInt):

    prefijo = "Parking"  # class variable

    def __init__(self, subterranean=None, parking_time=None, cost=None, name=None, adress=None, city=None, coordinates=None,
                 capacity=None):
        super().__init__(name, adress, city, coordinates, capacity)
        self.name = Util.name_creator(Parking.prefijo, name)
        self.cost = cost
        self.is_subterranean = subterranean
        self.parking_time = parking_time

    @property
    def is_subterranean(self):
        return self._is_subterranean

    @is_subterranean.setter
    def is_subterranean(self, is_subterranean=None):
        if type(is_subterranean) is bool:
            self._is_subterranean = is_subterranean
        else:
            aux = [True, False]
            self._is_subterranean = random.choice(aux)

    @property
    def parking_time(self):
        return self._parking_time

    @parking_time.setter
    def parking_time(self, time=None):
        if type(time) is int:
            self._parking_time = time
        else:
            self._parking_time = random.randint(10, 480)

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost=None):
        if type(cost) is int:
            self._cost = int
        else:
            self._cost = random.randint(0, 3)

    def __str__(self):
        devuelve = str()
        devuelve += "   " + self.name + "\n"
        if self.is_subterranean:
            devuelve += "Es un parking subterráneo\n"
        else:
            devuelve += "No es un parking subterráneo\n"
        devuelve += "El tiempo máximo de aparcamiento es de " + str(self.parking_time) + " minutos, es decir " + \
                    str(Util.minutes_to_hours(self.parking_time)) + " horas.\n"
        devuelve += "El precio por hora de aparcamiento es de " + str(self.cost) + "€.\n"
        return devuelve


class Restaurant(PuntoInt):

    prefijos = Util.conversor_txt_list(r"C:\Users\marco\Desktop\PythonDefinitivo\MatMaps\MatMaps_files\prefijos_Restaurantes.txt")
    platos_basicos = Util.conversor_txt_list(r"C:\Users\marco\Desktop\PythonDefinitivo\MatMaps\MatMaps_files\lista_comidas.txt")
    bebidas_basicas = Util.conversor_txt_list(r"C:\Users\marco\Desktop\PythonDefinitivo\MatMaps\MatMaps_files\lista_bebidas.txt")

    def __init__(self,  name=None, adress=None, city=None, capacity=None, average_cost=None, dish_list=None,
                 drinks_list=None, average_eating_time=None, coordinates=None):
        super().__init__(name, adress, city, coordinates, capacity)
        self.name = Util.name_creator(Restaurant.prefijos, name)

        if type(average_cost) != int:
            self.average_cost = random.randint(15, 80)
        else:
            self.average_cost = average_cost

        self.menu = dict()
        self.menu = self.create_menu(dish_list, drinks_list)

        if type(average_eating_time) != int:
            self.average_eating_time = random.randint(10, 60)
        else:
            self.average_eating_time = average_eating_time

    @classmethod
    def create_menu(cls, dish_list=None, drinks_list=None):

        platos = Set()      # TDA Set
        bebidas = Set()
        menu = dict()

        if type(dish_list) is list:
            lista_platos = dish_list
        else:
            lista_platos = cls.platos_basicos
        if type(drinks_list) is list:
            lista_bebidas = drinks_list
        else:
            lista_bebidas = cls.bebidas_basicas

        if len(lista_platos) >= 6:
            num_dishes = 6
        else:
            num_dishes = random.randint(0, len(lista_platos))

        if len(lista_bebidas) >= 3:
            num_drinks = 3
        else:
            num_drinks = random.randint(0, len(lista_bebidas))

        while len(platos) != num_dishes:
            plato = Util.list_to_string(random.choice(lista_platos))
            platos.__add__(plato)

        while len(bebidas) < num_drinks:
            drink = Util.list_to_string(random.choice(lista_bebidas))
            bebidas.__add__(drink)

        menu["Bebidas"] = bebidas
        menu["Platos"] = platos

        return menu

    def __str__(self):
        devuelve = str()
        devuelve += self.name + "\n"
        devuelve += "El precio medio del menu de manera habitual es de " + str(self.average_cost) + "€. \n"
        devuelve += "En el menú de hoy tenemos: \n"
        devuelve += "   De beber:\n"
        for element in self.menu["Bebidas"]:
            devuelve += "       " + element + "\n"
        devuelve += "   De comer:\n"
        for element in self.menu["Platos"]:
            devuelve += "       " + element + "\n"
        devuelve += "El tiempo medio de consumición es de " + str(self.average_eating_time) + " minutos"
        devuelve += " y tiene una capacidad máxima de " + str(self.capacity) + " personas. \n"
        return devuelve

    @property
    def average_eating_time(self):
        return self._average_eating_time

    @average_eating_time.setter
    def average_eating_time(self, average_eating_time=None):
        if average_eating_time is None:
            self._average_eating_time = random.randint(15, 60)
        else:
            self._average_eating_time = average_eating_time

    @property
    def menu(self):
        return self._menu

    @menu.setter
    def menu(self, menu: dict):
        self._menu = menu

    @property
    def average_cost(self):
        return self._average_cost

    @average_cost.setter
    def average_cost(self, average_cost: int):
        self._average_cost = average_cost


class Hotel(PuntoInt):

    prefijos = Util.conversor_txt_list(r"C:\Users\marco\Desktop\PythonDefinitivo\MatMaps\MatMaps_files\prefijos_hoteles.txt")

    def __init__(self, name=None, night_cost=None, adress=None, city=None, coordinates=None, capacity=None):
        super().__init__(name, adress, city, coordinates, capacity)
        self.night_cost = night_cost
        self.name = Util.name_creator(Hotel.prefijos, name)

    @property
    def night_cost(self):
        return self._night_cost

    @night_cost.setter
    def night_cost(self, night_cost=None):
        if night_cost is None:
            self._night_cost = random.randint(30, 200)
        else:
            assert type(night_cost) == int, "El precio ha de ser un número entero"
            self._night_cost = night_cost

    def __str__(self):
        cadena = str()
        cadena += "     " + self.name + "\n"
        cadena += "El coste por noche de este establecimiento es de " + str(self.night_cost) + "€. \n"
        return cadena


class CultureSite(PuntoInt):

    prefijos_culturales = Util.conversor_txt_list(r"C:\Users\marco\Desktop\PythonDefinitivo\MatMaps\MatMaps_files\prefijos_culturales.txt")

    def __init__(self, name=None, cost=None, visit_duration=None, adress=None, city=None, coordinates=None, capacity=None):
        super().__init__(name, adress, city, coordinates, capacity)
        self.cost = cost
        self.name = Util.name_creator(CultureSite.prefijos_culturales, name)
        self.visit_duration = visit_duration

    @property
    def visit_duration(self):
        return self._visit_duration

    @visit_duration.setter
    def visit_duration(self, time=None):
        if type(time) is int:
            self._visit_duration = time
        else:
            self._visit_duration = random.randint(5, 300)

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost=None):
        if type(cost) is int:
            self._cost = cost
        else:
            self._cost = random.randint(0, 40)

    def __str__(self):
        cad = str()

        cad += "    " + self.name + "\n"
        cad += "La visita a este lugar de interés cultural tiene un coste de " + str(self.cost) + "€. \n"
        cad += "Además, la visita tiene una duración aproximada de " + str(self.visit_duration) + " minutos, es decir, "
        cad += str(Util.minutes_to_hours(self.visit_duration)) + " horas.\n"

        return cad


class BusStop(PuntoInt):

    prefijo_bus = "Parada de bus"

    def __init__(self, name=None, bus_list=None, average_waiting_time=None, adress=None, city=None, coordinates=None,
                 capacity=None):
        super().__init__(name, adress, city, coordinates, capacity)
        self.average_waiting_time = average_waiting_time
        self.bus_list = bus_list
        self.name = Util.name_creator(BusStop.prefijo_bus, name)

    @property
    def average_waiting_time(self):
        return self._average_waiting_time

    @average_waiting_time.setter
    def average_waiting_time(self, average_waiting_time=None):
        if average_waiting_time is None:
            self._average_waiting_time = random.randint(5, 60)
        else:
            assert type(average_waiting_time) is int, "El tiempo debe de estar dado en minutos enteros. "
            self._average_waiting_time = average_waiting_time

    @property
    def bus_list(self):
        return self._bus_list

    @bus_list.setter
    def bus_list(self, bus_list=None):
        if bus_list is None:
            self._bus_list = list()
        else:
            assert type(bus_list) is list, "Bus_list debe ser una lista de líneas de bus. "
            self._bus_list = bus_list

    def add_bus(self, bus):
        self.bus_list.append(bus)

    def __str__(self):
        cad = str()
        cad += "    " + self.name + "\n"
        cad += "Las lineas de bus que pasan por esta parada son :"
        for bus in self.bus_list:
            cad += "\n " + bus
        cad += "\nEl tiempo medio de espera en esta parada es de " + str(self.average_waiting_time) + " minutos, es decir, "
        cad += str(Util.minutes_to_hours(self.average_waiting_time)) + " horas. \n"

        return cad


class TaxiStop(PuntoInt):

    prefijo = "Taxis"    # Variable de clase

    def __init__(self, name=None, telephone_number=None, average_waiting_time=None, adress=None, city=None,
                 coordinates=None, capacity=None):
        super().__init__(name, adress, city, coordinates, capacity)
        if type(name) is str or list:
            self.name = Util.name_creator(TaxiStop.prefijo, name)
        self.average_waiting_time = average_waiting_time
        self.telephone_number = telephone_number

    @property
    def average_waiting_time(self):
        return self._average_waiting_time

    @average_waiting_time.setter
    def average_waiting_time(self, average_waiting_time=None):
        if type(average_waiting_time) is int:
            self._average_waiting_time = average_waiting_time
        else:
            self._average_waiting_time = random.randint(5, 60)

    @property
    def telephone_number(self):
        return self._telephone_number

    @telephone_number.setter
    def telephone_number(self, number=None):
        if number is None:
            self._telephone_number = random.randint(100000000, 999999999)
        else:
            assert (type(number) is int) and (number in range(100000000, 999999999)), \
                "El número de telefono debe ser un entero de 9 cifras. "
            self._telephone_number = number

    def __str__(self):
        cad = str()
        cad += "    " + self.name + "\n"
        cad += "El numero de telefono para llamar a los taxis de esta ciudad es " + str(self.telephone_number) + ".\n"
        cad += "Los taxis suelen tardar una media de " + str(self.average_waiting_time) + " minutos en llegar. \n"
        return cad


class Airport(PuntoInt):

    prefijo = "Aeropuerto de"  # variable de clase
    nombres_default = Util.conversor_txt_list(r"C:\Users\marco\Desktop\PythonDefinitivo\MatMaps\MatMaps_files\aeropuertos.txt")

    def __init__(self, name=None, destinations=None, average_waiting_time=None, adress=None, city=None,
                 coordinates=None, capacity=None):
        super().__init__(name, adress, city, coordinates, capacity)

        if type(name) is str:
            self.name = Util.name_creator(Airport.prefijo, name)
        elif type(name) is list:
            self.name = Util.name_creator(Airport.prefijo, name)
        else:
            self.name = Util.name_creator(Airport.prefijo, Airport.nombres_default)

        self.average_waiting_time = average_waiting_time
        self.destinations = destinations

    @property
    def average_waiting_time(self):
        return self._average_waiting_time

    @average_waiting_time.setter
    def average_waiting_time(self, average_waiting_time=None):
        if average_waiting_time is None:
            self._average_waiting_time = random.randint(5, 60)
        else:
            assert type(average_waiting_time) is int, "El tiempo debe de estar dado en minutos enteros. "
            self._average_waiting_time = average_waiting_time

    @property
    def destinations(self):
        return self._destinations

    @destinations.setter
    def destinations(self, destinations=None):
        if destinations is None:
            self._destinations = dict()
        else:
            assert type(destinations) is dict, "El listado de destinos debe incluir el precio de cada viaje, " \
                                               "así como el tiempo medio de vuelo. "
            self._destinations = destinations

    def add_destination(self, destination, price: int, flight_duration: int):
        info = {'price': price, 'flight_duration': flight_duration}
        self.destinations[destination] = info

    def __str__(self):
        cad = str()
        cad += "    " + self.name + "\n"
        cad += "La lista de destinos desde este aeropuerto es: \n"
        for plane in self.destinations:
            cad += "    " + str(plane) + "\n"
        cad += "El tiempo medio de espera es de " + str(self.average_waiting_time) + " minutos, es decir, "
        cad += str(Util.minutes_to_hours(self.average_waiting_time)) + " horas.\n"

        return cad


class GasStation(PuntoInt):
    prefijo = "Gasolinera"  # variable de clase
    nombres_default = Util.conversor_txt_list(r"C:\Users\marco\Desktop\PythonDefinitivo\MatMaps\MatMaps_files\gasolineras.txt")

    def __init__(self, name=None, price=None, adress=None, city=None, coordinates=None, capacity=None):
        super().__init__(name, adress, city, coordinates, capacity)
        if type(name) is str:
            self.name = Util.name_creator(GasStation.prefijo, name)
        elif type(name) is list:
            self.name = Util.name_creator(GasStation.prefijo, name)
        else:
            self.name = Util.name_creator(GasStation.prefijo, GasStation.nombres_default)
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price=None):
        if price is None:
            self._price = random.randint(1, 2)
        else:
            assert type(price) is int, "El precio debe ser dado en enteros."
            self._price = price

    def __str__(self):
        cad = str()
        cad += "    " + self.name +"\n"
        cad += "El precio por litro de combustble es de " + str(self.price) + "€. \n"

        return cad
