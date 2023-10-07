import random


class Util:

    @staticmethod
    def duration(distance: float, speed: float):
        return distance / speed

    @staticmethod
    def hours_to_minutes(hours: float):
        horas = int(hours // 1)
        minutos_extras = int((60 * (hours % 1))//1)
        return horas + minutos_extras

    @staticmethod
    def minutes_to_hours(minutes: int) -> float:
        return (((float(minutes)/60)*100) // 1)/100

    @staticmethod
    def conversor_txt_list(txt_file):
        with open(txt_file, 'r', encoding='utf-8-sig') as f:
            lineas = [linea.split() for linea in f]
        return lineas

    @staticmethod
    def conversor_mejorado(txt_file):
        """
    Devuelve una lista de str, y no una lista de listas como hace el otro conversor
        """
        lista = Util.conversor_txt_list(txt_file)
        lista2 = list()
        for element in lista:
            lista2.append(Util.list_to_string(element))
        return lista2

    @staticmethod
    def list_to_string(lista: list):
        string = str()
        for element in lista:
            string += " " + str(element)
        string = string[1:]
        string.lstrip("ï»¿")
        string.rstrip(" ")
        return string

    @staticmethod
    def name_creator(prefijos=None, nombre=None):
        name = str()
        if prefijos is None:
            pass
        else:
            if type(prefijos) is str:
                name += prefijos
            elif type(prefijos) is list:
                name += Util.list_to_string(random.choice(prefijos))
            else:
                name += "Random"
        if nombre is None:
            if prefijos is None:
                name += "No name"
            else:
                pass
        else:
            if type(nombre) is str:
                name += " " + nombre
            elif type(nombre) is list:
                name += Util.list_to_string(random.choice(nombre))
            else:
                pass
        return name

    @staticmethod
    def randint2(var1: int, var2: int):
        """
        Método para generar un número entero aleatorio entre dos enteros dados sin importar el orden de introducción de
        parámetros
        :param var1: entero
        :param var2: entero
        :return: entero
        """
        if var1 <= var2:
            return random.randint(var1, var2)
        else:
            return random.randint(var2, var1)
