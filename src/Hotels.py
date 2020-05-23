class Hotels:

    def __init__(self):
        self.Code = []
        self.Name = []
        self.Guests = 0
        self.Rooms = 0
        self.Days = []
        self.Preu = []


    def addGuests(self, guests):
        self.Guests = self.Guests + guests

        self.Rooms = self.Guests//3


    def addHotel(self, name, days, code, preu):
        self.Name.append(name)
        self.Days.append(days)
        self.Code.append(code)
        self.Preu.append(preu)


    def remHotel(self, code):
        index = self.Code.index(code)
        self.Code.pop(index)
        self.Name.pop(index)
        self.Days.pop(index)
        self.Preu.pop(index)


    def getPreu(self):
        preu = 0
        for index, i in enumerate(self.Preu):
                preu = preu + i*self.Days[index]*self.Guests

        return preu