Unit 1: Basic Unix
==================

## Learning Objectives ##

+ Environment variables
+ Viewing files
+ Absolute and relative paths
+ Injury prevention shortcuts
+ Standard input, output, and error
+ Creating and modifying files
+ Compression and archiving
+ Customize your shell

------------------------------------------------------------------------------

## Environment Variables ##

The shell defines various variables which are called _shell variables_ or
_environment variables_. For example, the `USER` variable contains your user
name, `HOME` contains the path to your home directory, `SHELL` contains the
path to your shell, and `PWD` contains the focus of your terminal. You can
examine the contents of a variable with the `printenv` command.

```
printenv USER
printenv HOME
```

The `echo` command writes stuff to your terminal, including the contents of
environment variables. Put a `$` on the front of the variable names to
dereference their contents.

```
echo Hello $USER, your home directory is: $HOME
```

If you want to see all your environment variables, you can use the `printenv` 
command without any arguments. We won't be using environment variables much in 
this course, but they are an important part of Unix.

```
printenv
```

------------------------------------------------------------------------------

## Viewing Files ##

The most common programs for viewing files are these:

+ `cat` - dump the contents of files
+ `head` - print the first 10 lines of a file
+ `tail` - print the last 10 lines of a file
+ `more` - page through a file
+ `less` - page through a file with more control
+ `zless` - like `less` but works with compressed files

Let's give them a test drive.

```
cd ~/Code/MCB1850-2023/Unit1
cat README.md
head README.md
tail README.md
head -5 README.md
tail -15 README.md
```

To read a file one page at a time, use `more` or `less`. Use the "f" and "b"
keys to move forward or backward one page. You can also use the spacebar to
move forward one page. To quit the program, use the "q" key.

```
more README.md
less REAMDE.md
zless ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz
```

<<<<<<< HEAD
Most Unix programs have descriptive names or initialisms. `cat` is short for 
catenate. `head` and `tail` are pretty self-explanatory. `more` shows you more 
of a file. `less` does more than `more` because sometimes less is more. If you 
have a choice between a pun and something actually useful, always choose the 
pun. Compressed files often have a "z" suffix so `zless` makes sense as a 
variant of `less`.

------------------------------------------------------------------------------

## Absolute, and Relative Paths ##

When you open a terminal application, the focus of your shell begins in  your
home directory. Let's verify this. Open a new terminal.

```
pwd
```

When you change directories, your focus will change.

```
cd Code/MCB185-2023/Unit1
pwd
```

<<<<<<< HEAD
Note that in both cases, the output of `pwd` was a directory path that started 
with the `/` character. Any path that begins with the `/` is an **absolute 
path**. An absolute path always begins at the filesystem root, which is `/`. An 
absolute path is like specifying your address and including your country, 
state, street, and house number. In contrast, a relative path assumes some 
prior knowledge. For example, within a city, you might want to get to 112 Main 
Street and it would be silly to specify what country you were in. Any path that 
does not begin with the `/` character is a **relative path**.
=======
Note that in both cases, the output of `pwd` was a directory path that started
with the `/` character. Any path that begins with the `/` is an **absolute
path**. An absolute path always begins at the filesystem root, which is `/`.
It's sort of like specifying your address and including your country, state,
street, and house number. In contrast, a relative path assumes some prior
knowledge. For example, within a city, you might want to get to 112 Main Street
and it would be silly to specify country, and state. Any path that does not
begin with the `/` character is a **relative path**.
>>>>>>> e1fd756ff8929ce000adecc36aee16e0dbdf9100

+ any path that begins with the filesystem root `/` is an absolute path
+ any other path is a relative path

In addition to the various named directories on your filesystem, you also have
`.` and `..`. The single dot `.` is a relative path to your current directory.
The double dot `..` is a relative path to the parent directory.

+ `/bin` absolute path
+ `$HOME/Code` absolute path (the `/` is in the variable)
<<<<<<< HEAD
+ `~/DATA` absolute path (`~` is an absolute path)
+ `REAMDE.md` relative path to a file in current directory
+ `./README.md` also relative path to the same file above
+ `../README.md` relative path to a different file in parent directory

