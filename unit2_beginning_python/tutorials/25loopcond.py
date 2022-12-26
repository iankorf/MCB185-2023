# 25loopcond.py

# Move the triple quotes downward to uncover each segment of code

"""

# The real power of programming comes from nesting loops and conditionals

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

for i in range(len(dna)):
	codon = dna[i:i+3]
	if codon == 'ATG':
		print(f'found potential start codon at {i+1}')

# Loops can be inside loops

for frame in range(3):
	print(f'reading frame {frame+1}')
	for position in range(frame, len(dna) -2, 3):
		codon = dna[position:position+3]
		print(codon, end=' ')
	print()

# You can nest loops and condtionals

for frame in range(3):
	for position in range(frame, len(dna) -2, 3):
		codon = dna[position:position+3]
		if codon == 'ATG':
			print(f'start codon at {position+1} in frame {frame+1}')
		elif codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
			print(f'stop codon at {position+1} in frame {frame+1}')

# Printing out a simple +1/-1 nucleotide scoring matrix

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
