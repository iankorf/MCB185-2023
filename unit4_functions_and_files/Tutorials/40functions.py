# 40functions.py

import math
import random

# Move the triple quotes downward to uncover each segment of code

"""

# A function is created with the def keyword, a name, and a colon
# All of the statements in a function are indented
# Functions are generally declared at the top of the file
# In this tutorial, they are spread throughout the file

def greeting():
	print('hello')

greeting()

# Functions can take arguments

def greeting1(person):
	print(f'hello {person}')

greeting1('Ian')

# Functions can take multiple arguments

def greeting2(person1, person2):
	print(f'hello {person1} and {person2}')

greeting2('Nigel', 'Derek')

# Functions generally return a value

def anti(dna):
	seq = ''
	for c in dna[::-1]:
		if   c == 'A': seq += 'T'
		elif c == 'C': seq += 'G'
		elif c == 'G': seq += 'C'
		elif c == 'T': seq += 'A'
		else: seq += 'N'
	return seq

s = 'AAAACGTA'
print(s, anti(s))

# Functions can return multiple values, as a tuple

def composition(dna):
	a = dna.count('A') / len(dna)
	c = dna.count('C') / len(dna)
	g = dna.count('G') / len(dna)
	t = dna.count('T') / len(dna)
	return a, c, g, t

nts = composition(s) # returns a tuple
print(nts)
a, c, g, t = composition(s) # unpacking the tuple in named variables
print(a, c, g, t)

# Functions can call themselves!
# This is called recursion
# Recursion can wind your brain into knots at first

def factorial(n):
	if   n == 0: return 1
	elif n == 1: return n
	else:        return n * factorial(n-1)

print(factorial(0), factorial(5))

"""
