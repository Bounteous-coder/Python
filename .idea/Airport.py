class Airport:
    def __init__(self, code, city, country, continent=None) -> None:  # initializes object
        self._code = code
        self._city = city
        self._country = country
        self._continent = continent

    def __repr__(self) -> str:  # will return a string that prints the code, city and country of object
        return f"{self._code} ({self._city}, {self._country})"

    def getCode(self) -> str:  # returns code of object
        return self._code

    def getCity(self) -> str:  # returns city of object
        return self._city

    def getCountry(self) -> str:  # returns country of object
        return self._country

    def getContninent(self) -> str:  # returns country of object
        return self._continent

    def setCity(self, city) -> None:  # sets city of object to parameter
        self._city = city

    def setCountry(self, country) -> None:  # sets country of object to parameter
        self._country = country

    def setContinent(self, continent) -> None:  # sets continent of object to parameter
        self._continent = continent
