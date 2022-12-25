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

"""
