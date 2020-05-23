import unittest
from src.Main import Reserva
from unittest import mock
from src.Booking import Booking 

class Test_Booking(unittest.TestCase):
    
    def test_confirmacio_hotels_correcte(self):

        reserva = Reserva()

        #usuari introdueix dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")


        reserva.addPassengers(3)
        reserva.addHotel('Hotel Verdi', 10, "871654", 20)

        b = reserva.confirm_reserve_Hotels()

        self.assertEqual(b,0)

    @mock.patch('src.Booking.Booking.confirm_reserve')
    def test_confirmacio_hotels_erroni(self,mock_confirm):

        reserva = Reserva()

        #usuari introdueix dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        mock_confirm.return_value = False

        reserva.addPassengers(3)
        reserva.addHotel('Hotel Verdi', 10, "871654", 20)

        b = reserva.confirm_reserve_Hotels()

        self.assertEqual(b,1)# -*- coding: utf-8 -*-

    @mock.patch('src.Booking.Booking.confirm_reserve')
    def test_confirmacio_cars_reintent_erroni(self, mock_confirm):
        
        reserva = Reserva()

        #usuari introdueix dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        mock_confirm.return_value = False

        reserva.addPassengers(3)
        reserva.addHotel('Hotel Verdi', 10, "871654", 20)
        
        result = 1
        
        while result == 1:
            
            result = reserva.confirm_reserve_Hotels()
            
        self.assertEqual(result, 2)
        
        
    @mock.patch('src.Booking.Booking.confirm_reserve')
    def test_confirmacio_cars_reintent_segon_cas_correcte(self, mock_confirm):
        
        reserva = Reserva()

        #usuari introdueix dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        mock_confirm.return_value = False

        reserva.addPassengers(3)
        reserva.addHotel('Hotel Verdi', 10, "871654", 20)
        
        result = 1
        
        while(result == 1):
            
            result = reserva.confirm_reserve_Hotels()
            mock_confirm.return_value = True
            
        self.assertEqual(result, 0)
        
if __name__ == '__main__':
    unittest.main()