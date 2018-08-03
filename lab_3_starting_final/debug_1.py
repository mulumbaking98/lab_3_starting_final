#
# debug_1.py:
#
# L3-1: We'll run this code in the PyCharm debugger together...
#

import random as r

var1 = r.randint(1,7)
var2 = r.randRange(1,7)

var3 = var1 * var2

var4 = var1 + var2

print (var1,var2,var3,var4)

sum = 0 # accumulator variable
for count in range(1,4):
    sum = sum + count # update accumulator

print ("the sum of 1..3 is:", sum)