Let's get some practice using absolute and relative paths. List your current
directory using absolute and relative paths.
=======
+ `~/DATA` absolute path (`~` is an absolute path to your home directory)
+ `REAMDE.md` relative path to file in current directory
+ `./README.md` also relative path to file in current directory
+ `../README.md` relative path to file in parent directory

Let's get some practice using absolute and relative paths. Inside the Unit1
directory you will see another directory called `project`. This is some
fictious project that involves some document, image, and source files. List
the contents of the directory using absolute and relative paths.
>>>>>>> e1fd756ff8929ce000adecc36aee16e0dbdf9100

```
ls $HOME/Code/MCB185-2023/Unit1
ls
```

In this case, it was a lot simpler to use the relative path than the absolute
path. That's not always the case. Try listing the filesystem root using both
absolute and relative paths.

```
ls /
ls ../../../../..
```

------------------------------------------------------------------------------

## Injury Prevention Shortcuts ##

Typing is bad for your health. Seriously, if you type all day, you will end up
with a repetitive stress injury. Don't type for hours at a time. Make sure you
schedule breaks. Unix has several ways to save your fingers.

### Tab Completion ###

Probably the most important finger saver in Unix is **tab completion**. When
you hit the tab key, the shell completes the rest of the word for you if it can
guess what you want next. Try typing `h` and then the tab (you may need to hit
it twice depeding on your flavor of shell). You should see all the commands
that begin with the letter h. Now type `i` and hit tab again. Those are all the
commands that begin with `hi`. Add an `s` and run the `history` command. This
shows you the last commands you typed.

### Up Arrow ###

Instead of re-typing long commands, you can go backwards through your command
history with the up-arrow. Trying hitting the up-arrow several times and you'll
see all the commands you've typed for some time. You can use the left and right
arrows to position the cursor if you want to edit parts of the line. To get out
of this, and many other situations, type Control-C. That is, hit the control
key and then the letter "c".

You should use tab completion constantly. Not only does it save you key
presses and time, it also ensures that your spelling is correct.

### Wildcards ###

One of the most useful time-saving tricks in the shell is the use of the `*`
character as a wildcard. The `*` character matches missing characters if it
can. Inside the Unit1 directory, there is only one thing that starts with the
letter "p". The `*` will fill in the rest. So here are three ways of doing the
same thing.

For the exercises that follow, we will be using the "project" subdirectory, 
which contains several subdirectories and files.

```
ls project
ls p*
ls p "hit the tab key"
```

The `*` isn't limited to filling in a single word. If you look inside the
`project/img` directory, you will see 3 files. Two of them have png extensions
while the other is jpg. We can list just the png files as follows:


```
ls project/img/*.png
```

To view multiple files in succession, send them all to `less`. Use Control-N to 
get to the next file and Control-P to go to the previous file. Use the "q" key 
to quit.

```
less project/src/*
```

To merge several files, use `cat` (now catenate makes sense).

```
cat project/doc/*
```

To see everything in the project directory:

```
ls project/*
```

### Symbolic Links ###

<<<<<<< HEAD
Long path names are sometimes laborious to type or even to look at. Let's make 
a shortcut to the E.coli genome in DATA using a symbolic link, which is also 
called a soft-link.
=======
Long path names are sometimes laborious to look at. Let's make a shortcut to
the E.coli genome in DATA using a symbolic link, which is also called a
soft-link.
>>>>>>> e1fd756ff8929ce000adecc36aee16e0dbdf9100

```
ln -s ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz ./ecoli.fa.gz
```

Please tell me you used tab-completion for that and didn't actually type it
out! Now, we have a file called `ecoli.fa.gz` that appears exactly like the
original file except that it's just a shortcut.

```
zless ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz
zless ecoli.fa.gz
```

