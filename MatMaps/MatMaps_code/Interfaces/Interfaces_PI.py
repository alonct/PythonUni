from abc import ABC, abstractmethod


class IService(ABC):

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is IService:
            return hasattr(subclass, 'charge') and callable(subclass.charge)
        else:
            return NotImplemented

    @abstractmethod
    def charge(self):
        pass
