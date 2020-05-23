import unittest
from src.Flights import Flights
from src.User import User
from src.Skyscanner import Skyscanner
from src.Main import Reserva
from unittest import mock

class Test_Bank(unittest.TestCase):
    
    def test_ConfirmVols(self):
        '''
        #l'usuari posa les seves dades
        user = User()  
        user.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")
        
        #escull un viatge
        vols = Flights(["Roma", "Italia"],3)
       
        #cridem a la funció del SkyScanner per intentar verificar els vols
        skyscanner = Skyscanner()
        confirmem_vols = skyscanner.confirm_reserve(user, vols)
        
        #Si la funció retorna true, mostrariem per pantalla que els vols s'han pogut confirmar
        self.assertEqual(confirmem_vols, True)
        '''
        reserva = Reserva()

        #l'usuari posa les seves dades

        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        # escull un viatge
        reserva.addDestination(["Roma", "Italia"])
        reserva.addPassengers(3)

        # cridem a la funció del SkyScanner per intentar verificar els vols
        confirmem_vols = reserva.confirm_reserve(reserva.user, reserva.flights)
        # Si la funció retorna true, mostrariem per pantalla que els vols s'han pogut confirmar
        self.assertEqual(confirmem_vols, True)

    @mock.patch('src.Skyscanner.Skyscanner.confirm_reserve')
    def test_error_reserva_vuelos(self, mock_skyscanner):
        reserva = Reserva()

        # l'usuari posa les seves dades

        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        # escull un viatge
        reserva.addDestination(["Roma", "Italia"])
        reserva.addPassengers(3)

        # cridem a la funció del SkyScanner per intentar verificar els vols
        mock_skyscanner.return_value = False
        confirmem_vols = reserva.confirm_reserve(reserva.user, reserva.flights)
        # Si la funció retorna false, mostrariem per pantalla que els vols no s'han pogut confirmar
        self.assertEqual(confirmem_vols, False)
        print("Els vols no s'han pogut confirmar")

    @mock.patch('src.Skyscanner.Skyscanner.confirm_reserve')
    def test_error_reserva_bucle(self, mock_skyscanner):
        contador = 0

        def bucle():

            reserva = Reserva()
            mock_skyscanner.return_value = False

            # l'usuari posa les seves dades

            reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

            # escull un viatge
            reserva.addDestination(["Roma", "Italia"])
            reserva.addPassengers(3)

            # cridem a la funció del SkyScanner per intentar verificar els vols

            confirmem_vols = reserva.confirm_reserve(reserva.user, reserva.flights)
            # Si la funció retorna false, mostrariem per pantalla que els vols no s'han pogut confirmar
            self.assertEqual(confirmem_vols, False)
            print("Els vols no s'han pogut confirmar")

        while contador < 3:
            contador+=1
            bucle()

        if contador == 3 :
            print("Se ha producido un error en la confirmación de la reserva")



    @mock.patch('src.Skyscanner.Skyscanner.confirm_reserve')
    def test_error_reserva_vuelos_acierta_segunda(self, mock_skyscanner):
        reserva = Reserva()

        # l'usuari posa les seves dades

        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        # escull un viatge
        reserva.addDestination(["Roma", "Italia"])
        reserva.addPassengers(3)

        # cridem a la funció del SkyScanner per intentar verificar els vols
        mock_skyscanner.return_value = False
        confirmem_vols = reserva.confirm_reserve(reserva.user, reserva.flights)
        # Si la funció retorna false, mostrariem per pantalla que els vols no s'han pogut confirmar
        self.assertEqual(confirmem_vols, False)
        print("Els vols no s'han pogut confirmar")


        reserva = Reserva()

        # l'usuari posa les seves dades

        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        # escull un viatge
        reserva.addDestination(["Roma", "Italia"])
        reserva.addPassengers(3)

        # cridem a la funció del SkyScanner per intentar verificar els vols
        mock_skyscanner.return_value = True
        confirmem_vols = reserva.confirm_reserve(reserva.user, reserva.flights)
        # Si la funció retorna false, mostrariem per pantalla que els vols no s'han pogut confirmar
        self.assertEqual(confirmem_vols, True)
        print("Els vols s'han pogut confirmar")

if __name__ == '__main__':
    unittest.main()
