# 12text.py

# Move the triple quotes downward to uncover each segment of code

"""

# Variables with text are called strings

s = 'ACGT' # a string

# Square brackets let you access sub-strings as 'slices'
# Follow closely below, because the endpoints can be confusing
# The first number before : is the starting index, which starts at zero
# The second number after : is one larger than the last index

print(s, s[0], s[1])
print(s[2], s[2:3], s[2:4], s[2:5])

# You can also do the following shortcuts

print(s[:2]) # the 0 is implict on the left
print(s[2:]) # the end of the string is implicit on the right

# The + operator concatenates strings

s = s + 'N'
s += 'n'   # note that += is a shorthand for s = s +, just like in math
print(s)

# The * operator repeats strings

s *= 3
print(s)

# The len() function returns the length of a string
# Some function like len() return values, others like print() do not

print(len(s))

# There are several ways to format strings

txt = 'Ian'
num = 3/11

# Previously, we have used the print() function with commas

print(txt, num)

# What if we want to control the way the text looks?
# For example, what if we want exactly 3 decimal places?
# There are 3 distinct ways to format strings in python

# Method 1: printf-style formatting
# printf() is the name of an old C function, but not Python
# The syntax is well-known among old-school programmers

print('%s %.3f' % (txt, num))                # %s string, %f float
print('%s %.3f %d %e' % (txt, num, 2.1, .1)) # %d integer, %e scientific

# Method 2: str.format()
# Strings are objects with built-in functions (which are called methods)
# upper() and lower() are some simple examples of string methods
# When using object syntax, the function comes after the variable

print(txt.upper(), txt.lower())

# The format() method is a powerful way to control string formatting

print('{} {}'.format(txt, num))
print('{} {:.3f}'.format(txt, num))

# Method 3: f-strings
# f-strings are the newest and best way to format strings
# f-strings interpolate variables and other statements inside curly brackets

print(f'{txt} {num}')
print(f'{txt} {num:.3f}')

# You can even interpolate python code

print(f'{2+2} {1/7:.5f} {len(txt)}')

# The examples here are but the tip of a very large iceberg
# Each formatting method has many more options
# Check documentation online for more information
# Use f-strings instead of the other methods

"""
