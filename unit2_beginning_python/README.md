Unit 2: Beginning Python
========================

## Learning Objectives ##

+ Variables
+ Math
+ Strings
+ Loops
+ Conditionals

------------------------------------------------------------------------------

## Tutorials ##

Each of the files in the Tutorials directory is a Python program most of the
code contained in a giant triple-quoted string. To "play" the tutorial, move
the triple quotes farther down the file and run the program again. Each time
you move the quotes, you will see new output. People who just read the tutorial
don't learn the information very well. Experiment by changing some of the lines
and see what happens.

You will be editing and saving files in the Tutorials directory as you proceed.
However, you will not be able to "git push" these to GitHub because I have not
invited you as a collaborator.

## Programs ##

The files in the Programs directory are your homework problems. The comments
describe the goal of the program, and the triple quoted string at the end shows
the expected output. Before you start working on a homework problem, first copy
it to your homework repo. For example, you might do as follows for the first
program.

```
cd ~/Code/homework
cp ~/Code/MCB185-2023/Unit2/20loop.py .
git add 20loop.py
git commit -m init
git push
```

You could even copy all of the programs in the unit in one `cp` command.

```
cp ~/Code/MCB185-2023/Unit2/* .
git add 2*
git commit -m init
git push
```

If you really want to save yourself future work, you could grab all of the
homework from every "Programs" directory!

```
cp ~/Code/MCB185-2023/*/Programs/* .
git add *
git commit -m init
git push
```

## Homework ##

Your homework includes 10 programs plus a few optional practice problems
derived from Dungeons & Dragons 5e.
