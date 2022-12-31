# 62timer.py

import random
import sys
import time

# Move the triple quotes downward to uncover each segment of code

"""

# Dictionaries are much faster for lookups than lists
# Here's a demonstration

# First, let's create a list of random peptides with random values
peplen = 10
pepcount = 100000
peptides = []
values = []

# At the same time, we'll create a dictionary of key, value pairs
pepdict = {}

for i in range(pepcount):
	pep = ''
	for j in range(peplen):
		pep += random.choice('ACDEFGHIKLMNPQRSTVWY')
	peptides.append(pep)
	val = (random.random())
	values.append(val)
	pepdict[pep] = val

# Now let's search and see how long it takes
print(f'searching {pepcount} items', file=sys.stderr)

t0 = time.time()
for i in range(pepcount):
	pep = random.choice(peptides)
	if pep in peptides:
		idx = peptides.index(pep)
		print(pep, values[idx])
list_time = time.time() - t0

print(f'list: {list_time} seconds', file=sys.stderr)

# Now for the dictionary
t0 = time.time()
for i in range(pepcount):
	pep = random.choice(peptides)
	if pep not in pepdict: continue
	print(pep, pepdict[pep])
dict_time = time.time() - t0
print(f'dict: {dict_time} seconds', file=sys.stderr)

print(f'dict is {list_time/dict_time} times faster', file=sys.stderr)

# Now change pepcount to a higher value, like 100, 1000, or more
# Also redirect your output to /dev/null so you only see stderr
# python3 62timer.py > /dev/null

# | size | speed |
# |:----:|:-----:|
# |  100 |     2 |
# | 1000 |    16 |
# |  10K |   130 |
# | 100K |  1380 |
# |   1M |  N.D. |

"""
