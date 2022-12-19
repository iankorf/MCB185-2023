Unit 1: Basic Unix, Basic Python
================================

## Learning Objectives ##

+ Environment variables
+ Absolute and relative paths
+ Injury prevention with tab-completion and up-arrow
+ Standard input, output, and error
+ Creating and modifying files

------------------------------------------------------------------------------

## Environment Variables ##

The shell defines various variables which are called _shell variables_ or
_environment variables_. For example, the `USER` variable contains your user
name and the `HOME` variable contains the path to your home directory. You can
examine the contents of a variable with the `printenv` command.

```
printenv USER
printenv HOME
```

The `echo` command writes stuff to your terminal, including the contents of
environment variables.

```
echo Hello $USER, your home directory is: $HOME
```

If you want to see all your environment variables, you can use the `printenv`
command without any arguments.

```
printenv
```

------------------------------------------------------------------------------

## Focus, Absolute, and Relative Paths ##

When you open your terminal application, the focus of your shell is your home
directory. You can verify this with the `pwd` command. Open a new terminal and
run the command.

```
pwd
```

This command shows you the **absoute path** of your home directory. This might
be `/home/$USER` or `/Users/$USER` or possibly something else. What makes this
an absolute path is that it starts with a `/`. If the directory path doesn't
start with a `/`, it's not an absolute path.

You can access directories and files with absolute or relative paths. Let's try
listing your home directory using the absolute path. Substitute
"your_home_directory" for whatever the contens of `pwd` was. Don't forget the
leading `/`.

```
ls /your_home_directory
```

Of course, we could also have used the `$HOME` variable here.

```
ls $HOME
```

One more option is to use the `~` key for a shortcut to your home directory.

```
ls ~
```

Whether we type out the full name, use the `$HOME` environment variable or the
`~` shortcut, all of these methods use the absolute path. Let's list the
contents of your homework directory using absolute paths.

```
ls /your_home_directory/Code/homework
ls $HOME/Code/homework
ls ~/Code/homework
```

A **relative path** does not begin with the `/` symbol. Instead, the path is
relative to your current focus. Let's change focus to the homework repo and
then list it.

```
cd ~/Code/homework
ls
```

Here, the `ls` command uses the current focus. From your homework directory,
all of these commands do the same thing.

```
ls /your_home_directory/Code/homework
ls $HOME/Code/homework
ls ~/Code/homework
ls
```

When using relative paths, there are two important modifiers:

+ `.` means your current directory
+ `..` means your parent directory

Both of these commands do exactly the same thing:

```
cat 00helloworld.py
cat ./00helloworld.py
```

It may seem like `.` is useless, but there are times when you want to use your
current directory as an argument to a command. For example, if you want to copy
a file from some other location to your current focus, you would do something
like `cp some_path .`, where the `.` is your current focus.

You will find a lot more use for the `..` parent directory token. Let's say we
want to list the contents of the Code directory when the focus is homework. All
of these methods do the same thing.

```
ls /your_home_directory/Code
ls $HOME/Code
ls ~/Code
ls ..
```

The last command used the `..` for parent directory. The Code directory is "one
up" from the homework directory. Similalry, you could list the contents of your
home directory from within your homework directory. Both of these commands do
the same thing, but one uses absolute path and the other relative.

```
ls ~
ls ../..
```

------------------------------------------------------------------------------

## Injury Prevention ##

Typing is bad for your health. Seriously, if you type all day, you will end up
with a repetitive stress injury. Don't type for hours at a time. Make sure you
schedule breaks. Unix has several ways to save your fingers.

Probably the most important finger saver in Unix is **tab completion**. When
you hit the tab key, the shell completes the rest of the word for you if it can
guess what you want next. Try typing `h` and then the tab (you may need to hit
it twice depeding on your flavor of shell). Those are all the commands that
begin with the letter h. Now type `i` and hit tab again. Those are all the
commands that begin with `hi`. Add an `s` and run the `history` command. This
shows you the last commands you typed.

