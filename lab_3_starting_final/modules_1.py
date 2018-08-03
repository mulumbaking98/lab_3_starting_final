#
# modules_1.py =>
#
# L3-3 problem:
#
# Finish this so it (a) converts angle to radians r, and (b) prints out sin(r)**2 + cos(r)**2
#
# You'll need to look up the contents of the math module to see how to do (a)...
#

import math

angle = float(input("Enter an angle in degrees: "))

result = math.sin(math.radians(angle)) ** 2 + math.cos(math.radians(angle)) **2

print(result)

