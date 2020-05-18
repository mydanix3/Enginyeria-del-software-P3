class Flights:

    def get_always_true():
        return False
    
    def getPassengers(self):
        return self.Passengers
    
    # def __init__(self):
    #     pass

    def __init__(self,destino,gente):
        self.Destination = destino
        self.Passengers = gente
        self.Code = []
        self.Preu = []
        if destino:
            for i in destino:
                self.Code.append(self.getCodiVol(i,  self.Passengers))
                self.Preu.append(self.getPreuVol(self.Code[-1]))
        
        
    def addDestination(self, destination):
        self.Code.append(self.getCodiVol(destination, self.Passengers))
        self.Destination.append(destination)
        self.Preu.append(self.getPreuVol(self.Code[-1]))


    def remDestination(self, destination):
        if destination in self.Destination:
            index = self.Destination.index(destination)
            self.Destination.pop(index)
            self.Preu.pop(index)
            self.Code.pop(index)
            
            
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

    