Isntead of re-typing long commands, you can go backwards through your command
history with the up-arrow. Trying hitting the up-arrow several times and you'll
see all the commands you've typed for some time. You can use the left and right
arrows to position the cursor if you want to edit parts of the line. To get out
of this, and many other situations, type Control-C. That is, hit the control
key and then the letter c. This sends an "interrupt" signal to the shell.

You should use tab completion constantly. Not only does it save you key
presses and time, it also ensures that your spelling is correct.

------------------------------------------------------------------------------

## Standard Input, Output, and Error ##

When you issue commands like `cat`, the output that is sent to your terminal is
called Standard Output (stdout). Sometimes that output is really long and hard
to read quickly. 

```
cat ~/Code/MCB185-2023/README.md
```

In these cases, we often use a pager program like `less` to capture the stdout
and let us read it page-by-page. Let's try that. In order for `less` to get the output from `cat` we connect them with a pipe `|`.

```
cat ~/Code/MCB185-2023/README.md | less
```

It happens that `less`, and many other Linux programs, can read Standard Input
(stdin) from pipes as well as files. So you could have had a very similar
experience doing the following:

```
less ~/Code/MCB185-2023/README.md
```

So what's the difference? In one case, `less` reads the file off the
filesystem. In the other case, it reads a stream of stdout from `cat` into its
own stdin. Despite seeming similar, they are very different things. To make
this more clear, let's put in another pipe.

```
cat ~/Code/MCB185-2023/README.md | grep the | less
```

Here, the `cat` program streams stdout to the stdin of `grep`. This keeps every
line with the word "the" and streams that out to stdout. `less` captures that
as stdin and lets us page through it. However, maybe we want to send that on to
another program like `wc` to count the number of lines. That's simple:

```
cat ~/Code/MCB185-2023/README.md | grep the | wc
```

This is the simple power of Unix CLI tools. It's easy to chain them together
via stdin and stdout. In addition to the pipe `|` symbol, you can also
re-direct stdout to a file using the greater than sign `>`.

```
cat ~/Code/MCB185-2023/README.md | grep the | wc > foo
```

Now the file "foo" contains the output of that chain of commands. You can also
redirect stdin using the `<` sign, but that is not as common.

In addition to stdin and stdout, there is





Whenever you type at the keyboard, you are creating something called Standard
Input (stdin). Anything reported to your terminal is Standard Output (stdout).
Well, there is also Standard Error, but that's a topic for another day. Many
Unix programs can input stdin and output stdout. For example, the word count
program `wc` reads from stdin and writes to stdout.




------------------------------------------------------------------------------

## Creating, Modifying, and Viewing Files ##

For the this exercise in this section, it may be useful to have your graphical
desktop displaying the contents of your home directory. That way you can see
that the CLI does the same things as pointing and clicking.


### touch ###

There are a number of ways to create a file. The `touch` command, which we saw
last unit, will create a file or change its modification time (Unix records
when the last time a file was edited) if it already exists. Let's first make
sure we are in our home directory.

```
cd
touch emtpy
```

If your graphical file browser was open to your home directory, when you hit
the return key, you would have seen the file magically appear in the file
browser. The file "empty" doesn't contain anything at all. To verify this, try
`ls -l`, which creates a listing with a long format. You'll see a zero in one
of the columns. That's the file size in bytes. 

### nano ###


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

### mv ###

Now that "empty" is no longer empty, let's rename it. Weirdly the command used
to rename files is also the command to move them.

```
mv empty full
```

If you had your graphical file browser open, you would see that the name
changed. Try a long listing of the file now: `ls -l full`. We're going to make
a bunch of files, so let's create a directory to keep everything tidy.

```
mkdir Stuff
```

Again, if you were watching your file browser, you now have a new directory
called "Stuff" in your home directory. Let's move the "full" file to the Stuff
directory.

```
mv full Stuff
```







