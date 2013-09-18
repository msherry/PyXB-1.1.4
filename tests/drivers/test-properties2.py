import pyxb_114
import pyxb_114.binding.generate
import pyxb_114.utils.domutils
from xml.dom import Node

import pyxb_114.binding.basis
import os.path
schema_path = '%s/../schemas/test-collision.xsd' % (os.path.dirname(__file__),)
code = pyxb_114.binding.generate.GeneratePython(schema_location=schema_path, binding_style=pyxb_114.binding.basis.BINDING_STYLE_PROPERTY)
#file('code.py', 'w').write(code)

rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_114.utils import domutils

import unittest

class TestCollision (unittest.TestCase):

    def setUp (self):
        pyxb_114.binding.basis.ConfigureBindingStyle(pyxb_114.binding.basis.BINDING_STYLE_PROPERTY)

    def tearDown (self):
        pyxb_114.binding.basis.ConfigureBindingStyle(pyxb_114.binding.basis.DEFAULT_BINDING_STYLE)

    def testBasic (self):
        self.assertEqual(pyxb_114.binding.basis.CURRENT_BINDING_STYLE, pyxb_114.binding.basis.BINDING_STYLE_PROPERTY)
        instance = color(color_.red, color_=color_.green)
        self.assertEqual('<color color="green"><color>red</color></color>', instance.toxml("utf-8", root_only=True))
        instance.color = color_.blue
        self.assertEqual('<color color="green"><color>blue</color></color>', instance.toxml("utf-8", root_only=True))
        instance.color_ = color_.red
        self.assertEqual('<color color="red"><color>blue</color></color>', instance.toxml("utf-8", root_only=True))

if __name__ == '__main__':
    unittest.main()
