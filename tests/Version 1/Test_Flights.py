import unittest
from src.Main import Reserva
from unittest import mock

class Test_Flights(unittest.TestCase):
    
         
    def test_Viajeros(self):
        '''
        vols = Flights(['Roma'], 3) 
        self.assertEqual(vols.getPassengers(), 3)
        '''
        reserva = Reserva()
        reserva.addDestination(['Roma'])
        reserva.addPassengers(3)
        self.assertEqual(reserva.getPassengers(), 3)

    def test_ListaDestinoVacia(self):


        '''
        vols = Flights([], 3)
        self.assertEqual(vols.Destination, [])
        '''
        reserva = Reserva()
        reserva.addDestination([])
        reserva.addPassengers(3)
        self.assertEqual(reserva.getDestination(), [])
    

    def test_ListaVueloVacia(self):
        '''
        vols = Flights([], 3)
        self.assertEqual(vols.Code, [])
        '''
        reserva = Reserva()
        reserva.addDestination([])
        reserva.addPassengers(3)
        self.assertEqual(reserva.getCode(), [])

    def test_PrecioVacio(self):
        '''
        vols = Flights([], 3)
        self.assertEqual(vols.getTotalToPay(), 0)
        '''
        reserva = Reserva()
        reserva.addDestination([])
        reserva.addPassengers(3)
        self.assertEqual(reserva.getTotalToPay(), 0)

    def test_AddDestino_destino(self):
        '''
        vols = Flights(['Roma'], 3)
        vols.addDestination("Italia")
        self.assertEqual(vols.Destination, ['Roma', 'Italia'])
        '''
        reserva = Reserva()
        reserva.addDestination(['Roma'])
        reserva.addPassengers(3)
        reserva.addDestination('Italia')
        self.assertEqual(reserva.getDestination(), ['Roma', 'Italia'])

    @mock.patch('src.Flights.Flights.getCodiVol')
    def test_AddDestino_codigo(self, mock_flights):
        '''
        mock_flights.return_value = 123
        vols = Flights(["Roma"],3)
        mock_flights.return_value = 321
        vols.addDestination("Italia")
        self.assertEqual(vols.Code, [123,321])
        '''
        reserva = Reserva()
        mock_flights.return_value = 123
        reserva.addDestination(['Roma'])
        reserva.addPassengers(3)
        mock_flights.return_value = 321
        reserva.addDestination('Italia')
        self.assertEqual(reserva.getCode(), [123, 321])
    
    @mock.patch('src.Flights.Flights.getPreuVol')
    def test_PreuEsperat(self, mock_preus):
        '''
        mock_preus.return_value = 50
        vols = Flights(["Roma"],1)
        self.assertEqual(vols.getTotalToPay(), 50)
        mock_preus.return_value = 40
        vols.addDestination("Italia")
        self.assertEqual(vols.getTotalToPay(), 90)
        '''
        reserva = Reserva()
        mock_preus.return_value = 50
        reserva.addDestination(['Roma'])
        reserva.addPassengers(1)
        self.assertEqual(reserva.getTotalToPay(), 50)
        mock_preus.return_value = 40
        reserva.addDestination('Italia')
        self.assertEqual(reserva.getTotalToPay(), 90)
    
    @mock.patch('src.Flights.Flights.getPreuVol')
    def test_PreuEsperatMultiple(self, mock_preus):
        '''
        mock_preus.return_value = 50
        vols = Flights(["Roma"],3)
        self.assertEqual(vols.getTotalToPay(), 150)
        mock_preus.return_value = 40
        vols.addDestination("Italia")
        self.assertEqual(vols.getTotalToPay(), 270)
        '''
        reserva = Reserva()
        mock_preus.return_value = 50
        reserva.addDestination(['Roma'])
        reserva.addPassengers(3)
        self.assertEqual(reserva.getTotalToPay(), 150)
        mock_preus.return_value = 40
        reserva.addDestination('Italia')
        self.assertEqual(reserva.getTotalToPay(), 270)
        
    def test_RmDestino_destino(self):
        '''
        vols = Flights(["Roma","Italia","Belgica"],3)
        vols.remDestination("Italia")
        self.assertEqual(vols.Destination, ["Roma", "Belgica"])
        '''
        reserva = Reserva()
        reserva.addDestination(['Roma', 'Italia', 'Belgica'])
        reserva.addPassengers(3)
        reserva.remDestination('Italia')
        self.assertEqual(reserva.getDestination(), ["Roma", "Belgica"])
        
    @mock.patch('src.Flights.Flights.getCodiVol')
    def test_RmDestino_codigo(self, mock_flights):
        '''
        mock_flights.return_value = 123
        vols = Flights(["Roma"],3)
        mock_flights.return_value = 321
        vols.addDestination("Italia")
        mock_flights.return_value = 444
        vols.addDestination("Belginca")
        vols.remDestination("Italia")
        self.assertEqual(vols.Code, [123, 444])
        '''
        reserva = Reserva()
        mock_flights.return_value = 123
        reserva.addDestination(['Roma'])
        reserva.addPassengers(3)
        mock_flights.return_value = 321
        reserva.addDestination('Italia')
        mock_flights.return_value = 444
        reserva.addDestination('Belgica')
        reserva.remDestination('Italia')
        self.assertEqual(reserva.getCode(), [123, 444])
        
    @mock.patch('src.Flights.Flights.getPreuVol')
    def test_RmDestino_preu(self, mock_flights):
        '''
        mock_flights.return_value = 50
        vols = Flights(["Roma"],3)
        mock_flights.return_value = 40
        vols.addDestination("Italia")
        mock_flights.return_value = 30
        vols.addDestination("Belginca")
        self.assertEqual(vols.getTotalToPay(), 360)
        vols.remDestination("Italia")
        self.assertEqual(vols.getTotalToPay(), 240)
        '''
        reserva = Reserva()
        mock_flights.return_value = 50
        reserva.addDestination('Roma')
        reserva.addPassengers(3)
        mock_flights.return_value = 40
        reserva.addDestination("Italia")
        mock_flights.return_value = 30
        reserva.addDestination("Belgica")
        self.assertEqual(reserva.getTotalToPay(), 360)
        reserva.remDestination('Italia')
        self.assertEqual(reserva.getTotalToPay(), 240)
        
    
        
        
    
    



if __name__ == '__main__':
    unittest.main()
