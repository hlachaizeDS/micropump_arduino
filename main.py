from DispenseUnit_Arduino import *


COM_PORT="COM8"

pump_1=DispenseUnit_Arduino('fakeparent',COM_PORT)
#pump_1.init()
for i in range(100):
    print(i)
    pump_1.dispense(10)
