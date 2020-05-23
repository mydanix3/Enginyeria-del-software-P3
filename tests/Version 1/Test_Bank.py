import unittest
from src.Main import Reserva
from unittest.mock import MagicMock
from unittest import mock

class Test_Bank(unittest.TestCase):
    
    @mock.patch('src.Flights.Flights.getTotalToPay')
    def test_DoPayment(self, mock_flights):

        reserva = Reserva()

        #l'usuari posa les seves dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")
        
        #escull un viatge i es calcula el preu
        reserva.addDestination(["Roma", "Italia"])
        reserva.addPassengers(3)
        #vols = Flights(["Roma", "Italia"],3)
        mock_flights.return_value = 250
       
        #el preu es passa automàticament al paydata
        reserva.SetImport(reserva.getTotalToPay())
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
        self.assertEqual(pagament_correcte, True)
            
    def test_CardType(self):
        reserva = Reserva()

        # l'usuari posa les seves dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        user = reserva.user

        # escull un viatge i es calcula el preu
        reserva.addDestination(["Roma", "Italia"])
        reserva.addPassengers(3)

        reserva.SelectTargeta("Visa")

        reserva.DadesTarjeta("Santiago Marco Sola", "43523-76543-98123-76543", "987")

        auxiliar = reserva.paymentdata

        reserva.bank.do_payment = MagicMock(return_value = True)
        reserva.do_payment()

        reserva.bank.do_payment.assert_called_with(user, auxiliar)

    @mock.patch('src.Bank.Bank.do_payment')
    def test_ErrorPago(self, mock_bank):
        reserva = Reserva()

        # l'usuari posa les seves dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        # escull un viatge i es calcula el preu
        reserva.addDestination(["Roma", "Italia"])
        reserva.addPassengers(3)

        reserva.SelectTargeta("Visa")

        reserva.DadesTarjeta("Santiago Marco Sola", "43523-76543-98123-76543", "987")

        mock_bank.return_value = False
        respuesta = reserva.do_payment()

        self.assertEqual(respuesta, False, msg="No se ha podido realizar el pago")
        print("No se ha podido realizar el pago")


    @mock.patch('src.Bank.Bank.do_payment')
    def test_ErrorPago_bucle(self, mock_bank):

        contador = 0
        def bucle():
            reserva = Reserva()

            # l'usuari posa les seves dades
            reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

            # escull un viatge i es calcula el preu
            reserva.addDestination(["Roma", "Italia"])
            reserva.addPassengers(3)

            reserva.SelectTargeta("Visa")

            reserva.DadesTarjeta("Santiago Marco Sola", "43523-76543-98123-76543", "987")

            mock_bank.return_value = False
            respuesta = reserva.do_payment()

            self.assertEqual(respuesta, True, msg="No se ha podido realizar el pago")
            print("No se ha podido realizar el pago")

        while contador < 3:
            contador+=1
            bucle()

        if contador == 3 :
            print("Se ha producido un error en la realización del la pago")


    @mock.patch('src.Bank.Bank.do_payment')
    def test_ErrorPago_segunda_ok(self, mock_bank):
        reserva = Reserva()

        # l'usuari posa les seves dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        # escull un viatge i es calcula el preu
        reserva.addDestination(["Roma", "Italia"])
        reserva.addPassengers(3)

        reserva.SelectTargeta("Visa")

        reserva.DadesTarjeta("Santiago Marco Sola", "43523-76543-98123-76543", "987")

        mock_bank.return_value = False
        respuesta = reserva.do_payment()

        self.assertEqual(respuesta, False, msg="No se ha podido realizar el pago")
        print("No se ha podido realizar el pago")

        reserva = Reserva()

        # l'usuari posa les seves dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        # escull un viatge i es calcula el preu
        reserva.addDestination(["Roma", "Italia"])
        reserva.addPassengers(3)

        reserva.SelectTargeta("Visa")

        reserva.DadesTarjeta("Santiago Marco Sola", "43523-76543-98123-76543", "987")

        mock_bank.return_value = True
        respuesta = reserva.do_payment()

        self.assertEqual(respuesta, True, msg="No se ha podido realizar el pago")
        print("Se ha podido realizar el pago")

        
        
    
    
    
    
    
if __name__ == '__main__':
    unittest.main()
