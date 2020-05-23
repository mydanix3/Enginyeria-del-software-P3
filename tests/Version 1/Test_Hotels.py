# -*- coding: utf-8 -*-

import unittest
from src.Main import Reserva
from unittest import mock
from src.Booking import Booking

class Test_Flights(unittest.TestCase):

    def test_preu_hotels_add(self):
        reserva = Reserva()
        reserva.addPassengers(3)
        reserva.addHotel('Hotel Verdi', 10, "871654", 20)
        self.assertEqual(reserva.getPreuTotal(), 600)
        reserva.addHotel('Hotel Vela', 5, "457682", 30)
        self.assertEqual(reserva.getPreuTotal(), 1050)

    def test_preu_remove_hotel(self):
        reserva = Reserva()
        reserva.addPassengers(3)
        reserva.addHotel('Hotel Verdi', 10, "871654", 20)
        reserva.addHotel('Hotel Vela', 5, "457682", 30)
        reserva.remHotel("871654")
        self.assertEqual(reserva.getPreuTotal(), 450)

    def test_confirmacio_hotels_correcte(self):

        reserva = Reserva()

        #usuari introdueix dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")


        reserva.addPassengers(3)
        reserva.addHotel('Hotel Verdi', 10, "871654", 20)

        b = reserva.confirm_reserve_Hotels()

        self.assertTrue(b)

    @mock.patch('src.Booking.Booking.confirm_reserve')
    def test_confirmacio_hotels_erroni(self,mock_confirm):

        reserva = Reserva()

        #usuari introdueix dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        mock_confirm.return_value = False

        reserva.addPassengers(3)
        reserva.addHotel('Hotel Verdi', 10, "871654", 20)

        b = reserva.confirm_reserve_Hotels()

        self.assertFalse(b)


if __name__ == '__main__':
    unittest.main()
