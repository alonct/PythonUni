class Vehicle:

    def __init__(self):

        self.capacity = float()     # maxim weight
        self.passengers = int()    # maxim number of passengers
        self.speed = int()    # km/hour
        self.autonomy = float()     # number of km
        self.owner = str()      # propietario

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, var: float):
        self._capacity = var

    @property
    def passengers(self):
        return self._passengers

    @passengers.setter
    def passengers(self, var: int):
        self._passengers = var

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, var: int):
        self._speed = var

    @property
    def autonomy(self):
        return self._autonomy

    @autonomy.setter
    def autonomy(self, var: float):
        self._autonomy = var

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, var: str):
        self._owner = var
