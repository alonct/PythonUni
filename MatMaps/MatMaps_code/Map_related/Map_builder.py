from TDAGrafo.Grafo import Graph
from MatMaps.MatMaps_code.Extras.Herramientas import Util
import random


class MapBuilder:

    num_ciudades = (12, 17)  # determina el número de ciudades total
    num_pts_interes = (2, 7)  # determinan el número mínimo y máximo de puntos de interes en el mapa
    ref = r"C:\Users\marco\Desktop\PythonDefinitivo\MatMaps\MatMaps_files\Lista_nombres_lugares.txt"
    names_default = Util.conversor_mejorado(ref)

    def __init__(self):
        pass

    @classmethod
    def create_map(cls, cities=None, num_pts_interes=None):
        """
        A partir de los parámetros (o no) dados se crea un nuevo mapa
        """
        num_ciudades = int()
        puntos_interes = int()
        mapa = Graph()
        names = [str]

        if type(cities) is int:
            num_ciudades = cities
            names = cls.names_default
        elif type(cities) is list:
            num_ciudades = len(cities)
            names = cities
        else:
            ciudades = random.randint(cls.num_ciudades[0], cls.num_ciudades[1])
            names = cls.names_default

        if type(num_pts_interes) is tuple[int, int]:
            puntos_interes = Util.randint2(num_pts_interes[0], num_pts_interes[1])
        elif type(num_pts_interes) is int:
            puntos_interes = num_pts_interes
        else:
            puntos_interes = Util.randint2(cls.num_pts_interes[0], cls.num_pts_interes[1])

        if len(names) != 0:
            for city in names:
                mapa.add_vertex(city)
        else:
            for i in range(num_ciudades):
                nombre = random.choice(names)
                names.remove(nombre)
                mapa.add_vertex(nombre)


"""    @property
    def num_ciudades(self):
        return self._num_ciudades

    @num_ciudades.setter
    def num_ciudades(self, var: int):
        self._num_ciudades = var"""

"""
    @property
    def num_pts_interes(self):
        return self._num_pts_interes

    @num_pts_interes.setter
    def num_pts_interes(self, var: int):
        self._num_pts_interes = var"""
