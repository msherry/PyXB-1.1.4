import pyxb_114.binding.generate
import pyxb_114.utils.domutils

import os.path

from pyxb_114.exceptions_ import *

import unittest

class TestIncludeDD (unittest.TestCase):
    def testDefault (self):
        schema_path = '%s/../schemas/test-include-ad.xsd' % (os.path.dirname(__file__),)
        self.assertRaises(pyxb_114.SchemaValidationError, pyxb_114.binding.generate.GeneratePython, schema_location=schema_path)

if __name__ == '__main__':
    unittest.main()
    
