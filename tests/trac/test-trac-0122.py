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
     <attribute name="Prohibited" type="string" use="prohibited"/>
   </complexType>
  </element>
</schema>'''

code = pyxb_114.binding.generate.GeneratePython(schema_text=xsd)
#file('code.py', 'w').write(code)

rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_114.exceptions_ import *

import unittest

class TestTrac0122 (unittest.TestCase):
    def setRequired (self, instance, value):
        instance.Required = value

    def setOptional (self, instance, value):
        instance.Optional = value
        
    def setProhibitedNaive (self, instance, value):
        instance.Prohibited = value

    # Access to Prohibited is inhibited through Python properties;
    # bypass that for the purpose of testing
    def setProhibited (self, instance, value):
        attr = instance._AttributeMap.get('Prohibited')
        attr.set(instance, value)
        
    def getProhibited (self, instance):
        attr = instance._AttributeMap.get('Prohibited')
        return attr.value(instance)

    def testBasic (self):
        instance = Element()
        self.assertEqual(None, instance.Required)
        self.assertEqual(None, instance.Optional)
        self.assertEqual(None, self.getProhibited(instance))

        self.setRequired(instance, 'one')
        self.setOptional(instance, 'two')
        self.assertRaises(AttributeError, self.setProhibitedNaive, instance, 'three')
        self.assertRaises(pyxb_114.ProhibitedAttributeError, self.setProhibited, instance, 'three')
        self.assertEqual('one', instance.Required)
        self.assertEqual('two', instance.Optional)
        self.assertEqual(None, self.getProhibited(instance))

        instance.Optional = None
        self.assertRaises(pyxb_114.MissingAttributeError, self.setRequired, instance, None)
        self.setProhibited(instance, None)
        self.assertEqual('one', instance.Required)
        self.assertEqual(None, instance.Optional)
        self.assertEqual(None, self.getProhibited(instance))


if __name__ == '__main__':
    unittest.main()
    
