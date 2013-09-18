import pyxb_114.binding.generate
import pyxb_114.utils.domutils
import pyxb_114.utils.utility
from pyxb_114.utils.utility import MakeIdentifier

import os.path
xsd='''<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
   <xs:complexType name="simple_type">
      <xs:simpleContent>
         <xs:extension base="xs:string"/>
      </xs:simpleContent>
      <!-- attribute cannot be here, must be in xs:extension -->
      <xs:attribute name="is_clean" type="xs:boolean"/>
   </xs:complexType>
   <xs:element name="simple_element" type="simple_type"/>
</xs:schema>'''

import unittest

class TestTrac0148 (unittest.TestCase):
    def testProcessing (self):
        self.assertRaises(pyxb_114.SchemaValidationError, pyxb_114.binding.generate.GeneratePython, schema_text=xsd)

if __name__ == '__main__':
    unittest.main()
