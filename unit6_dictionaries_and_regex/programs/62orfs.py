# 62orfs.py

# Make a program that finds open reading frames in the E. coli genome
# Your program should read a fasta file
# There should be an optional minimum ORF size with a default value of 300 nt
# The output should be a table showing 4 columns
#     1. parent sequence identifier
#     2. begin coordinate
#     3. end coordinate
#     4. strand
#     5. first 10 amino acids of the protein

# Hint: use argparse, mcb185.read_fasta(), and mcb185.translate()
# Hint: don't use the whole genome for testing

# Note: your genes should be similar to those in the real genome

import argparse
import mcb185

parser = argparse.ArgumentParser(
	description='Count k-mers in a fasta file')
parser.add_argument('fasta', metavar='<fasta file>', type=str,
	help='path to file')
parser.add_argument('--minorf', required=False, type=int, default=300,
	metavar='<int>', help='minimum ORF length in nt [%(default)i]')
arg = parser.parse_args()

for name, seq in mcb185.read_fasta(arg.fasta):
	f = name.split()
	seqid = f[0]

	stop_used = {}
	for i in range(len(seq)):
		if seq[i:i+3] == 'ATG':
			for j in range(i+3, len(seq), 3):
				codon = seq[j:j+3]
				if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
					if j in stop_used: break
					stop_used[j] = True
					length = j - i + 1
					if length > arg.minorf:
						pep = mcb185.translate(seq[i:i+30])
						print(seqid, i+1, j+3, '+', pep)
					break

	stop_used = {}
	anti = mcb185.reverse_complement(seq)
	for i in range(len(anti)):
		if anti[i:i+3] == 'ATG':
			for j in range(i+3, len(anti), 3):
				codon = anti[j:j+3]
				if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
					if j in stop_used: break
					stop_used[j] = True
					length = j - i + 1
					if length > arg.minorf:
						pep = mcb185.translate(anti[i:i+30])
						print(seqid, len(anti)-j-2, len(anti)-i, '-', pep)
					break


"""
python3 62orfs.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz
NC_000913.3 108 500 - MVFSIIATRW
NC_000913.3 337 2799 + MRVLKFGGTS
NC_000913.3 2801 3733 + MVKVYAPASS
NC_000913.3 3512 4162 - MSHCRSGITG
NC_000913.3 3734 5020 + MKLYNLKDHN
NC_000913.3 3811 4119 - MVTGLSPAIW
NC_000913.3 5310 5738 - MKIPPAMANW
NC_000913.3 5683 6459 - MLILISPAKT
NC_000913.3 6529 7959 - MPDFFSFINS
NC_000913.3 7366 7773 + MKTASDCQQS
"""
