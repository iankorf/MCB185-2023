# 23loops.py

import math

# Move the triple quotes downward to uncover each segment of code

"""

# The 'for' loop is the most common loop construct you will use
# Note the indentation of the print(i) statement below
# Code 'inside' loops must be indented
# The range() function creates a list of numbers from 0 to some limit
# Note that Python starts counting from 0 not 1
# Note that the limit is not included in the range, like the slice operator

for i in range(3):
	print(i)
print('- end of loop 1')

# The above is really a shortcut for the following code

for i in range(0, 3):
	print(i)
print('- end of loop 2')

# The second construct allows you to set where the loop starts

for i in range(1, 3):
	print(i)
print('- end of loop 3')

# You can also set a step size between each integer interval

for i in range(1, 10, 3):
	print(i)
print('- end of loop 4')

# You can also iterate over the characters of a string with "in"
# Most loops will use range() or in

s = 'ACGT'
for c in s:
	print(c)
print('- end of loop 5')

# An alternate way to do the same thing
# It's absolutely critical you understand the code above and below
# They do similar things with different strategies

for i in range(len(s)):
	print(i, s[i])
print('- end of loop 6')

# Everything that is tabbed-over is within the same loop
# Try removing the tab in front of i += 1 below

i = 0
for c in s:
	print(i, c)
	i += 1
print('- end of loop 7')

"""
