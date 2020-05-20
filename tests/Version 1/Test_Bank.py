import unittest
from src.Flights import Flights
from src.PaymentData import PaymentData
from src.User import User
from src.Bank import Bank
from unittest import mock

class Test_Bank(unittest.TestCase):
    
    @mock.patch('src.Flights.Flights.getTotalToPay')
    def test_DoPayment(self, mock_flights):
        
        #l'usuari posa les seves dades
        user = User()  
        user.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")
        
        #escull un viatge i es calcula el preu
        vols = Flights(["Roma", "Italia"],3)
        mock_flights.return_value = 250
       
        #el preu es passa automàticament al paydata
        pay = PaymentData()
        pay.SetImport(vols.getTotalToPay())
        
        #es demana les dades de la tarjeta a l'usuari
        pay.DadesTarjeta("Santiago Marco Sola", "43523-76543-98123-76543", "987" )
        
        #cridem a la funció del Bank per a que ens faci l'operació
        banc = Bank()
        
        pagament_correcte = banc.do_payment(user, pay)
        
        #Si la funció dona true, mostrariem per pantalla que s'ha produit correctament
        self.assertEqual(pagament_correcte, True)
            
        
        
        
        
        
    
    
    
    
    
if __name__ == '__main__':
    unittest.main()