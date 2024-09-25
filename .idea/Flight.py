from Airport import *


class Flight:
    def __init__(self, flightNo, origin, destination) -> None:  # imports all data from Airport.py
        if not isinstance(origin, Airport) or not isinstance(destination, Airport):
            raise TypeError("The origin and destination must be Airport objects")
            return
        self._flightNo = flightNo
        self._origin = origin
        self._destination = destination

    def __repr__(self) -> str:  # returns string that contains flightNo, origin, destination and flightType
        return "Flight({}): {} -> {} [{}]".format(self._flightNo, self._origin.getCity(), self._destination.getCity(),
                                                  'domestic' if self.isDomesticFlight() else 'international')

    def __eq__(self, other: object) -> bool:  # checks if 2 flight objects have equal origins and destination
        if isinstance(other, Flight):
            return (self._origin == other._origin and self._destination == other._destination)
        else:
            return False

    def getFlightNumber(self) -> str:  # returns flightNo of object
        return self._flightNo

    def getOrigin(self) -> str:  # returns Origin of object
        return self._origin

    def getDestination(self) -> str:  # returns destination of object
        return self._destination

    def isDomesticFlight(self) -> bool:  # returns domestic flights of object to parameter
        return self._origin.getCountry() == self._destination.getCountry()

    def setOrigin(self, origin) -> None:  # sets origin of object to parameter
        self._origin = origin

    def setDestination(self, destination) -> None:  # sets destination of object to parameter
        self._destination = destination

