# 32lists.py

# Move the triple quotes downward to uncover each segment of code

"""

# Lists are like tuples, but are mutable (you can change their contents)
# Create lists with square brackets instead of (optional) parentheses

arr = [1, 2.0, 'three']
print(arr)

# You can change the content of each item in a list

arr[2] = 3
print(arr)

# You can slice a list, just like a string or tuple

print(arr[0:2])

# You can change the length of a list with append(), pop(), and insert()

arr.append('four') # adds 'four' to the end of a list
print(arr)

last = arr.pop() # removes the last element of a list and returns it
print(last, arr)

arr.insert(2, 'ok')  # inserts 'ok' at position 2
print(arr)

# Many lists contain numbers, like the following probability distribution

p = [0.2, 0.1, 0.4, 0.3]

# There are some convenient functions for working with lists: sum, min, max
print(p, sum(p), min(p), max(p))

# sorting is done with the sort() function
p.sort()
print(p)

# sorting also works with text
strings = ['dog', 'cat', 'mouse', 'elephant']
strings.sort()
print(strings)

# you can combine lists with the + sign
stuff = p + strings
print(stuff)

# you can find the first position of an item in the list with index()
print(stuff.index('cat'))
# print(stuff.index('foo')) # it's an error if it doesn't find it

# lists with mixed types don't sort though
#stuff.sort()

# Strings can be split into lists
t = 'the quick brown fox jumps over the lazy dog'
words = t.split() # default split is on spaces
print(words)

# Lists can be joined into strings
t = '-'.join(words)
print(t)

# Strings can be split into letters
dna = 'ACGT'
nts = list(dna)
print(dna, nts)

# Lists are often initialized empty
todo = []
todo.append('laundry')
print(todo)

# Lists are often initialized with a bunch of zeros
count = [0] * 20
print(count)

"""
