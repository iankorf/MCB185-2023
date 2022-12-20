Unit 1: Basic Unix, Basic Python
================================

## Learning Objectives ##

+ Environment variables
+ Viewing files
+ Absolute and relative paths
+ Injury prevention shortcuts
+ Standard input, output, and error
+ Creating and modifying files

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
this course.

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

Most Unix programs have descriptive names or initialisms. `cat` is short for 
catenate. `head` and `tail` are self-explanatory. `more` shows you more of a 
file. `less` does more than `more` because sometimes less is more. If you have 
a choice between a pun and something actually useful, always choose the pun.

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

Note that in both cases, the output of `pwd` was a directory path that started 
with the `/` character. Any path that begins with the `/` is an **absolute 
path**. An absolute path always begins at the filesystem root, which is `/`. 
It's sort of like specifying your address and including your country, state, 
street, and house number. In contrast, a relative path assumes some prior 
knowledge. For example, within a city, you might want to get to 112 Main Street 
and it would be silly to specify country, and state. Any path that does not 
begin with the `/` character is a **relative path**.

+ any path that begins with the filesystem root `/` is an absolute path
+ any other path is a relative path

In addition to the various named directories on your filesystem, you also have 
`.` and `..`. The single dot `.` is a relative path to your current directory. 
The double dot `..` is a relative path to the parent directory.

+ `/bin` absolute path
+ `$HOME/Code` absolute path (the `/` is in the variable)
+ `~/DATA` absolute path (`~` is an absolute path)
+ `REAMDE.md` relative path to file in current directory
+ `./README.md` also relative path to file in current directory
+ `../README.md` relative path to file in parent directory

Let's get some practice using absolute and relative paths. Inside the Unit1 
directory you will see another directory called `project`. This is some 
fictious project that involves some document, image, and source files. List
the contents of the directory using absolute and relative paths.

```
ls $HOME/Code/MCB185-2023/Unit1/project
ls project
```

In this case, it was a lot simpler to use the relative path than the absolute 
path. That's not always the case. Try listing the filesystem root using both
absolute and relative paths

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
key and then the letter c. This sends an "interrupt" signal to the shell.

You should use tab completion constantly. Not only does it save you key
presses and time, it also ensures that your spelling is correct.

### Wildcards ###

One of the most useful time-saving tricks in the shell is the use of the `*` 
character as a wildcard. The `*` character matches missing characters if it 
can. Inside the Unit1 directory, there is only one thing that starts with the 
letter "p". The `*` will fill in the rest. So here are three ways of doing the 
same thing.

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

Here are some more examples:

```
ls project/*
cat project/doc/*
```

### Symbolic Links ###

Long path names are sometimes laborious to look at. Let's make a shortcut to 
the E.coli genome in DATA using a symbolic link, which is also called a 
soft-link.

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

------------------------------------------------------------------------------

## Standard Input, Output, and Error ##

When you issue commands like `ls`, the output that is sent to your terminal is
called Standard Output (stdout). Output doesn't have to go to your terminal.
You can choose to send it to a file or to another program.

The `>` operator re-directs stdout to a file. Let's try that with the `ls`
command from your home directory.

