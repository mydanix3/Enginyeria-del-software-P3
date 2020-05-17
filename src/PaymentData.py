class PaymentData:
    
    def __init__(self,tipstargeta,nomtitular,codiseguretat,importe):
        self.CardType = tipstargeta
        self.OwnerName = nomtitular
        self.SecurityCode = codiseguretat
        self.Money = importe