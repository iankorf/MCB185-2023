# 30hwin.py

# Write a program that computes the entropy of a DNA sequence in a window
# Window size is 11 nt
# Output with 4 significant figures
# https://en.wikipedia.org/wiki/Entropy_(information_theory)


seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11


"""
python3 30hwin.py
0 ACGACGCAGGA 1.5726
1 CGACGCAGGAG 1.5395
2 GACGCAGGAGG 1.4354
3 ACGCAGGAGGA 1.4949
4 CGCAGGAGGAG 1.4354
5 GCAGGAGGAGA 1.3222
6 CAGGAGGAGAG 1.3222
7 AGGAGGAGAGT 1.3222
8 GGAGGAGAGTT 1.4354
9 GAGGAGAGTTT 1.5395
10 AGGAGAGTTTC 1.8676
11 GGAGAGTTTCA 1.8676
12 GAGAGTTTCAG 1.8676
13 AGAGTTTCAGA 1.8676
14 GAGTTTCAGAG 1.8676
15 AGTTTCAGAGA 1.8676
16 GTTTCAGAGAT 1.8676
17 TTTCAGAGATC 1.9363
18 TTCAGAGATCA 1.9363
19 TCAGAGATCAC 1.9363
20 CAGAGATCACG 1.8676
21 AGAGATCACGA 1.7899
22 GAGATCACGAA 1.7899
23 AGATCACGAAT 1.8586
24 GATCACGAATA 1.8586
25 ATCACGAATAC 1.7899
26 TCACGAATACA 1.7899
27 CACGAATACAT 1.7899
28 ACGAATACATC 1.7899
29 CGAATACATCC 1.8231
30 GAATACATCCA 1.7899
31 AATACATCCAT 1.5395
32 ATACATCCATA 1.5395
33 TACATCCATAT 1.5726
34 ACATCCATATT 1.5726
35 CATCCATATTA 1.5726
36 ATCCATATTAC 1.5726
37 TCCATATTACC 1.5726
38 CCATATTACCC 1.5395
39 CATATTACCCA 1.5726
40 ATATTACCCAG 1.8676
41 TATTACCCAGA 1.8676
42 ATTACCCAGAG 1.9363
43 TTACCCAGAGA 1.9363
44 TACCCAGAGAG 1.8676
45 ACCCAGAGAGA 1.5395
46 CCCAGAGAGAG 1.5726
"""