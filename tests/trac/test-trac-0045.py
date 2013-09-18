import pyxb_114
import pyxb_114.xmlschema.structures
import pyxb_114.utils.domutils

from pyxb_114.exceptions_ import *

import unittest

def CreateDocumentationNode (content):
    xmls = '<xs:annotation xmlns:xs="%s"><xs:documentation>%s</xs:documentation></xs:annotation>' % (pyxb_114.namespace.XMLSchema.uri(), content)
    dom = pyxb_114.utils.domutils.StringToDOM(xmls)
    node = dom.documentElement
    nsc = pyxb_114.namespace.resolution.NamespaceContext.GetNodeContext(node)
    if nsc.targetNamespace() is None:
        nsc.finalizeTargetNamespace()
    return pyxb_114.xmlschema.structures.Annotation.CreateFromDOM(node)


class TestTrac_0045 (unittest.TestCase):
    def testSimple (self):
        self.assertEqual('hi there!', CreateDocumentationNode("hi there!").asDocString())
        self.assertEqual(' "hi there!" ', CreateDocumentationNode('"hi there!"').asDocString())
        self.assertEqual("''' docstring! '''", CreateDocumentationNode('""" docstring! """').asDocString())
        self.assertEqual("inner ''' docstring!", CreateDocumentationNode('inner """ docstring!').asDocString())

if __name__ == '__main__':
    unittest.main()