How can you tell the difference between a normal file and a symbolic link? The
`-F` option gives `ls` some extra formatting. Symbolic links are shown with an
`@` symbol. Also, if you're using a color terminal, it will have a different
color.

```
ls -F
```

------------------------------------------------------------------------------

## Standard Input, Output, and Error ##

When you issue commands like `ls`, the output that is sent to your terminal is
called Standard Output (stdout). Output doesn't have to go to your terminal.
You can choose to send it to a file or to another program.

The `>` operator re-directs stdout to a file. Let's try that with the `ls`
command.

```
ls > foo
```

Notice that `ls` didn't print anything to the terminal? That's because the
contents are in the file "foo". You can dump those out to the terminal with
`cat`.

```
cat foo
```

Instead of sending stdout to a file, you can pipe it to another command. Here,
the stdout of `ls` will be sent to the Standard Input (stdin) of the word
counting program `wc` via the pipe `|` operator.

```
ls | wc
```

Some programs, like `wc` can read from both files and stdin.

```
wc foo
```

So `ls > foo` followed by `wc foo` does the same thing as `ls | wc` without
having any intermediate file. Unix pipes are a very powerful way to chain
programs to each other.

There is also the `<` operator. This sends stdin from a file to a program.

```
wc < foo
```

What do you think this does?

```
wc < foo > bar
```

Here, the contents of the file "foo" are sent to `wc` as stdin, and then `wc`
sends its output to the file "bar".

+ `>` sends the stdout of a program to a file
+ `<` sends the contents of a file to the stdin of a program
+ `|` connects the stdout of one program to the stdin in of another

In addition to stdin and stdout, there is another stream of data called
Standard Error (stderr). This is meant to be used for error messages or logging
messages rather than data.

------------------------------------------------------------------------------

## Creating and Modifying Files ##

For the exercises in this section, it may be useful to have your graphical 
desktop displaying the contents of your Unit1 directory. That way you can see 
that the CLI does the same things as pointing and clicking.

There are a number of ways to create a file. The `touch` command, which we saw
last unit, will create a file or change its modification time (Unix records
when the last time a file was edited) if it already exists. Let's first make
sure we are in the Unit1 directory.

```
cd ~/Code/MCB185-2023/Unit1
touch empty
```

If your graphical file browser was open to your Unit1 directory, when you hit 
the return key, you would have seen the file magically appear in the file 
browser. The file "empty" doesn't contain anything at all. To verify this, try 
`ls -l`, which creates a listing with a long format. You'll see a zero in one 
of the columns. That's the file size in bytes.

Lets add some content to the empty file. Most of the time when you create,
edit, and save files, you'll be using your favorite text editor. But there are
also terminal-based editors that you may find useful for remote logins. Let's
use `nano` to change the contents.

```
nano emtpy
```

Your terminal is now a text editor with some menus at the bottom. Type some 
stuff. Try navigating around the document with arrow keys. Write some poetry. 
When you're done, hit ^O to write the changes and then ^X to exit. What the 
heck are those keys? ^O is shorthand for Control-O. Just like when we hit 
Control-C before, hold the control key and then hit the "o" key.

Now that "empty" is no longer empty, let's rename it. Weirdly the command used
to rename files is also the command to move them.

```
mv empty full
```

If you had your graphical file browser open, you would see that the name
changed. Try a long listing of the file now: `ls -l full`. 

To copy a file, use the `cp` command.

```
cp full f2
```

If you do a long listing, you will see that the two files have the same size. 
To check if they have the same contents, you can do a `sum`. This will do a 
checksum on each file, and if they have the same value, they are very likely to 
have the exact same contents.

```
ls -l full f2
sum full f2
```

Now open up an editor (your graphical editor or `nano`) and modify one of the
characters in f2. The file size will remain the same, but the checksum will be
totally different. If you have two related files and want to see where they are
different, use the `diff` command.

```
ls -l full f2
sum full f2
diff full f2
```

Let's tidy up a bit by making a directory with `mkdir` and then moving the two 
files into that directory. Notice that the `mv` command can take multiple 
arguments. The last argument is the directory and the previous ones are files. 
This works for moving files but not renaming them (recall that `mv` does both).

