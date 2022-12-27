# 50argparse.py

import argparse

# This is a template you can use for processing command line arguments
# Change the names of the arguments to something descriptive
# Note that by giving type= the variables are converted to the proper type

# Commandline: python3 50argparse.py --r1 yo --r2 1 --r3 0.1
# Also try:
#	python3 50argparse.py
#	python3 50argparse.py --help

# setup
parser = argparse.ArgumentParser(description='Brief description of program.')

# positional arguments (always required)
parser.add_argument('file', type=str, metavar='<path>', help='some file')

# required named arguments
parser.add_argument('--r1', required=True, type=str,
	metavar='<str>', help='required string argument')
parser.add_argument('--r2', required=True, type=int,
	metavar='<int>', help='required integer argument')
parser.add_argument('--r3', required=True, type=float,
	metavar='<float>', help='required floating point argument')

# optional arguments with default parameters
parser.add_argument('--o1', required=False, type=str, default='hello',
	metavar='<str>', help='optional string argument [%(default)s]')
parser.add_argument('--o2', required=False, type=int, default=1,
	metavar='<int>', help='optional integer argument [%(default)i]')
parser.add_argument('--o3', required=False, type=float, default=3.14,
	metavar='<float>', help='optional floating point argument [%(default).3f]')

# switches
parser.add_argument('--switch', action='store_true',
	help='on/off switch')

# finalization
arg = parser.parse_args()

# testing
print(arg.file)
print(arg.r1, arg.r2, arg.r3)
print(arg.o1, arg.o2, arg.o3)
if arg.switch: print('switch on')
else:          print('switch off')

