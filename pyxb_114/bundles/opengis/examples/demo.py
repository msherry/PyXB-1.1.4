import pyxb_114.bundles.opengis.gml as gml
dv = gml.DegreesType(32, direction='N')
print dv.toxml("utf-8")
