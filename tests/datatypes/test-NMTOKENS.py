from pyxb_114.exceptions_ import *
import unittest
import pyxb_114.binding.datatypes as xsd

class Test_NMTOKENS (unittest.TestCase):
    def testBasicLists (self):
        v = xsd.NMTOKENS([ "one", "_two", "three" ])
        self.assertEqual(3, len(v))
        self.assertTrue(isinstance(v[0], xsd.NMTOKEN))
        self.assertEqual("one", v[0])

    def testStringLists (self):
        v = xsd.NMTOKENS("one _two three")
        self.assertEqual(3, len(v))
        self.assertEqual("one", v[0])
        self.assertTrue(isinstance(v[0], xsd.NMTOKEN))
        self.assertRaises(BadTypeValueError, xsd.NMTOKENS, 'string with b@d id')

if __name__ == '__main__':
    unittest.main()
