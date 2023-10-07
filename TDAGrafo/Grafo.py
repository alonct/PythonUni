# Implementación del TDA Grafo con listas de adyacencia
from random import choice
import copy as cp


class Graph:
    class Vertex:
        __slots__ = '_name', '_adjacency_list'
        _name: str
        _adjacency_list: dict

        def __init__(self, iname, _adjacency_list=None):
            if _adjacency_list is None:
                _adjacency_list = {}
            self._name = iname
            self._adjacency_list = _adjacency_list

        def add_adjacent(self, vertex: str, peso=int):
            self._adjacency_list[vertex] = peso

        def remove_adjacent(self, vertex: str):
            assert vertex in self._adjacency_list.keys(), vertex + " no se encuentra en la lista de vertices adyacentes"
            self._adjacency_list.pop(vertex)

        def get_name(self):
            return self._name

        def get_adjacency_list(self):
            return self._adjacency_list

        def get_adjacency_list_keys(self):
            return self._adjacency_list.keys()

        def get_weight(self, vertex: str):
            assert vertex in self.get_adjacency_list_keys()
            return self.get_adjacency_list()[vertex]

    __slots__ = '_list_ref'
    _list_ref: dict

    def __init__(self):
        self._list_ref = {}

    def __len__(self):
        return len(self.get_vertex_list())

    def add_vertex(self, iname: str):
        self._list_ref[iname] = Graph.Vertex(iname)

    def remove_vertex(self, iname: str):
        assert iname in self.get_vertex_list(), "Vertex not in keys"
        if iname in self.get_vertex_list():
            self._list_ref.pop(iname)
            for vertex in self._list_ref.values():
                if iname in vertex.get_adjacency_list_keys():
                    vertex.get_adjacency_list().pop(iname)

    def add_edge(self, vertex1: str, vertex2: str, peso=0):
        assert vertex1 and vertex2 in self.get_vertex_list(), "Al menos uno de los vertices no existe"
        self._list_ref[vertex1].add_adjacent(vertex2, peso)
        self._list_ref[vertex2].add_adjacent(vertex1, peso)

    def remove_edge(self, vertex1: str, vertex2: str):
        assert vertex1 and vertex2 in self.get_vertex_list(), "Al menos uno de los vertices no existe"
        self._list_ref[vertex1].remove_adjacent(vertex2)
        self._list_ref[vertex2].remove_adjacent(vertex1)

    def get_vertex(self, iname: str) -> Vertex:
        return self._list_ref.get(iname)

    def is_connected(self, vertex1: str, vertex2: str) -> bool:
        if vertex1 == vertex2:
            return True
        else:
            abierto = list()
            closed = list()
            abierto.append(vertex1)
            while len(abierto) != 0:
                closed.append(abierto[0])
                abierto.pop(0)
                if closed[len(closed) - 1] == vertex2:
                    return True
                for element in self.get_adjacent_vertex(closed[len(closed) - 1]):
                    if (element not in closed) and (element not in abierto):
                        abierto.append(element)
            return False

    def get_adjacent_vertex(self, vertex: str):
        return self.get_vertex(vertex).get_adjacency_list_keys()

    def get_adjacent_vertex_in_list(self, vertex: str):
        adjacent = list()
        for element in self.get_adjacent_vertex(vertex):
            adjacent.append(element)
        return adjacent

    def get_vertex_list(self):
        return self._list_ref

    def get_min_distances(self, vertex: str) -> dict:
        """
            Given a vertex, returns de minimum distances between that vertex and the rest of nodes in the graph
        """
        assert vertex in self.get_vertex_list(), "This vertex does not exist within the graph"
        distances = dict()
        seen = list()
        not_seen = list()

        for key in self.get_vertex_list():
            not_seen.append(key)
            if self.is_connected(vertex, key) is False:
                distances[key] = -1
                seen.append(key)
                not_seen.remove(key)
            elif key in self.get_adjacent_vertex(vertex):
                distances[key] = self.get_vertex(vertex).get_weight(key)

            else:
                distances[key] = -1  # -1 represents an infinite distance

        distances.update({vertex: 0})  # distance to itself must be 0
        seen.append(vertex)
        not_seen.remove(vertex)

        while len(seen) != len(self):
            node = not_seen[0]

            for key in not_seen:  # looking for the minimum distance between the known distances
                if distances[key] != -1:
                    if (distances[node] > distances[key]) or (distances[node] == -1):
                        node = key

            seen.append(node)
            not_seen.remove(node)
            for key in self.get_adjacent_vertex(node):
                if (distances[key] > distances[node] + self.get_vertex(node).get_weight(key)) or (distances[key] == -1):
                    distances[key] = distances.get(node) + self.get_vertex(node).get_weight(key)

        return distances

    def get_min_distance_between_vertex(self, vertex1: str, vertex2: str):
        if self.is_connected(vertex1, vertex2) is False:
            return -1
        else:
            return self.get_min_distances(vertex1)[vertex2]

    def get_shortest_route(self, vertex1: str, vertex2: str) -> list:
        assert self.is_connected(vertex1, vertex2), "These two vertex are not connected"
        route = [vertex1]
        if vertex1 == vertex2:

            return route
        else:
            copy = Graph()
            for item in self.get_vertex_list().keys():
                copy._list_ref[item] = self.Vertex(item, cp.deepcopy(self._list_ref[item].get_adjacency_list()))
            adjacency_list = list()
            adjacency_list += self.get_adjacent_vertex_in_list(vertex1)
            next_stop = choice(adjacency_list)
            copy.remove_vertex(vertex1)

            for element in adjacency_list:
                if self.is_connected(element, vertex2):
                    if (copy.get_min_distance_between_vertex(element, vertex2) +
                        self.get_vertex(vertex1).get_weight(element)) <= \
                            (copy.get_min_distance_between_vertex(next_stop, vertex2) +
                             self.get_vertex(vertex1).get_weight(next_stop)):
                        next_stop = element
            print(route)
            return route + copy.get_shortest_route(next_stop, vertex2)


if __name__ == "__main__":
    grafo = Graph()
    for name in ['Madrid', 'Cartagena', 'Murcia', 'Barcelona', 'Ferrol']:
        grafo.add_vertex(name)

    grafo.add_edge('Cartagena', 'Murcia', 50)
    grafo.add_edge('Murcia', 'Madrid', 450)
    grafo.add_edge('Madrid', 'Barcelona', 600)
    grafo.add_edge('Madrid', 'Ferrol', 550)
    grafo.add_edge('Cartagena', 'Ferrol', 1000)

    print("-" * 10)
    print(grafo.get_min_distance_between_vertex('Cartagena', 'Ferrol'))
    print(grafo.get_shortest_route('Cartagena', 'Ferrol'))
    print("-" * 10)

    print(grafo.is_connected('Barcelona', 'Ferrol'))

    print(grafo.get_min_distance_between_vertex('Barcelona', 'Ferrol'))
    print(grafo.get_shortest_route('Barcelona', 'Ferrol'))