### Standard Input, Standard Output, and Redirection ###

Whenever you type at the keyboard, you are creating something called Standard
Input (stdin). Anything reported to your terminal is Standard Output (stdout).
Well, there is also Standard Error, but that's a topic for another day. Many
Unix programs can input stdin and output stdout. For example, the word count
program `wc` reads from stdin and writes to stdout.


The `>` symbol is used to redirect output from standard output to a file. 



```
ls /bin > bar
```

This command listed the `/bin` directory and **redirected** the output to a
file named `bar`. The greater-than sign allows you to send a stream of
characters to a file. Those characters can be streamed from the `ls` command as
was done here, or you could type them at the keyboard. Let's try putting some
content into `foo` with the keyboard.

```
cat > foo
```

After you type the line above, the shell appears to hang. It's waiting for you
to start typing. Go ahead and write a few lines of poetry. To close the stream
of data and save the file, type ^D. What the heck is ^D? In Unix parlance, that
means hit the _control_ key followed by the _d_ key. This is sometimes written
as control-D. Note that even though ^D and control-D have a capital D in them,
you don't actually use the shift key. So go ahead and type ^D.

The most useful ways to view a file are with `head`, `tail`, `more`, and
`less`. `head` shows you the first 10 lines of a file, while `tail` shows you
the last 10. Of course there are command line options to change the number of
lines. Let's try them out.

```
head foo
tail foo
head -5 bar
tail -5 bar
```

If you want to view a whole file you can do that with `cat` or `less`. We just
saw how `cat` could be used to create a file, but it can also be used to view
them.

```
cat bar
```

This isn't very useful for viewing large files unless you're a speed reader. A
more useful way to look at files is with a _pager_. The `more` and `less`
commands let you see a file one terminal page at a time. This is what you used
before when viewing the manual page for the `date` command. Use the spacebar to
advance by one page, the _b_ key to go backwards by one page, and when you're
done, hit _q_ to quit. `more` and `less` do more or less the same thing, but
oddly enough `less` does more than `more`. There are a lot of silly jokes in
Unix culture.

```
less bar
```

## Editing Files ##

Most of the time, you will be using your programming editor to create, modify,
and save files. But there are terminal-based editors too. Let's try editing a
file with `nano`.

```
nano foo
```

This changes the entire look of your terminal. No longer are you typing
commands at a prompt. Now you're editing a file and can change the random text
you just wrote. Use the arrow keys to move the cursor around. Add some text by
typing. Remove some text with the delete key. At the bottom, you can see a menu
that uses control keys. To save the file you hit the ^O key (control and then
the letter o). You will then be prompted for the file name, at which point you
can overwrite the current file (bar) or make a new file with a different name.
To exit nano, hit ^X.

Unix file names often have the following properties:

* all lowercase letters
* no spaces in the name (use underscores or dashes instead)
* an extension such as .txt

## Navigating the Filesystem ##

In the Unix filesystem, all paths are either _absolute_ or _relative_. An
absolute path begins with a `/` while a relative path does not. While this may
seem like a small difference, it is actually very important.

The path `/bin`, which we used before with the `cat` command, is an absolute
path. The command `ls /bin` literally means "go to the root of the entire
filesystem and list the contents of the `bin` directory. Let's try that again
now, but first we will make sure the focus of the terminal is your home
directory.

```
cd
ls /bin
```

If we remove the `/` from the start, the command has a **very** different
meaning. It now says "in the current directory, list the contents of the `bin`
directory". We might not even have a `bin` directory in our home directory. And
if we did, surely the contents would be different from the root of the
filesystem, which contains programs critical to the operating system.

Let's make sure this is absolutely clear. Change focus to your `Code` directory
and list its contents.

```
cd ~/Code
ls
```

That should show you your homework and MCB185-2023 repos. Now that our focus is
the `Code` directory, let's list the contenst of our home directory using both
absolute and relative paths.





