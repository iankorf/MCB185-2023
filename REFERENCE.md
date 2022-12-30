Unix Quick Reference
====================

These are all of Unix commands we use in the course.


| Token | Meaning
|:------|:-------------------------------------------
| ^C    | send interrupt signal
| ^D    | send end-of-transmission signal
| ^Z    | send sleep signal
| tab   | tab-complete names
| `.`   | your current directory (see pwd)
| `..`  | your parent directory
| `~`   | your home directory (also $HOME)
| `*`   | wildcard - matches everything
| `|`   | pipe output from one command to another
| `>`   | redirect stdout to file
| `<`   | send a file as stdin


| Command   | Example       | Intent
|:----------|:--------------|:------------------------------------------------
| `cat`     | `cat > f`     | create file f and wait for keyboard (see ^D)
|           | `cat f`       | stream contents of file f to STDOUT
|           | `cat a b > c` | concatenate files a and b into c
| `cd`      | `cd d`        | change to relative directory d
|           | `cd ..`       | go up one directory
|           | `cd /d`       | change to absolute directory d
| `chmod`   | `chmod 644 f` | change permissions for file f in octal format
|           | `chmod u+x f` | change permissions for f the hard way
| `cp`      | `cp f1 f2`    | make a copy of file f1 called f2
| `cut`     | `cut -f 1 f`  | cut field 1 from file f
| `df`      | `df -h .`     | display free space on file system
| `diff`    | `diff f1 f2`  | shows differese between files f1 and f2
| `du`      | `du -h ~`     | display the sizes of your files
| `git`     | `git add f`   | start tracking file f
|           | `git commit`  | finished edits, ready to upload
|           | `git push`    | put changes into repository
|           | `git pull`    | retrieve latest documents from repository
|           | `git status`  | check on status of repository
| `grep`    | `grep p f`    | print lines with the letter p in file f
| `gzip`    | `gzip f`      | compress file f
| `gunzip`  | `gunzip f.gz` | uncompress file f.gz (see zcat)
| `head`    | `head f`      | display the first 10 lines of file f
|           | `head -2 f`   | display the first 2 lines of file f
| `history` | `history`     | display the recent commands you typed
| `htop`    | `htop`        | monitor resources, a variant of top
| `less`    | `less f`      | page through a file
| `ln`      | `ln -s f1 f2` | make f2 an alias of f1
| `ls`      | `ls`          | list current directory
|           | `ls -l`       | list with file details
|           | `ls -la`      | also show invisible files
|           | `ls -lta`     | sort by time instead of name
|           | `ls -ltaF`    | also show file type symbols
| `mkdir`   | `mkdir d`     | make a directory named d
| `more`    | `more f`      | page through file f (see less)
| `mv`      | `mv foo bar`  | rename file foo as bar
|           | `mv foo ..`   | move file foo to parent directory
| `nano`    | `nano`        | use the nano text file editor
| `pwd`     | `pwd`         | print working directory
| `rm`      | `rm f1 f2`    | remove files f1 and f2
|           | `rm -r d`     | remove directory d and all files beneath
|           | `rm -rf /`    | destroy your computer
| `rmdir`   | `rmdir d`     | remove directory d
| `sort`    | `sort f`      | sort file f alphabetically by first column
|           | `sort -n f`   | sort file f numerically by first column
|           | `sort -k 2 f` | sort file f alphabetically by column 2
| `sum`     | `sum f`       | create a checksum for a file
| `tail`    | `tail f`      | display the last 10 lines of file f
|           | `tail -f f`   | as above and keep displaying if file is open
| `tar`     | `tar -cf ...` | create a compressed tar-ball (-z to compress)
|           | `tar -xf ...` | decompress a tar-ball (-z if compressed)
| `time`    | `time ...`    | determine how much time a process takes
| `top`     | `top`         | display processes running on your system
| `touch`   | `touch f`     | update file f modification time (create if needed)
| `wc`      | `wc f`        | count the lines, words, and characters in file f
| `zcat`    | `zcat f.gz`   | stream compressed file f.gz to stdout
| `zless`   | `zless f.gz`  | page through compressed file f.gz



Python Concepts
===============

Summary of Python programming concepts by Unit

## Unit 2: Beginning Python ##

Variable types

```
None    a non-value, useful for debugging
int     integers
float   numbers with decimal points
str     'text' in single or double quotes
bool    False, True
```

Assignment operators

```
=     assignment not equality
+     addition, also used to concatenate strings
-     subtraction
*     multiplication, also used to make copies of strings
/     division
**    exponentiation
%     modulo (remainder after integer divide)
//    integer divide
()    parentheses force precedence, just like normal math
+=    auto-increment
-=    auto-decrement
*=    auto-multiplication
/=    auto-division
```

Comparison operators

```
==    equals
!=    not equal
>=    greater than or equal to
<=    less than or equal to
```

