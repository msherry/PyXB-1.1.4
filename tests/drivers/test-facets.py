import pyxb_114.binding.generate
import pyxb_114.utils.domutils
from xml.dom import Node

import os.path
schema_path = '%s/../schemas/test-facets.xsd' % (os.path.dirname(__file__),)
code = pyxb_114.binding.generate.GeneratePython(schema_location=schema_path)

rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_114.exceptions_ import *

import unittest

class TestFacets (unittest.TestCase):
    def testQuantity (self):
        xml = '<quantity xmlns="URN:test-facets">35</quantity>'
        instance = CreateFromDOM(pyxb_114.utils.domutils.StringToDOM(xml).documentElement)
        self.assertEqual(35, instance)
        for (k,v) in globals().items():
            if k.startswith('_STD_ANON'):
                break
        self.assertEqual(v.typeDefinition(), type(instance))
        self.assertRaises(Exception, v, -52)
        self.assertRaises(Exception, v, 100)

if __name__ == '__main__':
    unittest.main()
    
