# Student Number: 251264939
# Name: Numan Salahuddin

from Flight import *  # we import * from Flight
from Airport import *  # we import * from Airport


class Aviation:  # Adding Aviation class initializing objects from Airport.py
    def __init__(self):
        self._allAirports = []
        self._allFlights = {}
        self._allCountries = {}

    def getAllAirports(self):
        return self._allAirports

    def getAllFlights(self):
        return self._allFlights

    def getAllCountries(self):
        return self._allCountries

    def setAllAirports(self, airports):
        self._allAirports = airports

    def setAllFlights(self, flights):
        self._allFlights = flights

    def setAllCountries(self, countries):
        self._allCountries = countries

    def loadData(self, airportFile, flightFile, countriesFile):
        # we create a function for airports, flights and countries
        try:
            self._allAirports = []  # create an empty list for all airports
            self._allFlights = {}  # create an empty dictionary for all flights
            self._allCountries = {}  # create an empty dictionary for all countries
            with open(countriesFile, "r", encoding='utf8') as f:
                for line in f:
                    data = line.strip().split(',')
                    country = data[0].strip()
                    continent = data[1].strip()
                    self._allCountries[country] = continent

            with open(airportFile, "r", encoding='utf8') as f:
                for line in f:
                    data = line.strip().split(',')

                    code = data[0].strip()
                    name = data[1].strip()
                    city = data[2].strip()

                    airport = Airport(code, city, name)
                    self._allAirports.append(airport)

            with open(flightFile, "r", encoding='utf8') as f:
                for line in f:
                    data = line.strip().split(',')
                    flightNo = data[0].strip()
                    originCode = data[1].strip()
                    destCode = data[2].strip()
                    flight = Flight(flightNo, self.getAirportByCode(originCode), self.getAirportByCode(destCode))
                    try:
                        self._allFlights[originCode].append(flight)
                    except:
                        self._allFlights[originCode] = [flight]

            return True
        except:
            return False

    def getAirportByCode(self, code):  # we create another function for Airport codes
        for airport in self._allAirports:
            if airport.getCode() == code:
                return airport

    def findAllCityFlights(self, city):  # This function is for the Cities where the flights are available
        flights = []
        for flight_list in self._allFlights.values():
            for flight in flight_list:
                if (
                        flight.getOrigin().getCity() == city or flight.getDestination().getCity() == city) and flight not in flights:
                    flights.append(flight)
        return flights

    def findFlightByNo(self, flightNo):  # this function is for the countries where the flights are located
        for flight_list in self._allFlights.values():
            for flight in flight_list:
                if flight.getFlightNumber() == flightNo:
                    return flight
        return -1

    def findAllCountryFlights(self, country):  # this function is for the countries where the flights are located
        flights = []
        for flight_list in self._allFlights.values():
            for flight in flight_list:
                if (
                        flight.getOrigin().getCountry() == country or flight.getDestination().getCountry() == country) and flight not in flights:
                    flights.append(flight)
        return flights

    def findFlightBetween(self, origAirport, destAirport):
        # check if there is a single-hop connecting flight from origAirport to destAirport.
        for flight in self._allFlights.get(origAirport.getCode(), []):
            if flight.getDestination().getCode() == destAirport.getCode():
                return f"Direct Flight ({flight.getFlightNumber()}): {origAirport.getCode()} to {destAirport.getCode()}"

        connectingAirports = set()
        for flight1 in self._allFlights.get(origAirport.getCode(), []):
            for flight2 in self._allFlights.get(flight1.getDestination().getCode(), []):
                if flight2.getDestination().getCode() == destAirport.getCode():
                    connectingAirports.add(flight1.getDestination().getCode())
        if connectingAirports == set():
            return -1
        return connectingAirports

    def findReturnFlight(self, firstFlight):  # Finds the returning flights
        if firstFlight == -1:
            return -1

        dest = firstFlight.getOrigin()
        orig = firstFlight.getDestination()

        for flight in self._allFlights.get(orig.getCode(), []):
            if flight.getDestination().getCode() == dest.getCode():
                return flight
        return -1

    def findFlightsAcross(self, ocean):  # Finds flights across the continent.
        green = ['North America', 'South America']
        red = ['Asia', 'Australia']
        blue = ['Europe', 'Africa']
        flightsx = []
        if ocean.lower() == "atlantic":
            for j in self._allFlights.values():
                for i in j:
                    if (self._allCountries[i.getOrigin().getCountry()] in green and self._allCountries[
                        i.getDestination().getCountry()] in blue) or (
                            self._allCountries[i.getOrigin().getCountry()] in blue and self._allCountries[
                        i.getDestination().getCountry()] in green):
                        flightsx.append(i.getFlightNumber())
        elif ocean.lower() == "pacific":
            for j in self._allFlights.values():
                for i in j:
                    if (self._allCountries[i.getOrigin().getCountry()] in green and self._allCountries[
                        i.getDestination().getCountry()] in red) or (
                            self._allCountries[i.getOrigin().getCountry()] in red and self._allCountries[
                        i.getDestination().getCountry()] in green):
                        flightsx.append(i.getFlightNumber())

        return set(flightsx)