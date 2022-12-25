# 42generators.py

import random

# Move the triple quotes downward to uncover each segment of code

"""

# There are times when you want to generate a bunch of data
# Here's a function that returns a list of random sequences

def randseq(count, length):
	seqs = []
	for i in range(count):
		seq = []
		for j in range(length):
			seq.append(random.choice('ACGT'))
		seqs.append(''.join(seq))
	return seqs

seqs = randseq(5, 7)
print(seqs)

# A list of a few sequences isn't a big deal
# But imagine we want a function to create many large sequences
# The following code may cause your computer to run out of memory!
# Kill it with control-C and comment it out!

seqs = randseq(3000, 1000000) # size of human genome in 1M chunks

# Holding all of those sequences in memory is a lot of work
# Instead of creating all sequences up-front, generate them as needed
# Any function with a 'yield' statement is a generator function
# A 'yield' temporarily stops execution to return value(s)
# Generators improve performance by reducing memory

def seqgen(count, length):
	for i in range(count):
		seq = []
		for j in range(length):
			seq.append(random.choice('ACGT'))
		yield ''.join(seq)

# This works, but it takes a long time to run
# So ^C it and comment it out after trying it

for seq in seqgen(3000, 1000000): print(seq)

# In addition to generator functions, there are generator expressions
# These look a lot like list comprehension
# Except with parentheses instead of square brackets
# This is advanced-optional

for r in (random.random() for i in range(10)):
	print(r)

"""
