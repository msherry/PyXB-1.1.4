import pyxb_114.binding.generate
import pyxb_114.binding.datatypes as xs
import pyxb_114.binding.basis
import pyxb_114.utils.domutils

import os.path
xsd='''<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:simpleType name="foo"/>
</xs:schema>'''

from pyxb_114.exceptions_ import *

import unittest

class TestTrac_200908181430 (unittest.TestCase):
    def testParsing (self):
        self.assertRaises(pyxb_114.SchemaValidationError, pyxb_114.binding.generate.GeneratePython, schema_text=xsd)

if __name__ == '__main__':
    unittest.main()
