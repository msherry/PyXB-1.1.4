import pyxb_114.binding.generate
import pyxb_114.binding.datatypes as xs
import pyxb_114.binding.basis
import pyxb_114.utils.domutils

import os.path
xsd='''<?xml version="1.0" encoding="utf-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
        <xs:simpleType name="tBase">
                <xs:restriction base="xs:normalizedString">
                        <xs:enumeration value="A"/>
                        <xs:enumeration value="B"/>
                        <xs:enumeration value="C"/>
                        <xs:enumeration value="D"/>
                </xs:restriction>
        </xs:simpleType>
        <xs:simpleType name="tRestr">
                <xs:restriction base="tBase"/>
        </xs:simpleType>
        <xs:simpleType name="tAltRestr">
                <xs:restriction base="tBase">
                    <xs:enumeration value="C"/>
		</xs:restriction>
        </xs:simpleType>
	<xs:element name="base" type="tBase"/>
	<xs:element name="restr" type="tRestr"/>
	<xs:element name="altrestr" type="tAltRestr"/>
</xs:schema>
'''

#file('schema.xsd', 'w').write(xsd)
code = pyxb_114.binding.generate.GeneratePython(schema_text=xsd)
#file('code.py', 'w').write(code)
#print code

rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_114.exceptions_ import *

import unittest

class TestTrac_0089 (unittest.TestCase):
    base_valid = ( 'A', 'B', 'C', 'D' )
    restr_valid = base_valid
    altrestr_valid = ( 'C' )
    invalid = ( 'Q' )

    def testBase (self):
        for ok in self.base_valid:
            xmls = '<base>%s</base>' % (ok,)
            instance = CreateFromDocument(xmls)
            self.assertEqual(instance, ok)
            self.assertEqual(instance, base(ok))
        for nok in self.invalid:
            xmls = '<base>%s</base>' % (nok,)
            self.assertRaises(pyxb_114.BadTypeValueError, CreateFromDocument, xmls)
            self.assertRaises(pyxb_114.BadTypeValueError, base, nok)
        
    def testRestr (self):
        for ok in self.restr_valid:
            xmls = '<base>%s</base>' % (ok,)
            instance = CreateFromDocument(xmls)
            self.assertEqual(instance, ok)
            self.assertEqual(instance, base(ok))
        for nok in self.invalid:
            xmls = '<base>%s</base>' % (nok,)
            self.assertRaises(pyxb_114.BadTypeValueError, CreateFromDocument, xmls)
            self.assertRaises(pyxb_114.BadTypeValueError, base, nok)
        
    def testAlt (self):
        xmls = '<altrestr>C</altrestr>'
        instance = CreateFromDocument(xmls)
        self.assertEqual(instance, 'C')
        self.assertEqual(instance, altrestr('C'))
        xmls = '<altrestr>A</altrestr>'
        self.assertRaises(pyxb_114.BadTypeValueError, CreateFromDocument, xmls)
        self.assertRaises(pyxb_114.BadTypeValueError, altrestr, 'A')

if __name__ == '__main__':
    unittest.main()
