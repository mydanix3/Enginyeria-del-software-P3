import unittest
from src.Main import Reserva
from unittest.mock import MagicMock
from unittest import mock


class Test_RentalCars(unittest.TestCase):
    
    def test_confirmacio_cars_correcte(self):

        reserva = Reserva()
        #usuari introdueix dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        reserva.addPassengers(3)
        reserva.addCar("17842","Chevrolet","Roma",6,20)

        b = reserva.confirm_reserve_cotxes()

        self.assertEqual(b, 0)

    @mock.patch('src.Rentalcars.Rentalcars.confirm_reserve')
    def test_confirmacio_cars_erroni(self,mock_confirm):

        reserva = Reserva()

        #usuari introdueix dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        mock_confirm.return_value = False

        reserva.addPassengers(4)
        reserva.addCar("17842","Chevrolet","Roma",6,20)

        b = reserva.confirm_reserve_cotxes()

        self.assertEqual(b, 1)

    @mock.patch('src.Rentalcars.Rentalcars.confirm_reserve')
    def test_confirmacio_cars_reintent_erroni(self, mock_confirm):
        
        reserva = Reserva()

        #usuari introdueix dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        mock_confirm.return_value = False

        reserva.addPassengers(4)
        reserva.addCar("17842","Chevrolet","Roma",6,20)
        
        result = 1
        
        while result == 1:
            
            result = reserva.confirm_reserve_cotxes()
            
        self.assertEqual(result, 2)
        
        
    @mock.patch('src.Rentalcars.Rentalcars.confirm_reserve')
    def test_confirmacio_cars_reintent_segon_cas_correcte(self, mock_confirm):
        
        reserva = Reserva()

        #usuari introdueix dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        mock_confirm.return_value = False

        reserva.addPassengers(4)
        reserva.addCar("17842","Chevrolet","Roma",6,20)
        
        result = 1
        
        while(result == 1):
            
            result = reserva.confirm_reserve_cotxes()
            mock_confirm.return_value = True
            
        self.assertEqual(result,0)
        
if __name__ == '__main__':
    unittest.main()
