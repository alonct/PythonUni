from MatMaps.MatMaps_code.Extras.Herramientas import Util


def main(txt):
    txtref = txt
    lista = Util.conversor_txt_list(txtref)
    for element in lista:
        print(Util.list_to_string(element))


if __name__ == "__main__":

    main(r"C:\Users\marco\Desktop\PythonDefinitivo\MatMaps\MatMaps_files\lista_bebidas.txt")
    main(r'C:\Users\marco\Desktop\PythonDefinitivo\MatMaps\MatMaps_files\lista_comidas.txt')
