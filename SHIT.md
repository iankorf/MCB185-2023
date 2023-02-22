Shit Programming Practices
==========================

## if name dunder ##

If you're coming from another programming class (or maybe someplace on the
internet), you might have seen code that looks like the following:

```
# myprogram.py

def cool_function():
	stuff...

def main():
	stuff...

if __name__ == '__main__':
	main()
```

Let me explain why this programming idiom exists and also why it's the dumbest
shit ever.

In Python, and pretty much no other language, a file can be both a program
designed to be run by itself, or imported as a library. To run the file as a
program, you could do `python3 myprogram.py`. To import the file as a library,
your code needs an `import myprogram` statement. After such an import, you
could do something useful like:

```
myprogram.cool_function()
```

Some tasks, e.g. processing of command line arguments, should only occur in
programs and not libraries. You wouldn't want to import a library only to find
it accidentally mangled your command line. In order to protect such code from
running amok, you can put it in a `if __name__ == '__main__'` construct. Code
in this block is only run when the file is run as a program, not a library.

All of this sounds quite reasonable, but here's the problem: executables and
libraries are stored in completely different locations. Even though python
files **can** be used as both programs and libraries, they **shouldn't** be.
Programs belong in an executable path and libraries belong in a library path.
If you have some useful functions you want to share, put them in a library.
That's what libraries are for. Importing functions from executables breaks all
kinds of standards for no good reason.

The fact that `main()` is defined in `myprogram.py` suggests that another
python file could do the following:

```
import myprogram
myprogram.main()
```

Do you really want other python files, be they programs or other libraries,
calling the `main()` function from another file? No. Nobody wants that. So why
allow it by making a `main()` function?

But what if you have a python program and you don't want the code to be
accidentally imported? Isn't that a good reason to use the dunder? No. If you
don't want it imported, don't use the `.py` suffix. Most Unix programs don't
have a suffix. Does `ls` or `cat` have a suffix? No, and neither should
`myprogram` if it's an executable. Of course, if it's an executable, it needs
to have an interpreter directive on the first line and executable permissions.

```
#!/usr/bin/env python3
```

In this class, most of our scripts are named like `myprogram.py` with the
suffix, and we run them as `python3 myprogram.py`. Could these be accidentally
imported as libraries? Yes. Should we remove the suffix and make them actual
executables? This is an introductory programming class. We don't have to do
that. But once you start distributing your code to other people, yes, you
should make proper executables.

There is one okay reason to use the `if __name__ == '__main__'` dunder: test
code for libraries. All libraries should have unit tests. Small libraries can
pack their unit tests into the non-importable block and developers can run the
test code by itself. That said, there are much better unit-testing frameworks
in python, so even this isn't a compelling reason.
