import pyxb_114.binding.generate
import pyxb_114.utils.domutils
from xml.dom import Node

import os.path
xsd='''<?xml version="1.0" encoding="UTF-8"?>
<xs:schema
    xmlns:xs="http://www.w3.org/2001/XMLSchema">

	<xs:simpleType name="intList">
		<xs:list itemType="xs:int"/>
	</xs:simpleType>

	<xs:complexType name="tSingle">
		<xs:sequence>
			<xs:element name="li" type="intList" maxOccurs="1"/>
		</xs:sequence>
	</xs:complexType>

</xs:schema>'''

code = pyxb_114.binding.generate.GeneratePython(schema_text=xsd)
#file('code.py', 'w').write(code)

rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_114.exceptions_ import *

import unittest

class TestTrac0110 (unittest.TestCase):
    def tearDown (self):
        pyxb_114.RequireValidWhenGenerating(True)
        pyxb_114.RequireValidWhenParsing(True)

    def testWithValidation (self):
        expect = '<tSingle><li>1 2 3</li></tSingle>'
        s = tSingle()
        pyxb_114.RequireValidWhenGenerating(True)
        s.li = intList([1,2,3])
        self.assertEqual(s.toxml("utf-8", root_only=True), expect)
        pyxb_114.RequireValidWhenGenerating(False)
        s.li = intList([1,2,3])
        self.assertEqual(s.toxml("utf-8", root_only=True), expect)

if __name__ == '__main__':
    unittest.main()
    
