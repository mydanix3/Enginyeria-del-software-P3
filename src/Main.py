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

    #Clase Bank
    def do_payment(self, user: User, payment_data: PaymentData):
        return self.bank.do_payment(user, payment_data)

    #Clase Booking
    def confirm_reserve(self, user: User, hotels: Hotels) -> bool:
        return self.booking.confirm_reserve(user,hotels)

    #Clase Cars


    # Clase Flights
    def addPassengers(self,passengers):
        self.flights.addPassengers(passengers)

    def addDestination(self, lista):
        self.flights.addDestination(lista)

    def remDestination(self, destination):
        self.flights.remDestination(destination)

    def getTotalToPay(self):
        return self.flights.getTotalToPay()

    def getCodiVol(self, destination, passenger):
        return self.flights.getCodiVol(destination, passenger)

    def getPreuVol(self, codivol):
        self.flights.getPreuVol(codivol)

    def get_always_true(self):
        return self.flights.get_always_true()

    def getPassengers(self):
        return self.flights.getPassengers()

    def getDestination(self):
        return self.flights.getDestination()

    def getCode(self):
        return self.flights.getCode()

    def getPreu(self):
        return self.flights.getPreu()


    #Clase Hotels

    #Clase PaymentData
    def SelectTargeta(self, targeta):
        self.paymentdata.SelectTargeta(targeta)

    def SetImport(self, importe):
        self.paymentdata.SetImport(importe)

    def DadesTarjeta(self, nomtitular, numtargeta, codiseguretat):
        self.paymentdata.DadesTarjeta(nomtitular, numtargeta, codiseguretat)

    #Clase Rentalcars
    def confirm_reserve(self, user: User, cars: Cars) -> bool:
        return self.rentalcars.confirm_reserve(user, cars)

    #Clase Skyscanner
    def confirm_reserve(self, user: User, flights: Flights) -> bool:
        return self.skyscanner.confirm_reserve(user, flights)

    #Clase User
    def DadesUsuari(self,name,dni,DirPostal,phonenumber,email):
        self.user.DadesUsuari(name, dni, DirPostal, phonenumber, email)

    #Clase Reserva

