from src import Bank, Booking, Cars, Flights, Hotels, PaymentData, Rentalcars, Skyscanner, User

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
        self.bank.do_payment(user, payment_data)

    #Clase Booking
    def confirm_reserve(self, user: User, hotels: Hotels) -> bool:
        self.booking.confirm_reserve(user,hotels)

    #Clase Cars


    # Clase Flights
    def addDestination(self, lista):
        self.flights.add(self.lista)

    def remDestination(self, destination):
        self.flights.remDestination(self, destination)

    def getTotalToPay(self):
        self.flights.getTotalToPay(self)

    def getCodiVol(self, destination, passenger):
        self.flights.getCodiVol(self, destination, passenger)

    def getPreuVol(self, codivol):
        self.flights.getPreuVol(self, codivol)

    #Clase Hotels

    #Clase PaymentData
    def SelectTargeta(self, targeta):
        self.paymentdata.SelectTargeta(self,targeta)

    def SetImport(self, importe):
        self.paymentdata.SetImport(self.importe)

    def DadesTarjeta(self, nomtitular, numtargeta, codiseguretat):
        self.paymentdata.DadesTarjeta(self, nomtitular, numtargeta, codiseguretat)

    #Clase Rentalcars
    def confirm_reserve(self, user: User, cars: Cars) -> bool:
        self.rentalcars.confirm_reserve(self, user, cars)

    #Clase Skyscanner
    def confirm_reserve(self, user: User, flights: Flights) -> bool:
        self.skyscanner.confirm_reserve(self, user, flights)

    #Clase User
    def DadesUsuari(self,name,dni,DirPostal,phonenumber,email):
        self.user.DadesUsuari(self, name, dni, DirPostal, phonenumber, email)

    #Clase Reserva

