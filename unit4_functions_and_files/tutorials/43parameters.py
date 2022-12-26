# 43parameters.py

# Move the triple quotes downward to uncover each segment of code

"""

# Functions usually have a fixed number of positional arguments
# But they may also take named arguments
# For example, you have seen this with print() statements

for c in 'acgt':
	print(c, end='-') # prints - instead of finishing line
print() # prints blank line at the end

# Your functions can also have named parameters with default values
# These are created when you define the function with name=value

def get_codons(seq, frame=0):
	codons = []
	for i in range(frame, len(seq) - 2, 3):
		codons.append(seq[i:i+3])
	return codons

tx = 'ATGCGATAGATACCAGATATAT'
print(get_codons(tx))           # no frame, assumed to be 0
print(get_codons(tx, frame=1))  # use named parameter

# Functions can take a variable number of parameters

def squares(*values):
	squared = []
	for v in values: squared.append(v * v)
	return squared

print(squares(1))
print(squares(1, 2, 0.5))

# You can even mix variable parameters and named parameters

def pow(*values, power=2):
	results = []
	for v in values: results.append(v ** power)
	return results

print(pow(1, 2, 0.5))
print(pow(1, 2, 0.5, power=3))

# You can even have variable named parameters...
# But that is a topic for another day

"""
