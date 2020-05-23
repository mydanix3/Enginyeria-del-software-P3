from src.Bank import Bank
from src.Booking import Booking
from src.Cars import Cars
from src.Flights import Flights
from src.Hotels import Hotels
from src.PaymentData import PaymentData
from src.Rentalcars import Rentalcars
from src.Skyscanner import Skyscanner
from src.User import User

class Reserva:

    def __init__(self):
        self.bank = Bank()
        self.booking = Booking()
        self.cars = Cars()
        self.flights = Flights()
        self.hotels = Hotels()
        self.paymentdata = PaymentData()
        self.rentalcars = Rentalcars()
        self.skyscanner = Skyscanner()
        self.user = User()

    def getPreuTotal(self):
        return self.getPreuFlights() + self.getPreuHotels() + self.preuFinal()

    #Clase Bank
    def do_payment(self):
        return self.bank.do_payment(self.user, self.paymentdata)

    #Clase Booking
    def confirm_reserve_Hotels(self) -> bool:
        b = self.booking.confirm_reserve(self.user, self.hotels)

        if(b):
            print("la reserva del hotel se ha realizado correctamente")
        else:
            print("La reserva de los hoteles ha fallado por algún motivo.")

        return b

    #Clase Rentalcars
    def confirm_reserve_cotxes(self) -> bool:
        b = self.rentalcars.confirm_reserve(self.user, self.cars)

        if(b):
            print("la reserva del coche se ha realizado correctamente")
        else:
            print("La reserva de los coche ha fallado por algún motivo.")

        return b


    #Clase Skyscanner
    def confirm_reserve_vols(self) -> bool:
        return self.skyscanner.confirm_reserve(self.user, self.flights)


    #Clase User
    def DadesUsuari(self,name,dni,DirPostal,phonenumber,email):
        self.user.DadesUsuari(name, dni, DirPostal, phonenumber, email)


    #Clase Cars
    def getPreuCars(self):
        return self.cars.getPreu()

    def addCars(self, code,marca,destination,dias,preu):
        self.cars.addCar(code,marca,destination,dias,preu,self.flights.getPassengers())

    def removeCars(self, code):
        self.cars.removeCar(code)


    #Clase Flights
    def addPassengers(self,passengers):
        self.flights.addPassengers(passengers)
        self.hotels.addGuests(passengers)

    def addDestination(self, lista):
        self.flights.addDestination(lista)

    def remDestination(self, destination):
        self.flights.remDestination(destination)

    def getPreuFlights(self):
        return self.flights.getTotalToPay()

    def getCodiVol(self, destination, passenger):
        return self.flights.getCodiVol(destination, passenger)

    def getPassengers(self):
        return self.flights.getPassengers()

    #Clase Hotels
    def getPreuHotels(self):
        return self.hotels.getPreu()

    def addHotel(self, name, days, code, preu):
        self.hotels.addHotel(name, days, code, preu)

    def remHotel(self, code):
        self.hotels.remHotel(code)


    #Clase PaymentData
    def SelectTargeta(self, targeta):
        self.paymentdata.SelectTargeta(targeta)

    def SetImport(self, importe):
        self.paymentdata.SetImport(importe)

    def DadesTarjeta(self, nomtitular, numtargeta, codiseguretat):
        self.paymentdata.DadesTarjeta(nomtitular, numtargeta, codiseguretat)

    def GetTargeta(self):
        return self.paymentdata.GetTargeta()


    #Clase Reserva
