# 25loopcond.py

import random

# Move the triple quotes downward to uncover each segment of code

"""

# You can put loops inside of loops
# Make sure you have your indentation correct

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'
for frame in range(3):
	print(f'reading frame {frame+1}')
	for position in range(frame, len(dna) -2, 3):
		codon = dna[position:position+3]
		print(codon, end=' ')
	print()

# You can nest loops and condtionals
# Again, pay attention to your indentation

for frame in range(3):
	for position in range(frame, len(dna) -2, 3):
		codon = dna[position:position+3]
		if codon == 'ATG':
			print(f'start codon at {position} in frame {frame+1}')
		elif codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
			print(f'stop codon at {position} in frame {frame+1}')

# Here's a simple scoring matrix you might use for alignment

nts = 'ACGT'
print('\t', end='')
for nt in nts: print(nt, end='\t')
print()
for nt1 in nts:
	print(nt1, end='\t')
	for nt2 in nts:
		if nt1 == nt2: print('+1', end='\t')
		else: print('-1', end='\t')
	print()

"""
