import sys
import pyxb_114.xmlschema
import pyxb_114.binding.generate
import pyxb_114.utils.domutils

files = sys.argv[1:]
if 0 == len(files):
    files = [ 'pyxb_114/standard/schemas/XMLSchema.xsd' ]

rv = pyxb_114.binding.generate.GeneratePython(schema_location=files[0], generate_facets=True)
print '''# ---------
%s
# -------------''' % (rv,)
