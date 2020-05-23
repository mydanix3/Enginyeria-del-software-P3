import unittest
from src.Flights import Flights
from src.User import User
from src.Skyscanner import Skyscanner
from src.Main import Reserva
from unittest import mock

class Test_SkyScanner(unittest.TestCase):
    
    def test_reservar_vols_correcte(self):
        
        
        reserva = Reserva()

        #l'usuari posa les seves dades

        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        # escull un viatge
        reserva.addPassengers(3)
        reserva.addDestination('Roma', 123, 5, 50)
        reserva.addDestination('Florencia',321, 1, 40)
        

        # cridem a la funció del SkyScanner per intentar verificar els vols
        confirmem_vols = reserva.confirm_reserve_vols()
        
        # Si la funció retorna true, mostrariem per pantalla que els vols s'han pogut confirmar
        self.assertEqual(confirmem_vols, 0)
        
        
    @mock.patch('src.Skyscanner.Skyscanner.confirm_reserve')
    def test_error_reserva_vols(self, mock_skyscanner):
        reserva = Reserva()

        mock_skyscanner.return_value = False
        # l'usuari posa les seves dades

        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        # escull un viatge
        reserva.addPassengers(3)
        reserva.addDestination('Roma', 123, 5, 50)
        reserva.addDestination('Florencia',321, 1, 40)

        # cridem a la funció del SkyScanner per intentar verificar els vols
        confirmem_vols = reserva.confirm_reserve_vols()
        
        # Si la funció retorna false, mostrariem per pantalla que els vols no s'han pogut confirmar
        self.assertEqual(confirmem_vols, 1)


    @mock.patch('src.Skyscanner.Skyscanner.confirm_reserve')
    def test_error_reserva_bucle(self, mock_skyscanner):


        reserva = Reserva()
        mock_skyscanner.return_value = False

        # l'usuari posa les seves dades

        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        # escull un viatge
        reserva.addPassengers(3)
        reserva.addDestination('Roma', 123, 5, 50)
        
        acert = 1
        
        while(acert == 1):
            
            acert = reserva.confirm_reserve_vols()
    
        # Si la funció retorna -1, mostrariem per pantalla que els vols no s'han pogut confirmar
        self.assertEqual(acert, 2)



    @mock.patch('src.Skyscanner.Skyscanner.confirm_reserve')
    def test_error_reserva_vuelos_acierta_segunda(self, mock_skyscanner):
        reserva = Reserva()
        mock_skyscanner.return_value = False

        # l'usuari posa les seves dades

        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        # escull un viatge
        reserva.addPassengers(3)
        reserva.addDestination('Roma', 123, 5, 50)
        
        acert = 1
        
        while(acert == 1):
            
            acert = reserva.confirm_reserve_vols()
            mock_skyscanner.return_value = True
    
        # Si la funció retorna -1, mostrariem per pantalla que els vols no s'han pogut confirmar
        self.assertEqual(acert, 0)

if __name__ == '__main__':
    unittest.main()
