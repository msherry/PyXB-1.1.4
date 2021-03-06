import unittest
import app
import common4app

import pyxb_114.utils.domutils

pyxb_114.utils.domutils.BindingDOMSupport.DeclareNamespace(app.Namespace, 'app')
pyxb_114.utils.domutils.BindingDOMSupport.DeclareNamespace(common4app.Namespace, 'common')

class Test (unittest.TestCase):
    def testApp (self):
        x = common4app.extended('hi', 'there')
        a = app.elt(x)
        self.assertEquals('<app:elt xmlns:app="urn:app" xmlns:common="urn:common"><app:xcommon><common:elt>hi</common:elt><common:extElt>there</common:extElt></app:xcommon></app:elt>', a.toxml("utf-8", root_only=True))

if '__main__' == __name__:
    unittest.main()
