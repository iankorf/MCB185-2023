# 30methods.py

# Move the triple quotes downward to uncover each segment of code

"""

# Previously, we have use "function syntax", which has the form
#    function(data)
# Python also uses "method syntax", which has the form
#    data.method()
# Method syntax is also sometimes called object syntax
#    object.method()

s = 'ACGT'
print(len(s))       # function syntax
print(s.isupper())  # method syntax

# We have seen a few case of "dots" before but these weren't object methods
# However, they were object syntax
# math.log2()        # a class function
# math.e constant    # a class constant

# Let's get some practice using method syntax with strings
# Note that all of these methods return a new string
# That is, they don't change the original object

s = '>>>>>ACGT<<<<<'
print(s)

# count() returns the number of times it finds a substring
print(s.count('>'))
print(s.count('>>'))

# lstrip(), rstrip), and strip() remove characters at the ends of strings
# by default this is whitespace, but can be multiple characters

print(s.lstrip('>'))
print(s.rstrip('<'))
print(s.strip('<>'))

# replace() exchanges characters or strings
print(s.replace('>>', '.'))




# upper() and lower() convert case
# isupper() and islower() check for case
print(s.lower())
print(s.islower())

# find() returns the index of the first substring it finds
# rfind() searches backwards
# they both return -1 if they don't find anything
print(s.find('AC'))
print(s.rfind('AC'))
print(s.find('Z'))

# startswith() and endswith() search the start and end of strings
print(s.startswith('>'))
print(s.endswith('>'))

"""
