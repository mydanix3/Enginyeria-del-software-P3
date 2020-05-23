class Flights:

    def __init__(self):
        self.Destination = []
        self.Passengers = 0
        self.Code = []
        self.Preu = []
        self.Dias = []


    def addPassengers(self,passengers):
        self.Passengers += passengers

    def addDestination(self, destination, code, dias, preu):
            self.Code.append(code)
            self.Destination.append(destination)
            self.Preu.append(preu)
            self.Dias.append(dias)

    def remDestination(self, code):
        if code in self.Code:
            index = self.Code.index(code)
            self.Destination.pop(index)
            self.Preu.pop(index)
            self.Code.pop(index)
            self.Dias.pop(index)

    def getPassengers(self):
        return self.Passengers
    
    def getDestination(self):
        return self.Destination
    
    def getCode(self):
        return self.Code
    
    
    def getPreuFlights(self):

        Total_Pay = 0

        for i in self.Preu:
            Total_Pay = Total_Pay + i

        Total_Pay = Total_Pay * self.Passengers
        return Total_Pay
