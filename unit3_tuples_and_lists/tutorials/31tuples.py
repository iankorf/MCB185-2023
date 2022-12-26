# 31tuples.py

# Move the triple quotes downward to uncover each segment of code

"""

# Sometimes we want to work with multiple variables at the same time
# A convenient way to do this is a 'tuple'
# Any time you have comma separated values, you have a 'tuple'
# Tuples are often in parentheses but need not be

tup = 1, 2, 3
print(tup)      # all three values are contained in a single varible

tup = (1, 2, 3)
print(tup)      # same thing as above, parentheses optional

# Tuples can contain a mixture of variable types
# Note the output formatting
#    parentheses around all of the values
#    decimal point after the floating point value
#    strings are in quotes

tup = 1, 2.00, '3', 'four'
print(tup)


# You can use slice syntax, just like strings

print(tup[1:])
print(tup[:2])

# Tuples are immutable, meaning you can't change their contents

tup[1] = 'two'

"""
