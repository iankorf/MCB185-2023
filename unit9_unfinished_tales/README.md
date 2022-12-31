Unit 9: Unfinished Tales
========================

There are several important topics that are not covered, but are very important
for the aspiring bioinformatics programmer.

+ Doc strings
+ Unit tests
+ Functional tests
+ Software distribution
+ Object-oriented programming

## Doc Strings ##

Documentation is an essential part of programming. In this course, we learned
about usage statements, which every program should have. In addition, programs
should have other forms of documentation such as tutorials. Libraries should
have application programming interface (API) documentation that describes the
intent, input, and output of every function.

Doc-strings are big, triple-quoted strings of API documentation that sit right
next to their function. A doc-string reader then reads all of the doc-strings
in the library and makes a tidy HTML or PDF book out of it.

There is more than one standard for docs-strings and doc-string processors. At
some point, this section will have some examples...

## Unit Tests ##

Unit tests are sort of like the rubber gloves of software engineering. Just as
you wouldn't start working at the bench without rubber gloves, you shouldn't
start developing programs without unit tests.

A unit test is designed to test the smallest unit of calculation. If you have a
function that sums up a list, the unit test would check that the output of the
function is exactly what it's supposed to be. There can be many unit tests for
a function, for example, testing various kinds of input, some of which is
intended to be erroneous.

There is more than one standard for unit tests in python. At some point, this
section will have some examples...

## Functional Tests ##

A functional test is a lot like a unit test, except it's designed to test how
various components work together. For example, it could test the input and
output of an entire program rather than the 20 functions inside the program.

There are several ways to make functional tests. At some point, this section
will have some examples...

## Software Distribution ##

There are many ways to distribute software. The old-fashioned way is with a
tar-ball containing all of the sources, documentation, and testing data. Today,
lots of software is distributed via GitHub (or equivalent). You can also
distribute software via package manager like Conda. The Python way to
distribute programs and libraries is PyPi, the Python Package Index.

This is a much more complex topic than you might imagine.

## Object-Oriented Programming ##

We used objects at various times during the course, but didn't make our own
classes and objects. It's not necessary, but the syntactic sugars is nice
for your users. The Python way is a little ugly, but worth discussing...
some day.

