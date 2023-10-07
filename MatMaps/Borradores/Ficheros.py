import json
import json as js

import numpy
import numpy as np


def prueba():
    f = open("../MatMaps_files/Lista_nombres_lugares.txt", 'r')
    text = f.readlines()

    lista_nombres = [(line.strip()).split() for line in text]

    """for line in text:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        lista_nombres.append(line_list)"""

    lista_nombres.pop(0)
    print(lista_nombres)
    lista_final = list()
    for item in lista_nombres:
        for string in item:
            lista_final.append(string)

    print(lista_final)


def prueba_2():
    with open("MatMaps_code/Engine/Apuntes_geograficos_mapa.txt", "r") as f:
        ciudades = js.load(f)
        print(ciudades)


if __name__ == '__main__':
    prueba()
    prueba_2()
