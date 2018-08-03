#
# L3-5: find the logical bug in the following program
#
import math
number = int (input("Enter number of ints to process: "))

max_so_far = -math.inf #fix bug

for count in range(number):

    next_int = int(input("Enter next integer: "))
    max_so_far = max(max_so_far,next_int) # note the built-in max()

print("Largest entered is:", max_so_far)
