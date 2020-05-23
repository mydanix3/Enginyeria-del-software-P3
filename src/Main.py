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
        self.numero_de_vegades_pagament_fallat = 0
        self.numero_de_vegades_confirmar_vols_fallat = 0
        self.numero_de_vegades_confirmar_hotels_fallat = 0
        self.numero_de_vegades_confirmar_cotxes_fallat = 0

    def getPreuTotal(self):
        return self.getPreuFlights() + self.getPreuHotels() + self.getPreuCars()

    #Clase Bank
    def do_payment(self):
        
        if self.numero_de_vegades_pagament_fallat == 3:
            
            self.numero_de_vegades_pagament_fallat = 0
            print("Cancelant el carregament del pagament")
            return 2
                      
        
        b = self.bank.do_payment(self.user, self.paymentdata)
        
        if(b):
            print("El pagament s'ha realitzat correctament.")
            self.numero_de_vegades_pagament_fallat = 0
            return 0
        else:
            self.numero_de_vegades_pagament_fallat = self.numero_de_vegades_pagament_fallat + 1
            print("Error al fer el pagament, introdueixi les dades un altre cop.")
            return 1
            
    
    
    #Clase Booking
    def confirm_reserve_Hotels(self):
        
        if self.numero_de_vegades_confirmar_hotels_fallat == 3:
            self.numero_de_vegades_confirmar_hotels_fallat = 0
            print("cancelant el carregament de la reserva dels hotels")
            return 2
            
        b = self.booking.confirm_reserve(self.user, self.hotels)

        if(b):
            self.numero_de_vegades_confirmar_hotels_fallat = 0
            print("La reserva dels hotels s'ha realitzat correctament")
            return 0
        else:
            self.numero_de_vegades_confirmar_hotels_fallat = self.numero_de_vegades_confirmar_hotels_fallat + 1
            print("La reserva dels hotels ha fallat per algún motiu.")
            return 1


    #Clase Rentalcars
    def confirm_reserve_cotxes(self):
        
        if self.numero_de_vegades_confirmar_cotxes_fallat == 3:
            self.numero_de_vegades_confirmar_cotxes_fallat = 0
            print("cancelant el carregament de la reserva dels cotxes")
            return 2
        
        b = self.rentalcars.confirm_reserve(self.user, self.cars)
        

        if(b):
            self.numero_de_vegades_confirmar_cotxes_fallat = 0
            print("La reserva dels cotxes s'ha realitzat correctament")
            return 0
        else:
            self.numero_de_vegades_confirmar_cotxes_fallat = self.numero_de_vegades_confirmar_cotxes_fallat + 1
            print("La reserva dels cotxes ha fallat per algún motiu.")
            return 1



    #Clase Skyscanner
    def confirm_reserve_vols(self):
        
        if self.numero_de_vegades_confirmar_vols_fallat == 3:
            
           self.numero_de_vegades_confirmar_vols_fallat = 0
           print("cancelant el carregament de la reserva dels vols")
           return 2
       
        
        b = self.skyscanner.confirm_reserve(self.user, self.flights)
    
        if(b):
            self.numero_de_vegades_confirmar_vols_fallat = 0
            print("La reserva dels vols s'ha realitzat correctament")
            return 0
        else:
            self.numero_de_vegades_confirmar_vols_fallat = self.numero_de_vegades_confirmar_vols_fallat + 1
            print("La reserva dels vols ha fallat per algún motiu.")
            return 1
            
            


    #Clase User
    def DadesUsuari(self,name,dni,DirPostal,phonenumber,email):
        self.user.DadesUsuari(name, dni, DirPostal, phonenumber, email)


    #Clase Cars
    def getPreuCars(self):
        return self.cars.getPreu()

    def addCar(self, code,marca,destination,dias,preu):
        self.cars.addCar(code,marca,destination,dias,preu,self.flights.getPassengers())

    def removeCar(self, code):
        self.cars.removeCar(code)


    #Clase Flights
    def addPassengers(self,passengers):
        self.flights.addPassengers(passengers)
        self.hotels.addGuests(passengers)

    def addDestination(self, destination, code, dias, preu):
        self.flights.addDestination(destination, code, dias, preu)

    def remDestination(self, code):
        self.flights.remDestination(code)

    def getPreuFlights(self):
        return self.flights.getPreuFlights()

    def getPassengers(self):
        return self.flights.getPassengers()
    
    def getDestination(self):
        return self.flights.getDestination()
    
    def getCode(self):
        return self.flights.getCode()


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
