import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("null"),"" ) # test when null devuelve vacio
        self.assertEqual(englishToFrench("Hello"),"Bonjour" )  # test when 3.0 is given as input the output is 9.0.
        

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish("null"),"" ) # test when null devuelve vacio
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello" )  # test when 3.0 is given as input the output is 9.0.
       
        
unittest.main()