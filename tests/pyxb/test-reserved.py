import unittest
import pyxb_114.binding.basis

class TestReserved (unittest.TestCase):
    def testSTD (self):
        tSTD = pyxb_114.binding.basis.simpleTypeDefinition
        for k in tSTD.__dict__.keys():
            if not k.startswith('_'):
                self.assertTrue(k in tSTD._ReservedSymbols, k)

    def testCTD (self):
        tCTD = pyxb_114.binding.basis.complexTypeDefinition
        for k in tCTD.__dict__.keys():
            if not k.startswith('_'):
                self.assertTrue(k in tCTD._ReservedSymbols, k)

if '__main__' == __name__:
    unittest.main()
    
