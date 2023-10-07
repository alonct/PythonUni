from TDAGrafo.Grafo import Graph
from MatMaps.MatMaps_code.Extras.text_manager import TextManager as TM


class MatMapsEngine:

    def __init__(self):
        self._map = Graph
        self._geo_info_ref = "Apuntes_geograficos_mapa.txt"
        self._text_manager = TM()
        self._geo_info_dict = self._text_manager.json_reader(self._geo_info_ref)
        print(self._geo_info_dict)

    def map_builder(self):
        pass

    def player_location(self, player: str) -> str:
        """
        Dado un jugador devuelve el lugar donde se encuentra en ese momento
        """
    pass


def prueba():
    prueba = MatMapsEngine()


if __name__ == "__main__":
    prueba()
