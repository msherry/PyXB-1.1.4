import pyxb_114.binding.generate
import pyxb_114.utils.domutils
from xml.dom import Node

import os.path
xsd='''<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
	<xs:element name="elt" type="xs:string"/>
	<xs:complexType name="empty"/>
	<xs:complexType name="simple">
		<xs:simpleContent>
			<xs:extension base="xs:string"/>
		</xs:simpleContent>
	</xs:complexType>
	<xs:complexType name="complex">
		<xs:sequence>
			<xs:element ref="elt"/>
		</xs:sequence>
	</xs:complexType>
</xs:schema>'''

code = pyxb_114.binding.generate.GeneratePython(schema_text=xsd)
#print code

rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_114.exceptions_ import *

import unittest

class TestTrac0021 (unittest.TestCase):
    """Presence of a wildcard in a sequence model group causes other
    elements in that group to not be generated."""
    def testEmpty (self):
        instance = empty()
        self.assertRaises(pyxb_114.NotSimpleContentError, lambda: instance.value())
        self.assertRaises(pyxb_114.NotComplexContentError, lambda: instance.content())

    def testSimple (self):
        instance = simple("hi")
        self.assertEqual("hi", instance.value())
        self.assertRaises(pyxb_114.NotComplexContentError, lambda: instance.content())

    def testComplex (self):
        instance = complex("hi")
        self.assertRaises(pyxb_114.NotSimpleContentError, lambda: instance.value())
        elt = instance.content()[0]
        self.assertTrue(isinstance(elt, basestring))
        self.assertEqual("hi", elt)


if __name__ == '__main__':
    unittest.main()
    
