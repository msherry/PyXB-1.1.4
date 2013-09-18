# Test individual attributes
import pyxb_114.binding.generate
import pyxb_114.utils.domutils
from xml.dom import Node

import os.path
# <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xml="http://www.w3.org/XML/1998/namespace">

xsd='''<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:complexType name="structure">
    <xs:attribute ref="xml:lang"/>
    <xs:attribute ref="xml:base"/>
  </xs:complexType>
  <xs:element name="instance" type="structure"/>
</xs:schema>'''

code = pyxb_114.binding.generate.GeneratePython(schema_text=xsd)
#file('code.py', 'w').write(code)

rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_114.exceptions_ import *

import unittest

class TestTrac0023 (unittest.TestCase):
    def testBasic (self):
        self.assertEqual(2, len(structure._AttributeMap))
        self.assertEqual(pyxb_114.binding.xml_.STD_ANON_lang, structure._AttributeMap[pyxb_114.namespace.XML.createExpandedName('lang')].dataType())
        self.assertEqual(pyxb_114.binding.datatypes.anyURI, structure._AttributeMap[pyxb_114.namespace.XML.createExpandedName('base')].dataType())

if __name__ == '__main__':
    unittest.main()
    
