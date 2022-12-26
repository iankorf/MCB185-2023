# 44libraries.py

# Move the triple quotes downward to uncover each segment of code

"""

# You have used various libraries before (math, sys, gzip)
# Here's how you get to environment variables

import os
home = os.getenv('HOME')
print(home)

# But have you ever seen the guts of a library?
# Some of them are just python code you could write yourself
# Take a look at the mcb185.py library in the tutorials directory

import mcb185

# The read_fasta() function iterates through a fasta file
# It returns the definition line and sequence in a tuple

# The code below prints the identifier and first 20 aa of every E.coli protein

prot = 'DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz'

for defline, seq in mcb185.read_fasta(f'{home}/{prot}'):
	words = defline.split()
	name = words[0]
	print(name, seq[0:20])

"""