A path that begins with a `/` is called an _absolute path_ (we saw this before
when we did `ls /bin`). Your location also has a _relative path_, which is
simply the dot `.` character. Your full name is like an absolute path while
pronouns are like a relative path. So "Ian Frederick Korf" describes the author
absolutely, while "me" describes me more relatively. If I want to reference
other people, I can use an absolute or relative path. "Mario Takechi Korf"
describes my brother in absolute terms while "twin brother" describes him in
relative terms.




If you want to know what files are in your home directory, you can do that with
an absolute path regardless of where your shell is currently focused.



 You can
type out the path you found above, or you can dereference the `HOME`
environment variable.

	echo $HOME
	ls $HOME

You can also list your home directory using a relative path. Read the dot as
"here" so the following command is "list here".

	ls .

`ls` will list your current directory if you don't give it an argument, so an
equivalent statement is simply:

	ls

Notice that `ls` reports both the files and directories in your current
directory. Without icons it's a little difficult to figure out which names
correspond to file and which to directories. So let's add a command line option
to the `ls` command that will decorate directories with a special character.

	ls -F

This command adds a character to the end of the file names to indicate what
kind of files they are. A forward slash character indicates that the file is a
directory. These directories inside your working directory are called
_sub-directories_. They are **below** your current location. There are also
directories **above** your current focus. There is at most one directory
immediately above you. We call this the **parent** directory, which in Unix is
called `..` (that wasn't a typo, it's two dots). You can list your parent
directory as follows:

	ls ..

The `ls` command has a lot of options. Try reading the `man` pages and trying
some of them out. Now is a good time to experiment with a few command line
options. Note that you can specify them in any order and collapse them if they
don't take arguments (some options have arguments).

	man ls
	ls -a
	ls -l
	ls -l -a
	ls -a -l
	ls -la
	ls -al

There are two ways to specify a directory: _relative_ path and _absolute_ path.
The command `ls ..` listed the directory above the current directory. The
command `nano bar` edited the file `bar` in the current directory. You could
also have written `nano ./bar`. What if you want to list some directory
somewhere else or edit a file somewhere else? We actually did that before with
`ls /bin > foo`. To specify the absolute path, you precede the path with a
forward slash. For example, to list the absolute root of the Unix file system,
you would type the following:

	ls /

To list the contents of /usr/bin you would do the following:

	ls /usr/bin

This works exactly the same from whatever your current working directory is
because `/usr/bin` is an absolute path. However, if you do `ls bin` it only
works if you happen to have a directory or file called `bin` in your current
focus.

To change your working directory, use the `cd` command. Try changing to the root
directory

	cd /
	pwd
	ls

Now return to your home directory by executing `cd` without any arguments.

	cd
	pwd
	ls

Now go back to the root directory and create a file in your Work directory.
That is, your shell will have its focus on the root directory, but the files
you create will be in your Work directory. Open your GUI file browser to your
Work directory before you begin these commands.

	cd /
	touch $HOME/Work/file1
	touch ~/Work/file2
	ls ~/Work

### Moving and Renaming Files ###

Your home directory is starting to fill up with a bunch of crap. Let's organize
that stuff. First off, let's create a new directory for `stuff` using the
`mkdir` command.

	cd ~/Work
	mkdir stuff

Let's move some files into that new directory with the `mv` (move) command.

	mv foo stuff

The file `foo` is now inside the directory `stuff`. You can observe this by
listing the current directory, which no longer contains `foo`, and `stuff`,
where it now resides.

	ls .
	ls stuff

The weird thing about the `mv` command is that it not only moves files into
directories, it can also rename them. Let's try renaming `bar` to `bark`.

	mv bar bark

The difference between `mv foo stuff` and `mv bar bark` is that in the former
case there was a directory called `stuff` and in the latter there wasn't. This
is the key to `mv` command. If the last argument exists, it tries moving the
first argument (the file) into the last argument (the directory). What if you
try moving a file onto an already existing file? Let's do that with the
previously created `file` and `file2`.

	mv file1 file2
	ls .

