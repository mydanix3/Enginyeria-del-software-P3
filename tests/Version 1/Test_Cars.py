import unittest
from src.Main import Reserva
from unittest import mock

class Test_Cars(unittest.TestCase):

    def test_preu_cars_add():
        reserva = Reserva()
        reserva.addPassengers(8)
        preuInicial = reserva.getPreuTotal()
        reserva.addCar("17842","Chevrolet","Roma",6,20)
        preuFinal = preuInicial+40
        self.assertEqual(preuFinal,reserva.getPreuTotal())

    def test_preu_remove_cars(self):
        reserva = Reserva()
        reserva.addPassengers(8)
        reserva.addCar("17842","Chevrolet","Roma",6,20)
        reserva.addCar("19888","Mazda","Italia",6,25)
        preuInicial = reserva.getPreuTotal()
        reserva.removeCar("19888")
        preuFinal = preuInicial-50
        self.assertEqual(preuFinal, reserva.getPreuTotal())

    def test_confirmacio_cars_correcte(self):

        reserva = Reserva()
        #usuari introdueix dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        reserva.addPassengers(3)
        reserva.addCar("17842","Chevrolet","Roma",6,20)

        b = reserva.confirm_reserve_cotxes()

        self.assertTrue(b)

    @mock.patch('src.Skyscanner.Skyscanner.confirm_reserve')
    def test_confirmacio_cars_erroni(self,mock_confirm):

        reserva = Reserva()

        #usuari introdueix dades
        reserva.DadesUsuari("Santiago Marco", "49792132B", "08193", "657854321", "santiago.marco@uab.cat")

        mock_confirm.return_value = False

        reserva.addPassengers(4)
        reserva.addCar("17842","Chevrolet","Roma",6,20)

        b = reserva.confirm_reserve_cotxes()

        self.assertFalse(b)


if __name__ == '__main__':
    unittest.main()
