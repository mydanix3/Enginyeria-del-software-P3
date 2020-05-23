class PaymentData:
    
    def __init__(self):
        self.CardType = ""
        self.Money = 0
        self.SecurityCode = ""
        self.OwnerName = ""
        self.CardNum = ""
        
    def SelectTargeta(self, targeta):
        self.CardType = targeta
        
    def SetImport(self, importe):
        self.Money = importe
        
    def DadesTarjeta(self, nomtitular, numtargeta, codiseguretat):
         self.SecurityCode = codiseguretat
         self.OwnerName = nomtitular
         self.CardNum= numtargeta

    def GetTargeta(self):
        return self.CardType