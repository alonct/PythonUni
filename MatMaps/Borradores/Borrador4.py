import random
from MatMaps.MatMaps_code.Extras.Herramientas import Util


def main():
    var = r"C:\Users\marco\Desktop\PythonDefinitivo\MatMaps\MatMaps_files\Lista_nombres_lugares.txt"
    lista = Util.conversor_mejorado(var)
    lista2 = Util.conversor_txt_list(var)
    print(lista)
    print(lista2)


if __name__ == "__main__":
    main()
