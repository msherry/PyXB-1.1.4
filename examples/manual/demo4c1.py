import pyxb_114
import po4
import address
import pyxb_114.binding.datatypes as xs

po = po4.purchaseOrder(orderDate=xs.date(1999, 10, 20))
po.shipTo = address.USAddress('Alice Smith', '123 Maple Street', 'Anytown', 'AK', 12341)
po.billTo = address.USAddress('Robert Smith', '8 Oak Avenue', 'Anytown', 'AK', 12341)
po.items = pyxb_114.BIND(pyxb_114.BIND('Lapis necklace', 1, 99.95, partNum='833-AA'),
                     pyxb_114.BIND('Plastic necklace', 4, 3.95, partNum='833-AB'))
                
print po.toxml("utf-8")
