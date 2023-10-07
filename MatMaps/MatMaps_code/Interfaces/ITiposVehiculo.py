from abc import ABC, abstractmethod


class IElectricVehicle(ABC):

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is IElectricVehicle:
            return (hasattr(subclass, 'recharge_vehicle')
                    and callable(subclass.recharge_vehicle))
        else:
            return NotImplemented

    @abstractmethod
    def recharge_vehicle(self):
        """
        Para recargar la bateria de un vehículo eléctrico es necesario usar este método que dictaminará
        cosas como el tiempo que habrá que esperar para una carga completa etc...
        """
        pass


class IGasVehicle(ABC):

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is IGasVehicle:
            return (hasattr(subclass, 'refill_gas_tank')
                    and callable(subclass.refill_gas_tank))
        else:
            return NotImplemented

    @abstractmethod
    def refill_gas_tank(self):
        """
        método para rellenar el depósito de combustible
        """
        pass
