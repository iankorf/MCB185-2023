# 21math.py

# Move the triple quotes downward to uncover each segment of code

"""

# The typical mathematical operators behave as expected
# Try changing a and b
# Make sure you try b = 0 so you can observe the divide by zero error

a = 4
b = 3

add = a + b
sub = a - b
mul = a * b
div = a / b

print(add, sub, mul, div)

# Here are some other useful math operators

exp = a ** b   # a raised to the power of b
mod = a % b    # modulo: remainder after dividing a by b
idf = a // b   # integer division, then floor (round down)

print(exp, mod, idf)

# Python follows typical order of precedence (* / then + -)
# You can force precedence with parentheses, as expected

v1 = a + b * 0
v2 = (a + b) * 0

print(v1, v2)

# As a shortcut, you can do math and assignment at the same time

i = 0
i = i + 1
i += 1    # common short-cut for the line above
print(i)

# For complex math operations, you may need the math library

import math # import statements normally go at the top of a program

hyp = math.sqrt(a**2 + b**2) # Pythagoras, but also (a**2 + b**2)**0.5 works
print(hyp)

print(math.log2(0.25))

print(math.pi, math.floor(math.pi))
print(math.e, math.ceil(math.e))
print(math.inf, math.nan)

# Stirling's approximation of the log factorial
# Notice the use of \ to split a long line
# Try experimenting with n, including non-integer values (cool!)

n = 5
lnfac = 0.5 * math.log(math.tau) + (n + 0.5) * math.log(n) \
	- n + 1/(12 * n) - 1 / (360 * (n**3))
print(n, math.e**lnfac)
print(math.factorial(n))

"""
