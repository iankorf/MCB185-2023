# 34listcomp.py

# Move the triple quotes downward to uncover each segment of code

# List comprehension
#    Looks elegant
#    Can be slightly confusing
#    Is common in Python - so you must know it when you see it
#    Isn't found in most languages, so consider it optional

"""

# Consider the following initialization code:

data = [] # emtpy list to be filled with append()
for i in range(10): data.append(0)
print(data)

# You can write this more succinctly with the * operator

data = [0] * 10
print(data)

# Another alternative is list comprehension

data = [0 for i in range(10)]
print(data)

# Here's a slightly more complex initialization

squares = []
for i in range(10):
	squares.append(i ** 2)
print(squares)

# List comprehension turns 3 lines into 1

squares = [i ** 2 for i in range(10)]
print(squares)

# You can also include a conditional
# First the longer syntax

square3 = []
for i in range(10):
	if i % 3 == 0:
		square3.append(i ** 2)
print(square3)

# Now list comprehension

square3 = [i ** 2 for i in range(10) if i % 3 == 0]
print(square3)

"""
