import unittest
from src.Main import Reserva
from unittest import mock

class Test_Cars(unittest.TestCase):

    def test_preu_al_afegir_un_cotxe(self):
        reserva = Reserva()
        reserva.addPassengers(8)
 
        reserva.addCar("17842","Chevrolet","Roma",6,20)

        self.assertEqual(240,reserva.getPreuTotal())

    def test_preu_remove_cars(self):
        reserva = Reserva()
        reserva.addPassengers(8)
        reserva.addCar("17842","Chevrolet","Roma",6,20)
        reserva.addCar("19888","Mazda","Italia",6,25)

        reserva.removeCar("19888")

        self.assertEqual(240, reserva.getPreuTotal())
        

if __name__ == '__main__':
    unittest.main()
