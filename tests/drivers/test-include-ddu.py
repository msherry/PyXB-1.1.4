import pyxb_114.binding.generate
import pyxb_114.utils.domutils

import os.path
schema_path = '%s/../schemas/test-include-ddu.xsd' % (os.path.dirname(__file__),)
code = pyxb_114.binding.generate.GeneratePython(schema_location=schema_path)
#file('code.py', 'w').write(code)
rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_114.exceptions_ import *

import unittest

class TestIncludeDD (unittest.TestCase):
    def testDefault (self):
        xmls = '<entry xmlns="%s"><from>one</from><to>single</to></entry>' % (Namespace.uri(),)
        # Default namespace applies to from which should be in no namespace
        self.assertRaises(pyxb_114.UnrecognizedContentError, CreateFromDocument, xmls.encode('utf-8'))

    def testExplicit (self):
        xmls = '<ns:entry xmlns:ns="%s"><from>one</from><ns:to>single</ns:to></ns:entry>' % (Namespace.uri(),)
        instance = CreateFromDocument(xmls.encode('utf-8'))
        self.assertEqual(english.one, instance.from_)

if __name__ == '__main__':
    unittest.main()
    
