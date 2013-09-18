import pyxb_114
import unittest
import pyxb_114.binding.datatypes as xsd

class Test_token (unittest.TestCase):
    Cases = [ ('Internal spaces are ok', None),
                  ("with\nnewline", 'with newline'),
                  ("with\rreturn", 'with return'),
                  ("with\ttab", 'with tab'),
                  ("\n\nleading newline", 'leading newline'),
                  ("trailing newline\n\n", 'trailing newline'),
                  (' LeadingSpace', 'LeadingSpace'),
                  ('TrailingSpace ', 'TrailingSpace'),
                  ('Internal  Multiple Spaces', 'Internal Multiple Spaces'),
                  ]

    def testValid (self):
        for (lexical, value) in self.Cases:
            if value is None:
                value = lexical
            self.assertEqual(value, xsd.token(value))
            self.assertEqual(value, xsd.token(lexical, _from_xml=True))

    def testInvalid (self):
        for (lexical, value) in self.Cases:
            if value is not None:
                self.assertRaises(pyxb_114.BadTypeValueError, xsd.token, lexical)

if __name__ == '__main__':
    unittest.main()
