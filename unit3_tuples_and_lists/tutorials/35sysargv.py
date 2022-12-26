# 35sysargv.py

import sys

# This tutorial is a little different from the others
# Try running this first as: python3 35sysargv.py

print(sys.argv) # the program name is the first item in the list

# Now run this as: python3 35sysargv.py 1 2 3.14
# ['34sysargv.py', '1', '2', '3.14']
# All of the other things on the command line are in the sys.argv list

# Move the triple quotes down to uncover the code

"""

# Here are two ways to navigate the command line arguments
print('for i in range starting at 1')
for i in range(1, len(sys.argv)):
	print(sys.argv[i])

print('for val in slice starting at 1')
for val in sys.argv[1:]:
	print(val)

# Note that command line arguments are text, not numbers
# You must convert the text to numbers if you want to do math

total = 0
for val in sys.argv[1:]:
	total += float(val)
print(total)

# Why is the total of (1, 2, 3.14) 6.140000000000001 and not 6.14?
# Floating point numbers have limited precision

"""
