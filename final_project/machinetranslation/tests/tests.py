import unittest

from translator import englishtofrench, frenchtoenglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishtofrench("null"),"Null" ) # test when null devuelve vacio
        self.assertEqual(englishtofrench('Hello'),'Bonjour' )  # test hola
        

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchtoenglish("null"),"Null" ) # test when null devuelve vacio
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello' )  # test hola
       
      
unittest.main()