import pyxb_114.binding.datatypes as xs

import unittest

class TestTrac_0138 (unittest.TestCase):
    Literal = '2012-06-07T07:14:38.125296'
    def testPreservation (self):
        value = xs.dateTime(self.Literal)
        self.assertEqual(value.xsdLiteral(), self.Literal)

if __name__ == '__main__':
    unittest.main()
    
        
