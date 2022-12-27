# 52run.py

# There are times you want to run another program, and read its output
# There are several ways to do this in python!
# Here is my favorite way

import subprocess

for line in subprocess.run('ls -la', shell=True,
		capture_output=True).stdout.decode().split('\n'):
	print('yay', line)
