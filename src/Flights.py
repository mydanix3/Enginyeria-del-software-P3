class Flights:

    def __init__(self,destino,gente):
        self.Destination = destino
        self.Passengers = gente
        if not destino:
            self.Code = []
        else:
            self.Code = getCodiVol(destino)

    def addDestination(destination):
        self.Code.append(getCodiVol(destination))
        self.Destination.appen(destination)

    ##dummy function API skyscanner
    def getCodiVol(destination)
        codi = 0
        return codi
