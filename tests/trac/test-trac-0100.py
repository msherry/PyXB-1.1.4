import pyxb_114.binding.generate
import pyxb_114.utils.domutils
from xml.dom import Node

import os.path
xsd='''<?xml version="1.0" encoding="UTF-8"?>
 <schema xmlns="http://www.w3.org/2001/XMLSchema"
 xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    version="1.0" targetNamespace="http://www.example.com/test"
 xmlns:tgt="http://www.example.com/test"
    elementFormDefault="qualified" attributeFormDefault="unqualified">

  <complexType name="BaseRequestType" abstract="true">
    <attribute  name="attrib1"  type="xsd:string"/>
    <anyAttribute namespace="##any" processContents="skip"/>
  </complexType>

  <element name="Notification">
    <complexType>
      <complexContent>
        <extension base="tgt:BaseRequestType">
          <attribute name="attrib2" type="xsd:string" use="optional"/>
          <anyAttribute  namespace="##any" processContents="skip"/>
        </extension>
      </complexContent>
    </complexType>
  </element>
</schema>'''

code = pyxb_114.binding.generate.GeneratePython(schema_text=xsd)
#file('code.py', 'w').write(code)

rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_114.exceptions_ import *

import unittest

class TestTrac0100 (unittest.TestCase):
    xmls_base = '<tgt:Notification xmlns:tgt="http://www.example.com/test" attrib1="text"/>'
    def testBasic (self):
        instance = CreateFromDocument(self.xmls_base)
        self.assertEqual(instance.attrib1, "text")

    xmls_wc = '<tgt:Notification xmlns:tgt="http://www.example.com/test" attrib2="text2" xmlns:other="urn:other" other:attrib3="text3"/>'
    def testWildcard (self):
        instance = CreateFromDocument(self.xmls_wc)
        self.assertEqual(instance.attrib1, None)
        self.assertEqual(instance.attrib2, "text2")
        wca = instance.wildcardAttributeMap()
        self.assertEqual(1, len(wca))
        (attr, val) = wca.items()[0]
        self.assertEqual(attr.namespaceURI(), "urn:other")
        self.assertEqual(attr.localName(), "attrib3")
        self.assertEqual(val, "text3")


if __name__ == '__main__':
    unittest.main()
    
