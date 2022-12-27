# 51wc.py

import argparse
import sys

# This program is similar to the standard Unix wc
# It has a proper Unix CLI from argparse
# It reads named files or stdin (use - for file name)
# It does not read multiple files or use blank file names, however

parser = argparse.ArgumentParser(description='Line, word, and byte counts.')
parser.add_argument('file', type=str, metavar='<path>', help='some file')
parser.add_argument('-c', '--bytes', action='store_true', help='byte count')
parser.add_argument('-l', '--lines', action='store_true', help='line count')
parser.add_argument('-w', '--words', action='store_true', help='word count')
arg = parser.parse_args()

if arg.file == '-': fp = sys.stdin
else:               fp = open(arg.file)

bc = 0
lc = 0
wc = 0
while True:
	line = fp.readline()
	if line == '': break
	bc += len(line)
	lc += 1
	wc += len(line.split())

print(lc, wc, bc)
