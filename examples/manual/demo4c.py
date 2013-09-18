# examples/manual/demo4c.py

import pyxb_114
import po4
import address
import pyxb_114.binding.datatypes as xs

po = po4.purchaseOrder(orderDate=xs.date(1999, 10, 20))
po.shipTo = address.USAddress('Alice Smith', '123 Maple Street', 'Anytown', 'AK', 12341)
po.billTo = address.USAddress('Robert Smith', '8 Oak Avenue', 'Anytown', 'AK', 12341)
                
pyxb_114.RequireValidWhenGenerating(False)
print po.toxml("utf-8")
