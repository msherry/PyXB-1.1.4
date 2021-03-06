import pyxb_114.binding.generate
import pyxb_114.binding.datatypes as xs
import pyxb_114.binding.basis
import pyxb_114.utils.domutils

# Thanks to agrimstrup for this example

import os.path
xsd='''
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified" version="8 1.87" targetNamespace="URN:test-trac-0057">  

  <xsd:element name="ObsProject"> 
    <xsd:complexType> 
      <xsd:sequence> 
        <xsd:element name="assignedPriority" type="xsd:int"/>  
        <xsd:element name="timeOfCreation" type="xsd:string"/>  
      </xsd:sequence>  
      <xsd:attribute name="schemaVersion" type="xsd:string" use="required" fixed="8"/>  
      <xsd:attribute name="revision" type="xsd:string" default="1.87"/>  
      <xsd:attribute name="almatype" type="xsd:string" use="required" fixed="APDM::ObsProject"/> 
    </xsd:complexType> 
  </xsd:element>  


</xsd:schema>
'''

#file('schema.xsd', 'w').write(xsd)
code = pyxb_114.binding.generate.GeneratePython(schema_text=xsd)
#file('code.py', 'w').write(code)
#print code

rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_114.exceptions_ import *

import unittest

class TestTrac_0057 (unittest.TestCase):
    XMLS = '<ns1:ObsProject almatype="APDM::ObsProject" revision="1.74" schemaVersion="8" xmlns:ns1="URN:test-trac-0057"><ns1:timeOfCreation>2009-05-08 21:23:45</ns1:timeOfCreation></ns1:ObsProject>'

    def exec_toxml (self, v):
        return v.toxml("utf-8")

    def tearDown (self):
        pyxb_114.RequireValidWhenGenerating(True)
        pyxb_114.RequireValidWhenParsing(True)

    def testDefault (self):
        self.assertTrue(pyxb_114._GenerationRequiresValid)
        self.assertTrue(pyxb_114._ParsingRequiresValid)
        self.assertRaises(pyxb_114.UnrecognizedContentError, CreateFromDocument, self.XMLS)
        doc = pyxb_114.utils.domutils.StringToDOM(self.XMLS)
        self.assertRaises(pyxb_114.UnrecognizedContentError, CreateFromDOM, doc)
        
    def testDisable (self):
        pyxb_114.RequireValidWhenParsing(False)
        instance = CreateFromDocument(self.XMLS)
        self.assertRaises(pyxb_114.DOMGenerationError, self.exec_toxml, instance)
        doc = pyxb_114.utils.domutils.StringToDOM(self.XMLS)
        instance = CreateFromDOM(doc)
        pyxb_114.RequireValidWhenGenerating(False) 
        xml = instance.toxml("utf-8", root_only=True)
        self.assertEquals(xml, self.XMLS)

if __name__ == '__main__':
    unittest.main()