Whoops. `file1` just got renamed to `file2`. In other words, the contents of
`file2` just got permanently deleted. For this reason, sometimes people use the
`-i` flag to turn on interactive mode. Let's recreate the previous files and
try this again.

	touch file1 file2
	ls
	mv -i file1 file2

Now you get a warning before doing any destructive activities!

`mv` can move and rename a file at the same time. Let's put `bark` into the
`stuff` directory and change its name back to `bar`.

	mv bark stuff/bar
	ls stuff

`mv` can move multiple things at the same time. Let's move both `file1` and
`file2` into the `stuff` directory.

	mv file1 file2 stuff
	ls stuff

### Wildcards ###

One of the most useful time-saving tricks in the shell is the use of the `*`
character as a wildcard. The `*` character matches missing characters if it
can. If we want to list the files in `stuff` that start with the letter _f_ we
do the following:

	ls stuff/f*

A very common use of the wildcard is to match all files with a specific file
extension. Let's try that.

	touch a.txt b.txt
	ls *.txt
	mv *.txt stuff

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


## Customizing your login script ... ##





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




### Programs ###

In order for a text file to function as a program it needs 3 things.

1. An interpreter directive on the first line (we just did this)
2. Permission to be executed
3. Located in the executable path

### File Permissions ###

A file can have 3 kinds of permissions: read, write, and execute. These are
abbreviated as `rwx`. If a file has read permissions, you can view it. If it
has write permissions, you can edit it, which includes deleting it. If it has
execute permissions, you can run it as a program.

Directories are special kinds of files that also have the same permissions.
Here, read means you can view the files in the directory. Write means you can
add or delete files in the directory. Execute means you can enter the
directory.

Generally, you would like to be able to read, write, and execute the
directories you own. But this isn't always true of files. You may have
downloaded some important data and want to make sure you can't modify or delete
it. Permissions allow you to modify what actions can be taken by whom.

In addition to having 3 types of permissions (read, write, execute), every file
also has 3 types of people that can access it: the owner (you), the group you
belong to (e.g. a laboratory), or the public (everyone else who has access to
the computer).

Let's examine the file permissions on the directories and files you
currently have.

	cd ~/Work
	ls -lF

You should see something like the following:

	drwxr-xr-x  2 ian ian 4096 Feb 7 10:01 bin/
	drwxr-xr-x  2 ian ian 4096 Feb 7 10:01 lib/
	drwxr-xr-x  2 ian ian 4096 Feb 7 10:11 homework/

Let's break down what's happening with the first arcane set of symbols. The
first letter is `d` which indicates that the file is a directory. We can also
see this because of the trailing slash from the `ls -F`. The next 9 characters
are 3 triplets.

+ rwx the first triplet are your permissions
+ r-x the second triplet are group permissions
+ r-x the third triplet are public permissions

You may read, write, and execute the directory. That is, you have permission to
`ls` the directory, `rm` files in the directory, and `cd` into the directory.
Users who belong to your group can also read and enter your directories, but
they can't modify their contents.

Let's take a look at the permissions of `00helloworld.py`.

	cd homework
	ls -l 00helloworld.py

On Ubuntu, this is what I found, however the default permissions for your Linux
distribution may be different.

	-rw-r--r-- 1 ian ian 44 Feb 7 11:00 00helloworld.py

After the leading dash, there are 3 triplets of symbols. The first triplet
shows user permissions `rw-`. I have read and write permission but not execute.
The next triplets are for group and public. Both have read permission, but not
write or execute. Let's first turn on all permissions for everyone using the
`chmod` command and then list again.

	chmod 777 hello_world.py
	ls -l hello_world.py

Notice that you can now see `rwx` for owner, group, and public. Does it make
sense for _everyone_ to be able to edit your files? Probably not. It also
doesn't make sense for plain text files with your shopping list to have
executable permissions. So turning everything on isn't a good idea.

