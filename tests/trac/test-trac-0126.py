import pyxb_114.binding.generate
import pyxb_114.utils.domutils
from xml.dom import Node

import os.path
xsd='''<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema">
  <element name="Element">
   <complexType name="tElement">
     <attribute name="Required" type="string" use="required"/>
     <attribute name="Optional" type="string" use="optional"/>
   </complexType>
  </element>
</schema>'''

code = pyxb_114.binding.generate.GeneratePython(schema_text=xsd)
#file('code.py', 'w').write(code)

rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_114.exceptions_ import *

import unittest

class TestTrac0126 (unittest.TestCase):
    def tearDown (self):
        pyxb_114.RequireValidWhenGenerating(True)
        pyxb_114.RequireValidWhenParsing(True)

    def testBasic (self):
        instance = Element()
        self.assertEqual(None, instance.Required)
        self.assertEqual(None, instance.Optional)
        
        pyxb_114.RequireValidWhenGenerating(False)
        self.assertEqual('<Element/>', instance.toDOM().documentElement.toxml("utf-8"))
        pyxb_114.RequireValidWhenGenerating(True)
        self.assertRaises(pyxb_114.MissingAttributeError, instance.toDOM)
        instance.Required = 'value'
        xmls = instance.toDOM().documentElement.toxml("utf-8");
        self.assertEqual('<Element Required="value"/>', xmls)


if __name__ == '__main__':
    unittest.main()
    