```
cd
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

Let's be tidy and remove the "foo" and "bar" files with the `rm` command.

```
rm foo bar
```

------------------------------------------------------------------------------



------------------------------------------------------------------------------

## Creating and Modifying Files ##

For the exercises in this section, it may be useful to have your graphical
desktop displaying the contents of your home directory. That way you can see
that the CLI does the same things as pointing and clicking.

There are a number of ways to create a file. The `touch` command, which we saw
last unit, will create a file or change its modification time (Unix records
when the last time a file was edited) if it already exists. Let's first make
sure we are in our home directory.

```
cd
touch empty
```

If your graphical file browser was open to your home directory, when you hit
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
Control-C before, hold the control key and then hit the o key. Despite the
capital letters, we don't use the shift key.

Now that "empty" is no longer empty, let's rename it. Weirdly the command used
to rename files is also the command to move them.

```
mv empty full
```

If you had your graphical file browser open, you would see that the name
changed. Try a long listing of the file now: `ls -l full`. Now let's make a
directory.

```
mkdir Stuff
```

Again, if you were watching your file browser, you now have a new directory
called "Stuff" in your home directory. Let's move the "full" file to the Stuff
directory.

```
mv full Stuff
```

To remove a directory, you use the `rmdir` command. However, `rmdir` will not
remove a directory if it has any files in it. Therefore, the first command
below produces an error.

```
rmdir Stuff
rm Stuff/full
rmdir Stuff
```



STOPPED HERE


### Copying and Aliasing ###

The `cp` command copies files. Let's say you wanted to make a copy of `bar`
which is currently in your Work directory. You have to tell `cp` where you want
that copy to exist. It can't exist in the exact same location. You'll either
have to give it a different location or change its name. Let's first try giving
it a new location.

	cp stuff/bar .

The previous command reads as "copy the bar file from the stuff directory to my
current location". We could also copy the file without changing its location,
but we have to give it a new name.

	cp stuff/bar stuff/bark
	ls stuff

### Deleting Files ###

You delete files with the `rm` command. Be careful, because once gone, files
are gone forever. If you want a safer, interactive version of `rm` use it with
the `-i` flag (we saw this earlier with `mv`).

	ls stuff
	rm stuff/file1
	ls stuff
	rm -i bar

As a reminder, you didn't type those file names completely, right? You used tab
completion, right?

You can delete multiple files at once too and even whole directories. Watch out
though, that can get dangerous. If you want to completely remove everything in
the `stuff` directory, you _could_ do the following (but please don't):

	rm stuff/*

That will still leave the `stuff` directory intact, but without any files. If
you want to remove the directory, you use the `rmdir` command. You can try
this, but it won't work because the directory isn't empty. `rmdir` only removes
empty directories.

	rmdir stuff

If you want to remove a directory and everything it contains, you can use the
`-r` flag to recursively delete everything inside and the `-f` flag to force
delete of protected files. This is highly, highly destructive, so maybe don't
do it.

	rm -rf stuff

The worst possible thing you could do is unintentionally use the wildcard `*`
with the `rm` command with slightly incorrect syntax. Here, let me show you how
to destroy everything. Maybe don't type this...

	rm -rf stuff *

You may have wanted to do `rm -rf stuff/*` but the space between `stuff` and
`*` means that `*` matches **EVERYTHING**. So that's how you delete everything
in your current directory. If you happen to be in your home directory, you just
deleted everything you own. Ask me how I know.

Since `mv`, `cp`, and `rm` can be so dangerous, many people create aliases that
force each command to be interactive. We'll see how to do this a little farther
below when we get to the more advanced Unix section.


## Wildcards ##

## Compression and Archiving ##

## Customizing your login script ... ##





## Unix Permissions ##


### Files on Flash Drives ###

Most flash drives are formatted to be compatible with Windows machines. Each
operating system has a different idea about how to store filesystem metadata
such as permissions. Because of this, most files on flash drives end up with
all permission set. In octal, that would be 777 (read, write, execute) for
owner, group, and public. This is the most permissive setting and can be a
little dangerous. After copying files from a flash drive to your Unix machine,
it's probably a good idea to change the permissions to something more sensible.




### Customizing Your Shell ###

In order to simplify a few things, we need to customize your shell. First, we
have to figure out which shell you're running. Your shell is in your SHELL
environment variable. Here are two ways of seeing that.

	printenv SHELL
	echo $SHELL

If your shell is `/bin/bash` then check if you have a file called `.profile` or
`.bash_profile` or `.bashrc` in your home directory. If you already have one of
those files, edit it with nano. If not, create a `.profile` with nano.

If your shell is `/bin/zsh` then check if you have a file called `.zshrc`. If
it exists, edit it with nano. If not, create it with nano.

Now enter the following 2 lines into the file you're editing.

	alias ls="ls -F"
	export PATH=$PATH:$HOME/Work/bin

The first line makes it so that whenever you use the `ls` command, you're
actually invoking `ls -F` which displays the file type by appending a `*` to
executable files and a `/` to directories.

The second line adds your `Work/bin` directory to the executable path. Now, any
script you put into `Work/bin` can be run like any other program.

To protect yourself from accidentally overwriting or removing files, you might
want to add interactive mode for a few commands.

	alias rm="rm -i"
	alias mv="mv -i"
	alias cp="cp -i"



## Unix Permissions and Paths ##

Unix file permissions are critical to understand, but a little obscure. To
understand how they work, we're going to turn our `00helloworld.py` program
into a proper executable. Be patient in this section, it's complex.

Previously, when we wanted to run the program `00helloworld.py` we had to
proceed that with the command `python3`. Most of the programs you've seen so
far, like `date` or `ls` did not require anything other than the name of the
program. We can change `00helloworld.py` to work in the same manner. While this
isn't really necessary, it's very important to understand how permissions work,
so we're going to modify `00helloworld.py` to be just like `ls`.

Go to your homework repot and use nano to edit the file.

	nano 00helloworld.py

Now modify it so that it looks like the following:

	#!/usr/bin/env python3
	print('hello world')

Line 1 has the "hash bang" _interpreter directive_. The first line of a text
file tells Unix which language to use. Make sure the first character of the
file is `#` and that there are no additional leading spaces. Line 2 is what you
had before. Save this file and then push the changes back to your repo. We're
not done yet. This is just the first step.


### Files on Flash Drives ###

Most flash drives are formatted to be compatible with Windows machines. Each
operating system has a different idea about how to store filesystem metadata
such as permissions. Because of this, most files on flash drives end up with
all permission set. In octal, that would be 777 (read, write, execute) for
owner, group, and public. This is the most permissive setting and can be a
little dangerous. After copying files from a flash drive to your Unix machine,
it's probably a good idea to change the permissions to something more sensible.

### Customizing Your Shell ###

In order to simplify a few things, we need to customize your shell. First, we
have to figure out which shell you're running. Your shell is in your SHELL
environment variable. Here are two ways of seeing that.

	printenv SHELL
	echo $SHELL

If your shell is `/bin/bash` then check if you have a file called `.profile` or
`.bash_profile` or `.bashrc` in your home directory. If you already have one of
those files, edit it with nano. If not, create a `.profile` with nano.

If your shell is `/bin/zsh` then check if you have a file called `.zshrc`. If
it exists, edit it with nano. If not, create it with nano.

Now enter the following 2 lines into the file you're editing.

	alias ls="ls -F"
	export PATH=$PATH:$HOME/Work/bin

The first line makes it so that whenever you use the `ls` command, you're
actually invoking `ls -F` which displays the file type by appending a `*` to
executable files and a `/` to directories.

The second line adds your `Work/bin` directory to the executable path. Now, any
script you put into `Work/bin` can be run like any other program.

To protect yourself from accidentally overwriting or removing files, you might
want to add interactive mode for a few commands.

	alias rm="rm -i"
	alias mv="mv -i"
	alias cp="cp -i"


## Useful Unix Commands ##

The `wc` program counts the characters, words, and lines in text files. You
could counts the words in this document, for example.

	wc GUMPY.md

One of the most useful programs is `grep`. This prints out lines that match
specific strings or patterns. For example, if you wanted to print out all the
lines with the word Unix you would do the following:

	grep Unix GUMPY.md

To count how many lines that was, you could either use the `-c` flag to `grep`
or **pipe** the output to `wc`.

	grep -c Unix GUMPY.md
	grep Unix GUMPY.md | wc

When working with tabular data, you will find that `sort` is very useful, as it
let's you sort the lines on different columns.

When monitoring the progress of programs that take a long time to run, you will
find `time` useful for timing how long a program runs and `top` or `htop` for
monitoring how much RAM or other resources a program is taking.

To see how much free space you have on your file system, use the `df` (disk
free) command with the `-h` option to make it more human-readable (try it both
ways).

	df
	df -h

Another useful command is `du` (disk usage) which shows how much space each of
your files and directories uses.

	du
	du -h

## Unix Quick Reference ##

| Token | Meaning
|:------|:-------------------------------------|
| `.`   | your current directory (see pwd)
| `..`  | your parent directory
| `~`   | your home directory (also $HOME)
| ^C    | send interrupt signal
| ^D    | send end-of-file character
| tab   | tab-complete names
| `*`   | wildcard - matches everything
| `|`   | pipe output from one command to another
| `>`   | redirect stdout to file
| `<`   | send a file as stdin


| Command   | Example       | Intent                        |
|:----------|:--------------|:------------------------------|
| `cat`     | `cat > f`     | create file f and wait for keyboard (see ^D)
|           | `cat f`       | stream contents of file f to STDOUT
|           | `cat a b > c` | concatenate files a and b into c
| `cd`      | `cd d`        | change to relative directory d
|           | `cd ..`       | go up one directory
|           | `cd /d`       | change to absolute directory d
| `chmod`   | `chmod 644 f` | change permissions for file f in octal format
|           | `chmod u+x f` | change permissions for f the hard way
| `cp`      | `cp f1 f2`    | make a copy of file f1 called f2
| `df`      | `df -h .`     | display free space on file system
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
| `tail`    | `tail f`      | display the last 10 lines of file f
|           | `tail -f f`   | as above and keep displaying if file is open
| `tar`     | `tar -cf ...` | create a compressed tar-ball (-z to compress)
|           | `tar -xf ...` | decompress a tar-ball (-z if compressed)
| `time`    | `time ...`    | determine how much time a process takes
| `top`     | `top`         | display processes running on your system
| `touch`   | `touch f`     | update file f modification time (create if needed)
| `wc`      | `wc f`        | count the lines, words, and characters in file f
| `zcat`    | `zcat f.gz`   | stream compressed file f.gz to stdout


