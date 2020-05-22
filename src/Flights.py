class Flights:

    def __init__(self):
        self.Destination = []
        self.Passengers = 0
        self.Code = []
        self.Preu = []
        

    def addPassengers(self,passengers):
        self.Passengers += passengers

    def addDestination(self, destination):
        listaux=[]
        if type(destination) == str:
            listaux.append(destination)
        else:
            listaux = destination
        for x,i in enumerate(listaux):
            self.Code.append(self.getCodiVol(destination, self.Passengers))
            self.Destination.append(listaux[x])
            self.Preu.append(self.getPreuVol(self.Code[-1]))


    def remDestination(self, destination):
        if destination in self.Destination:
            index = self.Destination.index(destination)
            self.Destination.pop(index)
            self.Preu.pop(index)
            self.Code.pop(index)

    def get_always_true():
        return False

    def getPassengers(self):
        return self.Passengers

    def getDestination(self):
        return self.Destination

    def getCode(self):
        return self.Code

    def getPreu(self):
        return self.Preu
            
            
    def getTotalToPay(self):
        
        Total_Pay = 0
     
        for i in self.Preu:
            Total_Pay = Total_Pay + i
            
        Total_Pay = Total_Pay * self.Passengers
        return Total_Pay
            
    ##dummy function API skyscanner returns codi vol depenent numero de passatgers i destinació,
    ##buscarà vol més barat
    def getCodiVol(self, destination, passenger):
        codi = 0
        return codi
    
    ##dummy function API skyscanner returns preu vol depenens el seu codi
    def getPreuVol(self, codivol):
        return 0

    