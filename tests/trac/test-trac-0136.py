import types
import datetime
import pyxb_114.binding.generate
import pyxb_114.binding.datatypes as xs

import os.path
xsd='''<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:element name="timestamp" type="xsd:dateTime"/>
</xsd:schema>'''

#file('schema.xsd', 'w').write(xsd)
code = pyxb_114.binding.generate.GeneratePython(schema_text=xsd)
#file('code.py', 'w').write(code)

rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_114.exceptions_ import *

import unittest

class TestTrac_0136 (unittest.TestCase):
    def tearDown (self):
        pyxb_114.PreserveInputTimeZone(False)

    TS_p10 = '2012-05-14T16:36:02.157+10:00'
    TS_Z = '2012-05-14T06:36:02.157Z'
    TS_naive = '2012-05-14T06:36:02.157'
        
    Template = '<?xml version="1.0" ?><timestamp>%s</timestamp>'

    def genXML (self, ts):
        return self.Template % (ts,)

    def testNormalize (self):
        pyxb_114.PreserveInputTimeZone(False);
        i_p10 = CreateFromDocument(self.genXML(self.TS_p10))
        i_Z = CreateFromDocument(self.genXML(self.TS_Z))
        self.assertEqual(i_p10, i_Z)
        self.assertEqual(i_p10.tzinfo, i_Z.tzinfo)
        self.assertEqual(i_p10.xsdLiteral(), self.TS_Z)
        i_naive = CreateFromDocument(self.genXML(self.TS_naive))
        self.assertTrue(i_naive.tzinfo is None)

    def testUnnormalized (self):
        pyxb_114.PreserveInputTimeZone(True);
        i_p10 = CreateFromDocument(self.genXML(self.TS_p10))
        i_Z = CreateFromDocument(self.genXML(self.TS_Z))
        self.assertEqual(i_p10, i_Z)
        self.assertNotEqual(i_p10.tzinfo, i_Z.tzinfo)
        self.assertEqual(i_p10.xsdLiteral(), self.TS_p10)
        i_naive = CreateFromDocument(self.genXML(self.TS_naive))
        self.assertTrue(i_naive.tzinfo is None)

if __name__ == '__main__':
    unittest.main()
