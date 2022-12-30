# 60translate.py

# Make a function that translates coding sequences into proteins
# The function should have an optional frame argument
# Put this into your mcb185 library as translate()

# Make a test program that imports mcb185 and calls mcb185.translate()
# No need for argparse and such, this is just to test the library function

# Below are some things that will help
# 1. The standard genetic code in a dictionary
# 2. C. elegans act-1 coding sequence
# 3. C. elegans ACT-1 protein

# Note: there is one nucleotide ambiguity signal in the cds
# Note: the ambituity is translated as X in the protein
# Note: the stop codon is represented by *

gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}

actin_cds = "\
atgtgtgacgacgaggttgccgctcttgttgtagacaatggatccggaatgtgcaaggcc\
ggattcgccggagacgacgctccacgcgccgtgttcccatccattgtcggaagaccacgt\
catcaaggagtcatggtcggtatgggacagaaggactcgtacgtcggagacgaggcccaa\
tccaagagaggtatccttaccctcaagtacccaattgagcacggtatcgtcaccaactgg\
gatgatatggagaagatctggcatcacaccttctacaatgagcttcgtgttgccccagaa\
gagcacccagtcctcctcactgaagccccactcaatccaaaggctaaccgtgaaaagatg\
acccaaatcatgttcgagaccttcaacaccccagccatgtatgtcgccatccaagctgtc\
ctctccctctacgcttccggacgtaccaccggagtcgtcctcgactctggagatggtgtc\
acccacaccgtcccaatctacgaaggatatgccctcccacacgccatcctccgtcttgac\
ttggctggacgtgatcttactgattacctcatgaagatccttaccgagcgtggttactct\
ttcaccaccaccgctgagcgtgaaatcgtccgtgacatcaaggagaagctctgctacgtc\
gccctcgacttcgagcaagaaatggccaccgccgcttcttcctcttccctcgagaagtcy\
tacgaacttcctgacggacaagtcatcaccgtcggaaacgaacgtttccgttgcccagag\
gctatgttccagccatccttcttgggtatggagtccgccggaatccacgagacttcttac\
aactccatcatgaagtgcgacattgatatccgtaaggacttgtacgccaacactgttctt\
tccggaggaaccaccatgtacccaggaattgctgatcgtatgcagaaggaaatcaccgct\
cttgccccatcaaccatgaagatcaagatcatcgccccaccagagcgcaagtactccgtc\
tggatcggaggatctatcctcgcttccctctccaccttccaacagatgtggatctccaag\
caagaatacgacgagtccggcccatccatcgttcaccgcaagtgcttctaa\
"

act_protein = "\
MCDDEVAALVVDNGSGMCKAGFAGDDAPRAVFPSIVGRPRHQGVMVGMGQKDSYVGDEAQ\
SKRGILTLKYPIEHGIVTNWDDMEKIWHHTFYNELRVAPEEHPVLLTEAPLNPKANREKM\
TQIMFETFNTPAMYVAIQAVLSLYASGRTTGVVLDSGDGVTHTVPIYEGYALPHAILRLD\
LAGRDLTDYLMKILTERGYSFTTTAEREIVRDIKEKLCYVALDFEQEMATAASSSSLEKX\
YELPDGQVITVGNERFRCPEAMFQPSFLGMESAGIHETSYNSIMKCDIDIRKDLYANTVL\
SGGTTMYPGIADRMQKEITALAPSTMKIKIIAPPERKYSVWIGGSILASLSTFQQMWISK\
QEYDESGPSIVHRKCF*\
"
