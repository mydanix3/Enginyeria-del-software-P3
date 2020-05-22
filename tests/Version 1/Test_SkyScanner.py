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

        
        
        
    
    
if __name__ == '__main__':
    unittest.main()
