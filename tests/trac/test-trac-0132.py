# -*- coding: utf-8 -*-

import sys
import pyxb_114
import unittest

class TestTrac0132 (unittest.TestCase):
    message = u'bad character \u2620'
    def testDecode (self):
        e = pyxb_114.PyXBException(self.message)
        if sys.version_info[:2] > (2, 4):
            self.assertEqual(self.message, e.message)

if __name__ == '__main__':
    unittest.main()
