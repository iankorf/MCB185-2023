# 36errors.py

import math
import sys

# Move the triple quotes downward to uncover each segment of code

"""

# Once you start interacting with users, you will get erroneous input

# What if your program expects a probability distribution and the
# values don't add up to 1.0?

probs = [0.1, 0.2, 0.3, 0.5] # ooops
print(sum(probs))

# One way to handle this is for your program to exit

#assert(sum(probs) == 1) # comment this line out to continue

# But what about rounding errors?
# You should never ask for floating point numbers to be equal to a value
# Instead, make sure the numbers are close enough

probs = [0.1, 0.2, 0.3, 0.400000000001]
assert(math.isclose(sum(probs), 1.0)) # using default tolerance
assert(math.isclose(sum(probs), 1.0, abs_tol=0.01)) # choose your tolerance

# To check if something works, use "try"
# If the trial fails, the "except" clause is executed
# Note: errors and warnings are generally sent to stderr

probs = [0.1, 0.2, 0.3, 'zero point 4']
for val in probs:
	try:
		p = float(val)
	except:
		print(f'cannot convert {val} to a number', file=sys.stderr)


# If you want the program to terminate, you can raise an error

for val in probs:
	try:
		p = float(val)
	except:
		raise ValueError(f'cannot convert {val} to a number')

"""