The `chmod` command has two different syntaxes. The more human readable one
looks like this.

	chmod u-x 00helloworld.py
	ls -l 00helloworld.py

This command says: "change the user (u) to remove (-) the execute (x) permission
from file hello_world.py". You add permissions with +.

	chmod u+x 00helloworld.py
	ls -l 00helloworld.py

The less readable `chmod` format assigns all parameters in octal format
simultaneously. Once you understand how it works, it's much easier.

+ 4 is read permission
+ 2 is write permission
+ 1 is execute permission
+ 0 is no permissions

Every number from 0 to 7 results in a unique set of permission.

| Read | Write | Exec | Sum | Meaning
|:----:|:-----:|:----:|:---:|:--------
|   4  |   0   |   0  |  4  | only reading allowed
|   4  |   2   |   0  |  6  | reading and writing allowed
|   4  |   2   |   1  |  7  | reading, writing, and executing allowed
|   4  |   0   |   1  |  5  | reading and executing allowed
|   0  |   0   |   0  |  0  | nothing allowed

Here are some useful permission sets:

+ 600 your private diary (only you can read and write)
+ 644 your source code (you can read and write, others can read)
+ 755 your programs (like above, but executable)
+ 444 data files (everyone can read, nobody can write)

Let's set the permissions on `00helloworld.py` to the most appropriate set
using the octal format.

	chmod 755 00helloworld.py

### Making hello_world.py Executable ##

Now that your 0hello_world.py program has execute permissions, you can use it
like a Unix program. That is, you don't have to type `python3` before the
program name.

	./hello_world.py

But what's with the `./` before the program name. You don't have to type that
when you run the `ls` command or the `chmod` command, for example. That's
because those programs are in your **executable path** and `00helloworld.py` is
not. We'll fix that in a sec.

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

### PYTHONPATH ###

Just like your shell needs to know where your programs live, Python needs to
know where your libraries live. It's going to be a while before we are writing
our own libraries, but we should set things up for that later. It looks very
similar to the PATH setup you just did.

	export PYTHONPATH=$PYTHONPATH:$HOME/Work/lib

### Finally a Program ###

It's finally time to make `00helloworld.py` work like `ls` and such. Where were
we with what we needed to do?

1. An interpreter directive on the first line (we did this before)
2. Permission to be executed (we did this recently)
3. Located in the executable path

We have a few options here:

1. Move the file from homework to `~/Work/bin`
2. Copy the file from homework to `~/Work/bin`
3. Alias the file from homework to `~/Work/bin`

We don't want to move the file because then it's no longer in our repo. We also
don't want to copy the file because then we'll have 2 files running around and
edits in one won't be reflected in the other. The best thing is to use an alias
so that the shortcut in `~/Work/bin` points to the original file. While we're
at it, let's change the name of the program from `00helloworld.p` to
`helloworld`.

	cd ~/Work/bin
	ln -s ../homework/00helloworld.py ./helloworld

That's it, you're done. Now you can type `helloworld` in your terminal and the
program runs just like `ls` or any other proper CLI program. Note that you
generally don't need to do this. There's nothing wrong with `python3
filename.py` to invoke your python programs.



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

### Programs ###

In order for a text file to function as a program it needs 3 things.

1. An interpreter directive on the first line (we just did this)
2. Permission to be executed
3. Located in the executable path

### File Permissions ###

A file can have 3 kinds of permissions: read, write, and execute. These are
abbreviated as `rwx`. If a file has read permissions, you can view it. If it
has write permissions, you can edit it, which includes deleting it. If it has
execute permissions, you can run it as a program.

Directories are special kinds of files that also have the same permissions.
Here, read means you can view the files in the directory. Write means you can
add or delete files in the directory. Execute means you can enter the
directory.

Generally, you would like to be able to read, write, and execute the
directories you own. But this isn't always true of files. You may have
downloaded some important data and want to make sure you can't modify or delete
it. Permissions allow you to modify what actions can be taken by whom.

