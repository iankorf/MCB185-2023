# 40aacomp.py

# Make a program that reports the amino acid composition in a file of proteins

# Hint: gzip.open(sys.argv[1], 'rt')

# Idea 1: use 20 named variables
# Idea 2: use a list

import sys
import gzip


aa = 'ACDEFGHIKLMNPQRSTVWY'
count = [0] * 20

total = 0
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp.readlines():
		if line.startswith('>'): continue
		for c in line:
			idx = aa.find(c)
			if idx == -1: continue
			count[idx] += 1
			total += 1

for c, n in zip(aa, count):
	print(c, n, n/total)

"""
python3 40aacomp.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
A 126893 0.09540992062268747
C 15468 0.011630276313049023
D 68213 0.051288856874968515
E 76890 0.057813029849388374
F 51796 0.03894503438781272
G 97830 0.07355766302725536
H 30144 0.022665053606190182
I 79950 0.06011382151721421
K 58574 0.04404136312131714
L 142379 0.10705373100437075
M 37657 0.02831402347559394
N 51896 0.03902022365800311
P 59034 0.044387233764192915
Q 59178 0.04449550631326707
R 73620 0.055354340714162724
S 76865 0.057794232531840774
T 71428 0.05370619191158945
V 94237 0.07085611254931476
W 20297 0.015261166170542798
Y 37628 0.028292218587238727
"""
