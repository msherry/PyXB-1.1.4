from pyxb_114.exceptions_ import *
import unittest
import pyxb_114.binding.datatypes as xsd

class Test_ID (unittest.TestCase):
    def testValid (self):
        valid = [ 'schema', '_Underscore', '_With.Dot', 'With-Hyphen' ]
        for f in valid:
            self.assertEqual(f, xsd.ID(f))

    def testInvalid (self):
        invalid = [ '.DotFirst', 'With Spaces', 'With:Colon', 
                    'With?Illegal', '??LeadingIllegal', 'TrailingIllegal??',
                    '  LeadingSpace', 'TrailingSpace   ']
        for f in invalid:
            self.assertRaises(BadTypeValueError, xsd.ID, f)

if __name__ == '__main__':
    unittest.main()
