Unit 2: Beginning Python
========================

## Outline ##

+ Variables - different types for different flavors
+ Math - it works like you expect, mostly
+ Strings - text, and the critical slice operator
+ Loops - it's how stuff gets done
+ Conditionals - it's how decisions are made

------------------------------------------------------------------------------

## Tutorials ##

Each of the files in the `tutorials` directory is a Python program where most
of the code is contained in a giant triple-quoted string. To "play" the
tutorial, move the triple quotes farther down the file and run the program
again. Each time you move the quotes, you will see new output. You will learn
the most by experimenting as you go. Try changing the program before moving on
to the next section. People who just read the tutorial don't learn the material
very well, and will have a harder time completing the homework assignments.

You will be editing and saving files in the Tutorials directory as you proceed.
However, you will not be able to "git push" these to GitHub because I have not
invited you as a collaborator.

## Programs ##

The files in the `programs` directory are your homework problems. The comments
describe the goal of the program, and the triple quoted string at the end shows
you the the expected command line and output. Before you start working on a
homework problem, first copy it to your homework repo. For example, you might
do as follows for the first program.

```
cd ~/Code/homework
cp ~/Code/MCB185-2023/unit2_beginning_python/programs/20loop.py .
git add 20loop.py
git commit -m init
git push
```

You could even copy all of the programs in the unit in one `cp` command.

```
cp ~/Code/MCB185-2023/unit2_beginning_python/programs/* .
git add 2*
git commit -m init
git push
```

If you really want to save yourself future work, you could grab all of the
homework from every "Programs" directory!

```
cp ~/Code/MCB185-2023/*/programs/* .
git add *
git commit -m init
git push
```

## Optional ##

In addition to the required, numbered homework problems, there are a few
optional practice problems derived from Dungeons & Dragons 5e.
