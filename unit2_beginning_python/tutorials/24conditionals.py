# 24conditionals.py

import random

# Move the triple quotes downward to uncover each segment of code

"""

# The standard conditional statement is a single 'if'

a = 1
b = 2

if a < b:
	print('Yes, a < b')

# We can assign the expression (a < b) to a variable

c = a < b
print(c)
print(type(c))

# Variables of type 'bool' can be True or False
# Often we want to ask about multiple exclusive conditions
# For these situations, we use elif and else
# In the example below, we use the randint() function from the random module
# Try running the code several times

r = random.randint(1, 4) # generate a random number from 1 to 4
if   r == 1: print('A')
elif r == 2: print('C')
elif r == 3: print('G')
else:        print('T')

# Let's put that code above into a loop and generate some random sequence
# Note the use of end='' to prevent starting a new line

length = 10
for i in range(length):
	r = random.randint(1, 4) # generate a random number from 1 to 4
	if   r == 1: print('A', end='')
	elif r == 2: print('C', end='')
	elif r == 3: print('G', end='')
	else:        print('T', end='')
print()

# While on the subject of the random library, let's explore a little bit
print(random.random()) # a random floating point from 0 <= X < 1
print(random.choice('AAAAACGT')) # chooses a random letter (mostly A)

# The Boolean operators are 'and', 'or', and 'not'

# Print out all the positions that are A or T
# Note the use of 'or'

dna = 'ACGTGGGGT'
for i in range(len(dna)):
	nt = dna[i]
	if nt == 'A' or nt == 'T':
		print('W at', i) # W means A or T

# Let's print all the positions with a CG di-nucleotide
# Note the use of 'and'
# Note the -1 in the range() function to prevent running over the end

for i in range(len(dna) -1):
	if dna[i] == 'C' and dna[i+1] == 'G':
		print('CG at', i)

# Print out all letters that are not G
# Note the switch from range() to iterating through letters in the sequence

for nt in dna:
	if not nt == 'G':
		print(nt, end='')
print()

## You could also use the != operator

for nt in dna:
	if nt != 'G':
		print(nt, end='')
print()

# There is also greater-than-or-equal and less-than-or-equal operators
# These can be used to comapre characters as well as numbers

for nt in dna:
	if nt >= 'F': print(nt, end='')
print()

for nt in dna:
	if nt <= 'F': print(nt, end='')
print()

# The 'while' loop mixes a conditional with a loop
# Note the use of the 'break' statement to prevent this from going forever

i = 0
while (True): # this loop runs forever
	print('break yet?', i)
	i += 1
	if i > 5: break # this breaks the loop
print('broken at', i)

# The `continue` statement allows you to skip to the next iteration

for i in range(10):
	if i < 8: continue # this skips ahead to next iteration
	print('skipped until', i)

"""

