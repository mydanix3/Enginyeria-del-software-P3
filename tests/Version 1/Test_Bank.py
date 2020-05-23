import unittest
from src.Main import Reserva
from unittest.mock import MagicMock
from unittest import mock

class Test_Bank(unittest.TestCase):
    
    def test_Pagament_Correcte(self):

        reserva = Reserva()

        #l'usuari posa les seves dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")
        
        #escull un viatge i es calcula el preu
        reserva.addPassengers(3)
        reserva.addDestination('Roma', 123, 5, 50)
       
        #el preu es passa automàticament al paydata
        reserva.SetImport(reserva.getPreuTotal())
        #pay = PaymentData()
        #pay.SetImport(vols.getTotalToPay())

        #es demana les dades de la tarjeta a l'usuari
        reserva.DadesTarjeta("Santiago Marco Sola", "43523-76543-98123-76543", "987" )
        #pay.DadesTarjeta("Santiago Marco Sola", "43523-76543-98123-76543", "987")
        
        #cridem a la funció del Bank per a que ens faci l'operació

        pagament_correcte = reserva.do_payment()
        #banc = Bank()
        #pagament_correcte = banc.do_payment(user, pay)
        
        #Si la funció dona true, mostrariem per pantalla que s'ha produit correctament
        self.assertEqual(pagament_correcte, 0)
            
    def test_CardType(self):
            reserva = Reserva()

            # l'usuari posa les seves dades
            reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")
    
            user = reserva.user
    
            # escull un viatge i es calcula el preu
            reserva.addPassengers(3)
            reserva.addDestination('Roma', 123, 5, 50)
    
            reserva.SelectTargeta("Visa")
    
            reserva.DadesTarjeta("Santiago Marco Sola", "43523-76543-98123-76543", "987")
    
            auxiliar = reserva.paymentdata
    
            reserva.bank.do_payment = MagicMock(return_value = True)
            reserva.do_payment()
    
            reserva.bank.do_payment.assert_called_with(user, auxiliar)
            

    @mock.patch('src.Bank.Bank.do_payment')
    def test_Pagament_incorrecte(self, mock_bank):
        reserva = Reserva()

        # l'usuari posa les seves dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        # escull un viatge i es calcula el preu
        reserva.addPassengers(3)
        reserva.addDestination('Roma', 123, 5, 50)

        reserva.SelectTargeta("Visa")

        reserva.DadesTarjeta("Santiago Marco Sola", "43523-76543-98123-76543", "987")

        mock_bank.return_value = False
        respuesta = reserva.do_payment()

        self.assertEqual(respuesta, 1)
        


    @mock.patch('src.Bank.Bank.do_payment')
    def test_Error_Pago_bucle(self, mock_bank):

       
        reserva = Reserva()

        # l'usuari posa les seves dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        # escull un viatge i es calcula el preu
        reserva.addPassengers(3)
        reserva.addDestination('Roma', 123, 5, 50)
        
        reserva.SelectTargeta("Visa")

        respuesta = 1 
        mock_bank.return_value = False
        
        while(respuesta == 1):

            reserva.DadesTarjeta("Santiago Marco Sola", "43523-76543-98123-76543", "987")

            respuesta = reserva.do_payment()

        self.assertEqual(respuesta, 2)
           


    @mock.patch('src.Bank.Bank.do_payment')
    def test_Error_Pago_segon_cas_ok(self, mock_bank):
        reserva = Reserva()

        # l'usuari posa les seves dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        # escull un viatge i es calcula el preu
        reserva.addPassengers(3)
        reserva.addDestination('Roma', 123, 5, 50)
        
        reserva.SelectTargeta("Visa")

        respuesta = 1 
        mock_bank.return_value = False
        while(respuesta == 1):

            reserva.DadesTarjeta("Santiago Marco Sola", "43523-76543-98123-76543", "987")

            respuesta = reserva.do_payment()
            mock_bank.return_value = True
            

        self.assertFalse(respuesta, 0)
           

    
if __name__ == '__main__':
    unittest.main()