In addition to having 3 types of permissions (read, write, execute), every file
also has 3 types of people that can access it: the owner (you), the group you
belong to (e.g. a laboratory), or the public (everyone else who has access to
the computer).

Let's examine the file permissions on the directories and files you
currently have.

	cd ~/Work
	ls -lF

You should see something like the following:

	drwxr-xr-x  2 ian ian 4096 Feb 7 10:01 bin/
	drwxr-xr-x  2 ian ian 4096 Feb 7 10:01 lib/
	drwxr-xr-x  2 ian ian 4096 Feb 7 10:11 homework/

Let's break down what's happening with the first arcane set of symbols. The
first letter is `d` which indicates that the file is a directory. We can also
see this because of the trailing slash from the `ls -F`. The next 9 characters
are 3 triplets.

+ rwx the first triplet are your permissions
+ r-x the second triplet are group permissions
+ r-x the third triplet are public permissions

You may read, write, and execute the directory. That is, you have permission to
`ls` the directory, `rm` files in the directory, and `cd` into the directory.
Users who belong to your group can also read and enter your directories, but
they can't modify their contents.

Let's take a look at the permissions of `00helloworld.py`.

	cd homework
	ls -l 00helloworld.py

On Ubuntu, this is what I found, however the default permissions for your Linux
distribution may be different.

	-rw-r--r-- 1 ian ian 44 Feb 7 11:00 00helloworld.py

After the leading dash, there are 3 triplets of symbols. The first triplet
shows user permissions `rw-`. I have read and write permission but not execute.
The next triplets are for group and public. Both have read permission, but not
write or execute. Let's first turn on all permissions for everyone using the
`chmod` command and then list again.

	chmod 777 hello_world.py
	ls -l hello_world.py

Notice that you can now see `rwx` for owner, group, and public. Does it make
sense for _everyone_ to be able to edit your files? Probably not. It also
doesn't make sense for plain text files with your shopping list to have
executable permissions. So turning everything on isn't a good idea.

The `chmod` command has two different syntaxes. The more human readable one
looks like this.

	chmod u-x 00helloworld.py
	ls -l 00helloworld.py

This command says: "change the user (u) to remove (-) the execute (x) permission
from file hello_world.py". You add permissions with +.

	chmod u+x 00helloworld.py
	ls -l 00helloworld.py

The less readable `chmod` format assigns all parameters in octal format
simultaneously. Once you understand how it works, it's much easier.

+ 4 is read permission
+ 2 is write permission
+ 1 is execute permission
+ 0 is no permissions

Every number from 0 to 7 results in a unique set of permission.

| Read | Write | Exec | Sum | Meaning
|:----:|:-----:|:----:|:---:|:--------
|   4  |   0   |   0  |  4  | only reading allowed
|   4  |   2   |   0  |  6  | reading and writing allowed
|   4  |   2   |   1  |  7  | reading, writing, and executing allowed
|   4  |   0   |   1  |  5  | reading and executing allowed
|   0  |   0   |   0  |  0  | nothing allowed

Here are some useful permission sets:

+ 600 your private diary (only you can read and write)
+ 644 your source code (you can read and write, others can read)
+ 755 your programs (like above, but executable)
+ 444 data files (everyone can read, nobody can write)

Let's set the permissions on `00helloworld.py` to the most appropriate set
using the octal format.

	chmod 755 00helloworld.py

### Making hello_world.py Executable ##

Now that your 0hello_world.py program has execute permissions, you can use it
like a Unix program. That is, you don't have to type `python3` before the
program name.

	./hello_world.py

But what's with the `./` before the program name. You don't have to type that
when you run the `ls` command or the `chmod` command, for example. That's
because those programs are in your **executable path** and `00helloworld.py` is
not. We'll fix that in a sec.

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

### PYTHONPATH ###

