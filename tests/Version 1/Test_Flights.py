import unittest
import Flights
from unittest import mock

class Test_Flights(unittest.TestCase):

    def test_Viajeros(self):
        vuelo = Flights.Flights([123],["Roma"],3)
        self.assertEqual(vuelo.Passengers, 3)

    def test_ListaDestinoVacia(self):
        vuelo = Flights.Flights([123],[],3)
        self.assertEqual(vuelo.Destination, [])

    def test_ListaVueloVacia(self):
        vuelo = Flights.Flights([123],[],3)
        self.assertEqual(vuelo.Code, [])

    def test_PrecioVacio(self):
        vuelo = Flights.Flights([123],[],3)
        self.assertEqual(vuelo.Code, [])

    @mock.patch('src.Flights')
    def test_AddDestino_destino(self):
        mock_flights.getCodiVol.return_value = 299
        expected = ["Roma","Italia"]
        vuelo = mock_flights.Flights([123],["Roma"],3)
        vuelo.addDestination("Italia")
        self.assertEqual(vuelo.Destination, expected)

    @mock.patch('src.Flights')
    def test_AddDestino_codigo(self):
        mock_flights.getCodiVol.return_value = 321
        expected = [123,321]
        vuelo = mock_flights.Flights([123],["Roma"],3)
        vuelo.addDestination("Italia")
        self.assertEqual(vuelo.Destination, expected)



if __name__ == '__main__':
    unittest.main()
