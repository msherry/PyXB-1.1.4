import pyxb_114.bundles.opengis.sos_1_0 as sos
import pyxb_114.utils.utility
import sys
import traceback

# Import to define bindings for namespaces that appear in instance documents
import pyxb_114.bundles.opengis.sampling_1_0 as sampling
import pyxb_114.bundles.opengis.swe_1_0_1 as swe
import pyxb_114.bundles.opengis.tml

for f in sys.argv[1:]:
    print '------------------ %s' % (f,)
    xmls = pyxb_114.utils.utility.TextFromURI(f)
    try:
        instance = sos.CreateFromDocument(xmls)
        #print xmls
        print instance.toxml("utf-8")
    except Exception, e:
        print '%s failed: %s' % (f, e)
        traceback.print_exception(*sys.exc_info())
    