Just like your shell needs to know where your programs live, Python needs to
know where your libraries live. It's going to be a while before we are writing
our own libraries, but we should set things up for that later. It looks very
similar to the PATH setup you just did.

	export PYTHONPATH=$PYTHONPATH:$HOME/Work/lib

### Finally a Program ###

It's finally time to make `00helloworld.py` work like `ls` and such. Where were
we with what we needed to do?

1. An interpreter directive on the first line (we did this before)
2. Permission to be executed (we did this recently)
3. Located in the executable path

We have a few options here:

1. Move the file from homework to `~/Work/bin`
2. Copy the file from homework to `~/Work/bin`
3. Alias the file from homework to `~/Work/bin`

We don't want to move the file because then it's no longer in our repo. We also
don't want to copy the file because then we'll have 2 files running around and
edits in one won't be reflected in the other. The best thing is to use an alias
so that the shortcut in `~/Work/bin` points to the original file. While we're
at it, let's change the name of the program from `00helloworld.p` to
`helloworld`.

	cd ~/Work/bin
	ln -s ../homework/00helloworld.py ./helloworld

That's it, you're done. Now you can type `helloworld` in your terminal and the
program runs just like `ls` or any other proper CLI program. Note that you
generally don't need to do this. There's nothing wrong with `python3
filename.py` to invoke your python programs.

## Editors and IDEs ##

It's time to stop using `nano`. While it is useful for very small tasks, it's
not a great programming editor. Most of us are more efficient navigating
documents with a mouse than a keyboard. All of the files you have been editing
with `nano` could have been edited with Atom, BBEdit, Geany, Gedit, Jedit,
Notepad++, Sublime, etc.

Some people prefer programming in an Integrated Development Environment (IDE).
Popular IDEs for Python include IDLE, PyCharm, Spyder and Eclipse. IDEs can
make debugging easier as they automatically place your cursor at lines with
bugs and let you manually inspect variable contents. While IDEs may make your
Python programming more efficient, they separate you from Unix. Since one of
the reasons you are taking this course is to learn some Unix, I don't recommend
using an IDE at this time.

So which programming/text editor should you use? Whatever is installed by
default in your Linux distribution should be fine. I use Geany on Linux, BBEdit
on Mac, and Notepad++ on Windows.

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

| Token   | Function
|:--------|:-------------------------------------|
| .       | your current directory (see pwd)
| ..      | your parent directory
| ~       | your home directory (also $HOME)
| ^C      | send interrupt signal
| ^D      | send end-of-file character
| tab     | tab-complete names
| *       | wildcard - matches everything
| \|      | pipe output from one command to another
| >       | redirect output to file

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
| `date`    | `date`        | print the current date
| `df`      | `df -h .`     | display free space on file system
| `du`      | `du -h ~`     | display the sizes of your files
| `git`     | `git add f`   | start tracking file f
|           | `git commit -m "message"` | finished edits, ready to upload
|           | `git push`    | put changes into repository
|           | `git pull`    | retrieve latest documents from repository
|           | `git status`  | check on status of repository
| `grep`    | `grep p f`    | print lines with the letter p in file f
| `gzip`    | `gzip f`      | compress file f
| `gunzip`  | `gunzip f.gz` | uncompress file f.gz
| `head`    | `head f`      | display the first 10 lines of file f
|           | `head -2 f`   | display the first 2 lines of file f
| `history` | `history`     | display the recent commands you typed
| `kill`    | `kill 1023`   | kill process with id 1023
| `less`    | `less f`      | page through a file
| `ln`      | `ln -s f1 f2` | make f2 an alias of f1
| `ls`      | `ls`          | list current directory
|           | `ls -l`       | list with file details
|           | `ls -la`      | also show invisible files
|           | `ls -lta`     | sort by time instead of name
|           | `ls -ltaF`    | also show file type symbols
| `man`     | `man ls`      | read the manual page on ls command
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




+ Use tab-completion
+ Use the up-arrow
