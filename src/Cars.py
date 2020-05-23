class Cars:

    def __init__(self):
        self.Code = []
        self.Marca = []
        self.LlocRecollida = []
        self.DuradaReserva = []
        self.Preus = []
        self.NumeroCotxes = []

    def addCar(self, _code,_marca,_destination,_dias,_preu,_personas):
        self.Code.append(_code)
        self.Marca.append(_marca)
        self.DuradaReserva.append(_dias)
        self.LlocRecollida.append(_destination)
        self.Preus.append(_preu)
        self.NumeroCotxes.append(_personas//4)

    def removeCar(self,_code):
        if _code in self.Code:
            index = self.Code.index(_code)
            self.Code.pop(index)
            self.Marca.pop(index)
            self.DuradaReserva.pop(index)
            self.LlocRecollida.pop(index)
            self.Preus.pop(index)

    def getPreu(self):
        preu = 0
        for index, i in enumerate(self.Preus):
                preu = i * self.NumeroCotxes[index]*self.DuradaReserva[index]
        return preu
