from typing import Optional


class List:

    class Node:
        __slots__ = '_value', '_next'
        _value: object
        _next: Optional['Node']

        """def __init__(self, value: object, next = List.Node):
            self._value = value
            self._next = next"""

        def get_value(self):
            return self._value

        def set_value(self, value: object):
            self._value = value

        def get_next(self):
            return self._next

        """def set_next(self, next: 'Node'):"""

    __slots__ = '_list', '_first_node_ref'
    _list: list[[Node]]
    _first_node_ref: Node

    def __init__(self):
        self._list = list()

    def get_list(self):
        return self._list

    def get_first_node(self):
        return self._first_node_ref

    def set_first_node(self, node: Node):
        self._first_node_ref = node

    def __len__(self) -> int:
        return len(self.get_list())

    """def __contains__(self, value):
        actual = self.get_first_node()
        while actual is not None or actual."""