# 61regex.py

import re

# Move the triple quotes downward to uncover each segment of code

"""

string1 = "0123456789"

# Regular expressions (regex) are used to look for patterns in strings

pat1 = '5'

if re.search(pat1, string1): print(f'found {pat1} with regex')

# For the previous example, you could have used 'in'

if pat1 in string1: print(f'found {pat1} with in')

# The power of regexes is that you can make a pattern fuzzy
# Here are some simple rules
#    a     matches the letter a
#    B     matches the letter B
#    \w    matches any word symbol (letters, numbers, underscore)
#    \W    matches any non-word symbol
#    \d    matches any number
#    .     matches any character
#    \.    matches an actual dot
#    \w+   matches any number of word symbols
#    [ab]  matches the letter a or b
#    [a-d] matches the letters a, b, c, d
#    ()    used for capturing groups
#    \(    matches a left parenthese
# The rules for regex are quite long, so it's best to have a cheat sheat handy
# You should make your own, and write it in Markdown (that's homework)

string2 = 'Email me at atagcgaat@gmail.com if you want'
pat2 = '\w+@\w+.\w+'

if re.search(pat2, string2): print(f'found {pat2}')

# In order to retrieve the email, we need to store the match object
# Then we can retrieve it with match.group()

match = re.search(pat2, string2)
if match: print(match.group())

# You can assign subgroups using parentheses
# This allows you to pull out individual substrings

pat3 = '(\w+)\@(\w+.\w+)' # group 1 is username, group 2 is service
match = re.search(pat3, string2)
if match:
	print(match.group(1))
	print(match.group(2))

# If you want to find a pattern multiple times in a string, use finditer()

seq = 'ATCCGACTCCGTGCCGCCGCAGGGAGTGTGTCAAGTTACAGAGGCGCCGGAATCGGCCCCTGCGCTCCTCG'
HinF1 = 'GA[ACGT]TC' # restriction enzyme from Haemophilus influenzae

for match in re.finditer(HinF1, seq):
	print(match.group(), match.start(), match.end())

# For quick-n-dirty multiple matches, you may like findall()

print(re.findall(HinF1, seq))

# Sometimes you want to terminate a pattern when first found
# The intent here is to capture gene-b0001

data = 'ID=gene-b0001;Dbxref=ASAP:ABE-0000006,ECOCYC:EG11277,GeneID:944742;Name=thrL;gbkey=Gene;gene=thrL;gene_biotype=protein_coding;gene_synonym=ECK0001;locus_tag=b0001'

match = re.search('ID=(\S+);', data)
print(match.group(1))

# Unfortunately, the pattern \S+ doesn't terminate on the first semi-colon
# To change that behavior, we need a non-greedy match indicator
# This is the question mark symbol

match = re.search('ID=(\S+?);', data)
print(match.group(1))

"""
