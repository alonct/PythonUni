from abc import ABC, abstractmethod


class ICapital(ABC):
    """
    ICapital es una interfaz que incluye metodos relacionados con ser la capital de un país

    """

    @classmethod
    def __subclasshook__(cls, subclass):

        if cls is ICapital:
            return (hasattr(subclass, 'pasar_aduanas')
                    and callable(subclass.pasar_aduanas))
        else:
            return NotImplemented

    @abstractmethod
    def pasar_aduanas(self):
        """
        Método necesario para poder entrar a un nuevo país. Este podrá ser diferente dependiendo del país en cuestion.
        """
        pass
    
