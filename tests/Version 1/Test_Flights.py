import unittest
from src.Flights import Flights
from unittest import mock

class Test_Flights(unittest.TestCase):
    
         
    def test_Viajeros(self):
        vols = Flights(['Roma'], 3) 
        self.assertEqual(vols.getPassengers(), 3)

    def test_ListaDestinoVacia(self):    
        vols = Flights([], 3)
        self.assertEqual(vols.Destination, [])
    

    def test_ListaVueloVacia(self):     
        vols = Flights([], 3)
        self.assertEqual(vols.Code, [])

    def test_PrecioVacio(self):
        vols = Flights([], 3)
        self.assertEqual(vols.getTotalToPay(), 0)

    def test_AddDestino_destino(self):
        vols = Flights(['Roma'], 3)
        vols.addDestination("Italia")
        self.assertEqual(vols.Destination, ['Roma', 'Italia'])

    @mock.patch('src.Flights.Flights.getCodiVol')
    def test_AddDestino_codigo(self, mock_flights):
        mock_flights.return_value = 123
        vols = Flights(["Roma"],3)
        mock_flights.return_value = 321
        vols.addDestination("Italia")
        self.assertEqual(vols.Code, [123,321])
    
    @mock.patch('src.Flights.Flights.getPreuVol')
    def test_PreuEsperat(self, mock_preus):
        mock_preus.return_value = 50
        vols = Flights(["Roma"],1)
        self.assertEqual(vols.getTotalToPay(), 50)
        mock_preus.return_value = 40
        vols.addDestination("Italia")
        self.assertEqual(vols.getTotalToPay(), 90)
    
    @mock.patch('src.Flights.Flights.getPreuVol')
    def test_PreuEsperatMultiple(self, mock_preus):
        mock_preus.return_value = 50
        vols = Flights(["Roma"],3)
        self.assertEqual(vols.getTotalToPay(), 150)
        mock_preus.return_value = 40
        vols.addDestination("Italia")
        self.assertEqual(vols.getTotalToPay(), 270)
        
    def test_RmDestino_destino(self):
        vols = Flights(["Roma","Italia","Belgica"],3)
        vols.remDestination("Italia")
        self.assertEqual(vols.Destination, ["Roma", "Belgica"])
        
    @mock.patch('src.Flights.Flights.getCodiVol')
    def test_RmDestino_codigo(self, mock_flights):
        mock_flights.return_value = 123
        vols = Flights(["Roma"],3)
        mock_flights.return_value = 321
        vols.addDestination("Italia")
        mock_flights.return_value = 444
        vols.addDestination("Belginca")
        vols.remDestination("Italia")
         
        self.assertEqual(vols.Code, [123, 444])
        
    @mock.patch('src.Flights.Flights.getPreuVol')
    def test_RmDestino_preu(self, mock_flights):
        mock_flights.return_value = 50
        vols = Flights(["Roma"],3)
        mock_flights.return_value = 40
        vols.addDestination("Italia")
        mock_flights.return_value = 30
        vols.addDestination("Belginca")
        self.assertEqual(vols.getTotalToPay(), 360)
        vols.remDestination("Italia")
        self.assertEqual(vols.getTotalToPay(), 240)
        
    
        
        
    
    



if __name__ == '__main__':
    unittest.main()
