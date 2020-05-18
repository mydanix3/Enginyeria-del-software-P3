class PaymentData:
    
    def __init__(self):
        pass
        
    def SelectTargeta(self, targeta):
        self.CardType = targeta
        
    def SetImport(self, importe):
        self.Money = importe
        
    def DadesTarjeta(self, nomtitular, numtargeta, codiseguretat):
         self.SecurityCode = codiseguretat
         self.OwnerName = nomtitular
         self.CardNum= numtargeta