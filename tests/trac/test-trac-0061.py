import pyxb_114.binding.generate
import pyxb_114.binding.datatypes as xs
import pyxb_114.binding.basis
import pyxb_114.utils.domutils

import os.path
xsd='''<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
<xs:simpleType name="tla">
  <xs:annotation><xs:documentation>Simple type to represent a three-letter acronym</xs:documentation></xs:annotation>
  <xs:restriction base="xs:string">
    <xs:length value="3"/>
  </xs:restriction>
</xs:simpleType>
<xs:simpleType name="Atla">
  <xs:annotation><xs:documentation>A three-letter acronym that starts with A</xs:documentation></xs:annotation>
  <xs:restriction base="tla">
    <xs:pattern value="A.."/>
  </xs:restriction>
</xs:simpleType>
<xs:simpleType name="tlaZ">
  <xs:annotation><xs:documentation>A three-letter acronym that ends with Z</xs:documentation></xs:annotation>
  <xs:restriction base="tla">
    <xs:pattern value="..Z"/>
  </xs:restriction>
</xs:simpleType>
<xs:simpleType name="combAtlaZ">
  <xs:annotation><xs:documentation>A three-letter acronym that either starts with A or ends with Z</xs:documentation></xs:annotation>
  <xs:restriction base="tla">
    <xs:pattern value="A.."/>
    <xs:pattern value="..Z"/>
  </xs:restriction>
</xs:simpleType>
<xs:simpleType name="dervAtlaZ">
  <xs:annotation><xs:documentation>A three-letter acronym that starts with A and ends with Z</xs:documentation></xs:annotation>
  <xs:restriction base="Atla">
    <xs:pattern value="..Z"/>
  </xs:restriction>
</xs:simpleType>

</xs:schema>'''

#file('schema.xsd', 'w').write(xsd)
code = pyxb_114.binding.generate.GeneratePython(schema_text=xsd)
#file('code.py', 'w').write(code)
#print code

rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_114.exceptions_ import *

import unittest

class TestTrac_0061 (unittest.TestCase):
    def testDocString (self):
        self.assertEquals("Simple type to represent a three-letter acronym", tla._Documentation.strip())
        self.assertEquals("Simple type to represent a three-letter acronym", tla.__doc__.strip())

    def testTLA (self):
        self.assertEquals("tla", tla('tla'))
        self.assertRaises(pyxb_114.BadTypeValueError, tla, 'four')
        self.assertRaises(pyxb_114.BadTypeValueError, tla, '1')

    def testAtla (self):
        self.assertRaises(pyxb_114.BadTypeValueError, Atla, 'four')
        self.assertRaises(pyxb_114.BadTypeValueError, Atla, '1')
        self.assertEquals("A23", Atla('A23'))
        self.assertEquals("A2Z", Atla('A2Z'))
        self.assertRaises(pyxb_114.BadTypeValueError, Atla, 'B12')

    def testtlaZ (self):
        self.assertRaises(pyxb_114.BadTypeValueError, tlaZ, 'four')
        self.assertRaises(pyxb_114.BadTypeValueError, tlaZ, '1')
        self.assertEquals("12Z", tlaZ('12Z'))
        self.assertEquals("A2Z", tlaZ('A2Z'))
        self.assertRaises(pyxb_114.BadTypeValueError, tlaZ, '12X')

    def testcombAtlaZ (self):
        self.assertRaises(pyxb_114.BadTypeValueError, combAtlaZ, 'four')
        self.assertRaises(pyxb_114.BadTypeValueError, combAtlaZ, '1')
        self.assertEquals("A2Z", combAtlaZ('A2Z'))
        self.assertEquals("A23", combAtlaZ('A23'))
        self.assertEquals("12Z", combAtlaZ('12Z'))
        self.assertRaises(pyxb_114.BadTypeValueError, combAtlaZ, '12X')
        self.assertRaises(pyxb_114.BadTypeValueError, combAtlaZ, 'X23')

    def testdervAtlaZ (self):
        self.assertRaises(pyxb_114.BadTypeValueError, dervAtlaZ, 'four')
        self.assertRaises(pyxb_114.BadTypeValueError, dervAtlaZ, '1')
        self.assertEquals("A2Z", dervAtlaZ('A2Z'))
        self.assertRaises(pyxb_114.BadTypeValueError, dervAtlaZ, 'A23')
        self.assertRaises(pyxb_114.BadTypeValueError, dervAtlaZ, '12Z')
        self.assertRaises(pyxb_114.BadTypeValueError, dervAtlaZ, '12X')
        self.assertRaises(pyxb_114.BadTypeValueError, dervAtlaZ, 'X23')

if __name__ == '__main__':
    unittest.main()