Boolean operators

```
and   true if both sides are true
or    true if either side is true
not   reverses Boolean value
```

Core functions

```
type()          returns the type of
int()           converts to integer
float()         converts to floating point number
str()           converts to string
len()           returns the length of an argument
range()         creates a sequence of numbers
range(a)        from 0 to a, not including a
range(a, b)     from a to b, not including b
range(a, b, c)  from a to b, not including b, with step size c
```

Slice syntax

```
s[0]       the first element of the container
s[0:1]     also the first element of the container
s[a:b]     a slice starting from a and not including b
s[a:]      a slice starting from a and going until the end
s[:b]      a slice starting at the beginning but ending before b
s[:]       the whole thing
s[::-1]    the whole thing, in reverse
```

Printing and f-strings

```
print('a')          writes to stdout and includes newline
print('a', end='')  writes to stdout and does not include newline
h = 'hello'
w = 'world'
print('{h} {w}')    f-strings interpolate variables into strings
print('{len(h)}')   also functions
```

Math library

```
math.pi        3.14159...
math.e         2.71828...
math.inf       represents infinity
math.nan       not a number (e.g. log(0))
math.ceil()    rounds up
math.floor()   rounds down
math.log()     transforms to log base e
math.log2()    transforms to log base 2
```

Random library

```
random.randint(a, b)  generates a random number from a to b (inclusive)
random.random()       generates a random number 0 <= X < 1
random.choice()       chooses a random value from a container
random.seed(a)        sets the random seed to integer a
```

Loops

```
for i in range(a):         iterate from 0 to a, not inclusive
for i in range(a, b):      iterate from a to b, not inclusive
for i in range(a, b, c):   as above, but in step size c
for nt in dna:             iterate over characters in string
break                      stop the loop now
continue                   go to the next iteration of the loop
while (logic):             iterates as long as logic is True
```


## Unit 3: Tuples and Lists ##

String methods

```
str.count()         counts the occurances of substrings
str.strip()         replaces characters at the ends (defaults to whitespace)
str.lstrip()        left-hand strip
str.rstrip()        right-hand strip, used frequently to remove newline
str.replace()       find and replace substrings
str.find()          report index of substring
str.rfind()         as above but from the right
str.upper()         convert to uppercase
str.lower()         convert to lowercase
str.isupper()       True if everything is uppercase
str.islower()       True if everything is lowercase
str.startswith()    True if starts with substring
str.endswith()      True if ends with substring
```

List operators

```
[]         creates an empty list
+          concatenates lists
*          initializes all elements of a list
in         checks for elements in a list (or other containers)
```

List functions

```
sum()         return the sum of all elements
min()         return the minimum value
max()         return the maximum value
list()        convert a string into a list
enumerate()   iterates through a list with a tuple of (index, value)
zip()         iterates through multiple lists simultaneously
```

List methods

```
list.sort()     changes the order of the list
list.append()   adds an element to the end of a list
list.pop()      removes the last element and returns it
list.insert()   inserts values at any position
```

Command line and checking

```
sys.argv        list of arguments, program name is sys.argv[0]
assert()        demands a condition or exits
math.isclose()  tests floating point bounds
try             sets up a test condition
except          evalutes when 'try' fails
raise           throws an error
```


## Unit 4: Functions and Files ##

Keywords

```
def             define a new function
return          return values from a function
with .. as ..   construct for opening and closing files
yield           briefly return values from a function
```

File functions

```
open()          create a file pointer
gzip.open()     create a file pointer to a compressed file
```

File methods

```
file.read()       read entire file into variable - not actually covered
file.readline()   read one line from a file
file.readlines()  iterate through all lines in a file
file.write()      write to a file
file.close()      close file pointer
```

Miscellany

```
os.getenv()          get environment variable contents
mcb185.read_fasta()  iterate through a fasta file
```


## Unit 5: Advanced Linux ##

New Python concepts in an otherwise Unix-themed lesson

```
import argparse     argparse is the standard CLI library
file.stdin          the file handle for stdin
subprocess.run()    run an external program and get its output
```


## Unit 6: Dictionaries and Regex ##

Dictionaries

```
{}                  the dictionary constructor
dict.keys()         get only the keys of a dictionary
dict.values()       get only the values of a dictionary
dict.items()        iterate through a tuple of (key, value)
del                 remove a dictionary key (and value)
in                  check if a key is in a dictionary
```

Regular expressions

```
import re           this is how it begins
re.search()         the usual way to look for patterns
match.group()       returning strings from matches
re.finditer()       iterate through matches
re.findall()        get a list of matches
```


## Unit 7: Complex Data Structures ##

JSON

```
import json
json.load()
json.dump()
```


## Unit 8: Final Projects ##

Various final projects ideas of varying difficutly.


## Unit 9: Unfinished Tales ##

Some important but uncovered topics.
