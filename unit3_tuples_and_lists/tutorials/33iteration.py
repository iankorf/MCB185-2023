# 33iteration.py

# Move the triple quotes downward to uncover each segment of code

p = [0.1, 0.2, 0.3, 0.4]

"""

# iterating over range()
sum1 = 0
for i in range(len(p)):
	sum1 += p[i]
print(sum1)

# iterating over values
sum2 = 0
for x in p:
	sum2 += x
print(sum2)

# enumerate() hands you a tuple of (index, value) with each iteration
for tup in enumerate(p):
	print(tup)

# as above but "unpacking" the tuple
for i, v in enumerate(p):
	print(i, v)

# zip() allows you to iterate over multiple containers simultaneously
string = 'abcd'
animals = ('ant', 'bat', 'cat', 'dog')
for a, b, c  in zip(p, string, animals):
	print(a, b, c)

# the "in" keyword is used for iteration
# it is also used to check for elements in a container (string, tuple, list)

if 'a' in string: print(f'a is in {string}')
if 'bat' in animals: print(f'bat is in {animals}')
if 0.3 in p: print(f'0.3 is in {p}')

"""
