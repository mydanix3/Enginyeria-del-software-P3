import unittest
from src.Main import Reserva
from unittest import mock

class Test_Flights(unittest.TestCase):


    def test_Numero_Viatgers_Esperat(self):
      
        reserva = Reserva()
        
        reserva.addPassengers(3)
        self.assertEqual(reserva.getPassengers(), 3)

    def test_Lista_Destinacio_Buida_Si_Viatge_Sense_Destinacions(self):

        reserva = Reserva()
        
        self.assertEqual(reserva.getDestination(), [])
          
        reserva.addDestination('Roma', 123, 5, 50)
        
        reserva.remDestination(123)
        
        self.assertEqual(reserva.getDestination(), [])
      


    def test_Llista_Vols_Buida_Si_Viatge_Sense_Destinacions(self):
       
        reserva = Reserva()
        
        self.assertEqual(reserva.getCode(), [])
        
        reserva.addDestination('Roma', 123, 5, 50)
        
        reserva.remDestination(123)
        
        self.assertEqual(reserva.getCode(), [])

    def test_Preu_si_Viatge_Vols_Sense_Destinacions(self):
      
        reserva = Reserva()
     
        self.assertEqual(reserva.getPreuTotal(), 0)
        
        reserva.addDestination('Roma', 123, 5, 50)
        
        reserva.remDestination(123)
        
        self.assertEqual(reserva.getPreuTotal(), 0)

    def test_Llista_Destins_Afegint_destins(self):
       
        reserva = Reserva()
        reserva.addPassengers(3)
        reserva.addDestination('Roma', 123, 5, 50)
        self.assertEqual(reserva.getDestination(), ['Roma'])
        reserva.addDestination('Florencia',321, 1, 40)
        self.assertEqual(reserva.getDestination(), ['Roma', 'Florencia'])


    def test_Llista_Codis_Afegint_destins(self):
       
        reserva = Reserva()

        reserva.addPassengers(3)
        reserva.addDestination('Roma', 123, 5, 50)
        self.assertEqual(reserva.getCode(), [123])
        
        reserva.addDestination('Florencia', 321, 1, 40)
        self.assertEqual(reserva.getCode(), [123, 321])

    def test_Preu_Esperat_Amb_Un_Viatger(self):
    
        reserva = Reserva()

        reserva.addPassengers(1)
        reserva.addDestination('Roma', 123, 6, 50)
        
        self.assertEqual(reserva.getPreuTotal(), 50)   
       
        reserva.addDestination('Florencia', 321, 2, 40)
        
        self.assertEqual(reserva.getPreuTotal(), 90)

    def test_Preu_Esperat_Amb_Mes_Dun_Passatger(self):
       
        reserva = Reserva()
        
        reserva.addPassengers(3)     
        reserva.addDestination('Roma', 123, 6, 50)
        
        self.assertEqual(reserva.getPreuTotal(), 150)
       
        reserva.addDestination('Florencia', 321, 2, 40)
        
        self.assertEqual(reserva.getPreuTotal(), 270)


    def test_Llista_De_Destins_Esperada_eliminant_un_desti(self):
       
        
        reserva = Reserva()
        
        reserva.addPassengers(3)
        reserva.addDestination('Roma', 123, 2, 50)
        reserva.addDestination('Florencia', 321, 5, 40)
        reserva.addDestination('Belgica', 444, 6, 30)
        
        reserva.remDestination(321)
        
        self.assertEqual(reserva.getDestination(), ["Roma", "Belgica"])


    def test_Llista_de_Codis_Esperada_eliminant_un_desti(self):
       
        reserva = Reserva()
        
        reserva.addPassengers(3)
        reserva.addDestination('Roma', 123, 2, 50)
        reserva.addDestination('Florencia', 321, 5, 40)
        reserva.addDestination('Belgica', 444, 6, 30)
        
        reserva.remDestination(321)
        
        self.assertEqual(reserva.getCode(), [123, 444])


    def test_Preu_esperat_eliminant_un_desti(self):
        
        
        reserva = Reserva()
        
        reserva.addPassengers(3)
        reserva.addDestination('Roma', 123, 2, 50)
        reserva.addDestination('Florencia', 321, 5, 40)
        reserva.addDestination('Belgica', 444, 6, 30)
        
        self.assertEqual(reserva.getPreuTotal(), 360)
        
        reserva.remDestination(321)
        
        self.assertEqual(reserva.getPreuTotal(), 240)





if __name__ == '__main__':
    unittest.main()