```
mkdir Stuff
mv full f2 Stuff
```

To remove a directory, you use the `rmdir` command. However, `rmdir` will not
remove a directory if it has any files in it. So this command will fail. Do it
anyway.

```
rmdir Stuff
```

Let's empty the directory using a wildcard. Note the use of `.` to mean "this 
directory".

```
mv Stuff/* .
ls
```

Now the `rmdir` will work.

```
rmdir Stuff
```

To delete files, use the `rm` command. Using wildcards with `rm` is potentially 
dangerous. While the intent of `rm * .txt` looks like you want to remove all 
text files in the current directory, there is a space between the `*` and the 
`.txt`. What this literally means is to delete all files (the wildcard) and 
then the file called `.txt`, which probably doesn't even exist.

------------------------------------------------------------------------------

## Compression and Archiving ##

Text files tend to be very wasteful of disk space. For starters, they only use 
7 of the 8 possible bits of every byte. This means they are about 2 times 
larger than they need to be. In addition, they tend to be highly repetitive, 
often using the same patterns of characters several times. Taken together, text 
files of genome data can typically be compressed 3-fold or more. The most 
common compression program in Linux is `gzip`. Let's try it.

```
ls
gzip README.md
ls
```

Notice that when you run `gzip`, it creates a new file with a `.gz` extension.
It also removes the old file. To return the file, `gunzip` it.

```
gunzip README.md.gz
```

If you want to compress a file and also keep the original, use the `-k` flag.

```
gzip -k README.md
ls
```

If you want to compress an entire directory, you have to first make an archive 
out of it with the `tar` command (short for "tape archive"). We often call tar 
files tarballs. So let's make a tarball out of the project directory. You must 
pass the `-c` option to "create" and the `-f` option to name the "file". Like 
other Unix options, you can put the two letters together.

```
tar -cf project.tar project
```

It is common to compress tarballs with gzip. Compressed archives are so common 
that the `tar` command allows you to do both steps at once if you add the `-z` 
option.

```
tar -zcf p.tar.gz project
```

To extract from a tarball, you use `-x` instead of `-c`. The project directory 
already exists, so let's delete it and then recreate it. The first command here 
is really dangerous because it deletes the directory and everything beneath it.

```
rm -rf project
ls
tar -xf project.tar
ls project/*
```

Earlier we used `zless` to examine the contents of a compressed file (or a 
symbolic link to the actual file).

```
zless ecoli.fa.gz
```

What if we want to do `wc` the file? Do we have to decompress it? No, and we 
shouldn't because then it will take up a lot more space. You can often leave 
compressed files as is, and uncompress their contents on the fly. These two
commands are the same:

```
gunzip -c ecoli.fa.gz | wc
zcat ecoli.fa.gz | wc
```

------------------------------------------------------------------------------

## Customize Your Shell ##

In order to simplify a few things, you should customize your login script. 
First, we have to figure out which shell you're running. Your shell is in your 
SHELL environment variable. Here are two ways of seeing that.

```
printenv SHELL
echo $SHELL
```

If your shell is `/bin/bash` then check if you have a file called `.profile` or 
`.bash_profile` or `.bashrc` in your home directory. If not, create a 
`.profile` with `touch`.

If your shell is `/bin/zsh` then check if you have a file called `.zshrc`. If 
not, create it with `touch`.

Whichever file you have from above is your login script. Open the file in your 
favorite editor, add these lines at the end, and save.

```
alias ls="ls -F"
alias ll="ls -l"
alias ..="cd .."
alias rm="rm -f"
```

Now `ls` always does `ls -F`. Meaning, you will always be able to tell a 
directory or symbolic link from the character at the end of the name. You will 
be changing to parent directories a lot so `..` is a nice convenience. Since 
`rm` is a dangerous command, the `-i` option is always added to enter 
interactive mode (you always have to confirm your decisions). We will add more 
customizations later.
