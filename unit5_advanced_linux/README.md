Unit 4: Advanced Linux
======================

## Learning Objectives ##

+ Make your libraries work anywhere
+ Make your programs into executables that work anywhere
+ Monitor resources



+ IPC, exit codes, memory usage, top
+ Running other programs
+ Reading from stdin
+ argparse


------------------------------------------------------------------------------

## Library Path ##

Currently, the `mcb185.py` library needs to be in the same directory as the
program that imports it. That's not the way the math library works. You can use
that in any program. To make `mcb185.py` available to other programs, Python
needs to know where to find it. There are several ways to do this. We are going
to use the PYTHONPATH environment variable.

In your terminal, type the following line:

```
PYTHONPATH=$HOME/Code/homework
```

This sets your PYTHONPATH environment variable to include your homework
directory. To verify this works, enter the interactive mode of python by typing
`python3` and hitting return. You will now get a prompt that looks like '>>>'.
You can start typing anything you want and python will interpret it as python.
Try doing some math.

```
3 + 5
v = 7
v *= 7
v
```

To check if `mcb185` can be found, do an import statement. If that works, also
try something else so you know what the error looks like. If it doesn't work,
ask for help, as something is wrong.

```
import mcb185
import blahblahblah
```

Your homework directory isn't the best place to keep libraries. Instead, put
your libraries in `~/Code/lib`. Since `~/Code/lib` isn't under git control,
we'll put a symbolic link in there instead of the actual file.

```
cd ~/Code
mkdir lib
ln -s ~/Code/homework/mcb185.py lib
ls -lF lib
```

Now `mcb185.py` appears to be inside your `~/Code/lib` and with one more change
it will be available to any of your future python programs. Edit your login
script and add the following line.

```
PYTHONPATH=$HOME/Code/lib
```

------------------------------------------------------------------------------

## Executable Programs ##

So far, all of your python programs have started with `python3 ...`. But most
Unix programs don't require you to type `python3` before hand. For example,
`ls` is just what it is, rather than `python3 ls`.

In the last homework, you wrote `42dust.py`. We're going to make this into an
executable called `dust` that you can run from anywhere on your computer, just
like `ls`.

We need to do 3 things.

1. Modify `42dust.py` to have an interpreter directive
2. Give `42dust.py` executable permissions
3. Put `42dust.py` in the executable path as `dust`

## Interpreter Directive ##

An interpreter directive is the first line of a text file that tells the shell
what interpreter to use. Since we're programming in Python, the line you need
to add to your file is this:

```
#!/usr/bin/env python3
```

This must be the first line of your program. The first characters must be `#!`.
Any extra spaces at the front will cause failure.


## File Permissions ##

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
it. For example, the files in your `~/DATA` directory should be read-only.

Permissions allow you to modify what actions can be taken by whom. In addition
to having 3 types of permissions (read, write, execute), every file also has 3
types of people that can access it: the owner (you), the group you belong to
(e.g. a laboratory), or the public (everyone else who has access to the
computer).

Let's examine the file permissions on the directories and files you
currently have.

```
cd ~/Code
ls -lF
```

You should see something like the following:

```
drwxr-xr-x  2 ian ian 4096 Feb 7 10:11 homework/
drwxr-xr-x  2 ian ian 4096 Feb 7 10:01 lib/
drwxr-xr-x  2 ian ian 4096 Feb 7 10:11 MCB185-2023/
```

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

```
cd ~/Code/homework
ls -lF 00helloworld.py
```

On Ubuntu, this is what I found, however the default permissions for your Linux
distribution may be different.

```
-rw-r--r-- 1 ian ian 44 Feb 7 11:00 00helloworld.py
```

After the leading dash, there are 3 triplets of symbols. The first triplet
shows user permissions `rw-`. I have read and write permission but not execute.
The next triplets are for group and public. Both have read permission, but not
write or execute. Let's first turn on all permissions for everyone using the
`chmod` command and then list again. The numbers below will be explained
shortly.

```
chmod 777 00helloworld.py
ls -lF 00helloworld.py
```

Notice that you can now see `rwx` for owner, group, and public. This means that
everyone has read, write, and execute permissions. That's probably not a good
idea. Let's turn all permissions off. Now, even you don't have permission to
view the file (which is why the `less` fails below).

```
chmod 000 00helloworld.py
less 00helloworld.py
```

The `chmod` command has two different syntaxes. The more human readable one
looks like this.

```
chmod u+r 00helloworld.py
ls -lF 00helloworld.py
```

The `u+r` reads as: "(u) user (+) add (r) read permission". The less readable
`chmod` format assigns all parameters in octal format simultaneously. Once you
understand how it works, it's much easier.

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

```
chmod 644 00helloworld.py
```

Let's also set the permission of your `42dust.py` program to be executable,
since that was part of the original goal.

```
chmod 755 42dust.py
```

Let's also change all of the data files to be read-only, as they should have
been all along.

```
chmod 444 ~/DATA/E.coli/*
```

One last note about permissions. Not all file systems have the same ideas when
it comes to file permissions. Mac and Unix generally play well together, but
not always with Windows. If you get a file from a flash drive, it will
generally have all permissions on (i.e. `777`). When working with two different
operting systems on the same file system, sometimes all of the permissions will
get set to `000`, meaning no access even by you. If this happens, you can reset
your permission as `644` or whatever your preference is. One of the reasons
that WSL is not recommended is because this shit happens all the time.

## Executable Path ##

When you type `ls` at the command line, the shell needs to find the program
somewhere in your file system. To find out the actual location of the program,
use the `which` command. You will find that `ls` and `python3` are in different
places.

```
which ls
which python3
```

Programs aren't all stored in the same place. Some are in `/bin`, while others
are in `/usr/bin`, `/sbin`, or elsewhere. By default, you don't have permission
to put your programs in these locations. In order to make your personal
programs behave like proper Unix programs, we have to create a place to store
your progams and add that to the executable path.

Just like the case for your library files, we'll create a directory under
`Code` and link in the files. Note that the symbolic link doesn't have the
exact same name as the previous file. You're allowed to name your symbolic
links anything you want (within reason). Since we want `42dust.py` to run more
simply as `dust`, this is one way to accomplish that.

```
mkdir ~/Code/bin
cd ~/Code/bin
ln -s ~/Code/homework/42dust.py ./dust
```

Since `dust` has an interpreter directive and exectuable permission, you can
now run it as an executable or as input to python.

```
python3 dust
./dust
```

We aren't quite done. You can't run `dust` without using the whole path (that's
why there is a `./` on the front of the command).

```
cd
~/Code/bin/dust
dust
```

The last part is to edit your PATH. Let's look at it now.

```
printenv PATH
```

This is a colon-delimited list of directories. This is where the shell looks
for executables. Your `Code/bin` isn't there, so we have to add it to your
login script. Edit your loging script to include:

```
PATH=$PATH:$HOME/Code/bin
```

This appends your `Code/bin` to the end of whatever was already in `PATH`. Open
a new terminal and now you can `dust` from anywhere you like.

------------------------------------------------------------------------------

## Monitoring Resources ##

Bioinformatics data can be huge, so it's important to know how to monitor how
much of the various computer resources you're using (disk, CPU, RAM, network).

To see how much space you have left on you hard-disk (even though it's an SSD)
use the "disk free" command `df`. With the `-h` option, you will get human
readable sizes (like 5G).

```
df -h
```

To get the sizes of files and directories, use `du -h`. This can descend very
deeply into directories, so it's often useful to pass `--max-depth` so you
don't see a thousand files.

```
du -h --max-depth ~/Code
```

The Linux equivalent of "Task Manager" or "System Monitor" is `top` or `htop`.
These show which processes are currently running on your computer and what
resources they are using. To get out of either of these, hit "q".

```
top
```

To get information about your physical computer, the files `/proc/cpuinfo` and 
`/proc/meminfo` are available in Linux (not Mac).

```
less /proc/cpuinfo
less /proc/meminfo
```

If you want to estimate how long a job is going to take, it's often useful to 
`time` a subset of the problem. For example, if you were going to align all 
human genes to all drosophila genes, you might time how long it takes to align 
100 genes and then multiply that by 200 to estimate the whole time (given that 
humans have around 20,000 genes). `time` is also useful when benchmarking 
different algorithms to figure out how much faster one is than another.

```
time zcat ~/DATA/E.coli/*.gz | wc
```

This shows the real, wallclock time, as well as user and system time. The 
amount of CPU used is the user + system time. The real time reported can be 
longer if the computer is waiting around (e.g. for network). For programs that 
use multiple CPUs, the user and system times may be much longer than real time.

------------------------------------------------------------------------------


## Text Processing ##

Python is a powerful tool for text processing, but Unix has some built-in tools 
that are so convenient, you'll sometimes use them instead. These include:

+ cut - for cutting out columns of a table
+ grep - for finding patterns
+ sort - for sorting

Let's start by making some soft links to keep the command lines a bit shorter.

```
ln -s ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz prots.gz
ln -s ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gff.gz gff.gz
```

To print out all the definition lines, we can `grep` for the greater-than sign.

```
zcat prots.gz | grep ">"
```

To count how many proteins there are, we pipe to `wc`.

```
zcat prots.gz | grep ">" | wc
```

Let's now look at all of the lines that aren't definition lines. This is simply 
passing the `-v` option to `grep`.

```
zcat prots.gz | grep -v ">" | less
```

The `cut` program allows us to get columns of data. The usual delimiter is tab, 
but we can change that to anything. Let's use a space as the delimiter and grab 
the database identifiers from the fasta file definition lines. The id is always 
the first part of the definition line, so "field 1" or `-f 1`.

```
zcat prots.gz | grep ">" | cut -d " " -f 1
```

Take a look at the gff file.

```
zless gff.gz
```


There's a lot of stuff in there. The lines that begin with # are comments. All 
of the other lines contain tab-delimited information about the genes and other 
features. The first 6 columns of GFF are the following:

1. sequence name
2. source
3. type
4. begin
5. end
6. strand

Let's ignore the comment lines and then pull out all of the sequence names.

```
zcat gff.gz | grep -v "^#"  | cut -f 1
```

It looks like all of the values are the same. That makes sense if the genome is 
described by one circular chromosome and none of the plasmids. To be sure, 
let's send the output to `sort -u`, which will make a unique list.

```
zcat gff.gz | grep -v "^#"  | cut -f 1 | sort -u
```

In fact, there is only one chromosome. How many sources and types are there? 
This is as simple as changing the argument to `cut`.

```
zcat gff.gz | grep -v "^#"  | cut -f 2 | sort -u
zcat gff.gz | grep -v "^#"  | cut -f 3 | sort -u
```

The source of all features is "RefSeq", however there are many types of 
features including CDS, exon, gene, pseudogene, etc. If you wanted to count the 
number of "gene" features, you might be tempted to grep for gene. However, this 
doesn't really work because the word "gene" occurs in more places that just 
field 3.

```
zcat gff.gz | grep -v "^#"  | grep gene | wc
```

No, E. coli doesn't contain 9477 genes. There are are a number of ways to get 
the correct number but we will leave this as a cautionary note and move on.

------------------------------------------------------------------------------

## What's Missing ##

There's a lot more we could discuss in an Advanced Linux section. Here are some 
topics we won't be covering, but you will run into at some point in the future.

+ Clusters: nice, nohup, screen, sga, slurm
+ File managemant: curl, find, rsync, scp, sftp, wget
+ Job control: bg, fg, jobs, ps
+ Pipelines: make, snakemake, xargs
+ Scripting quickly: awk, perl, sed
+ Signals and exit codes

------------------------------------------------------------------------------

## Python ##

The `dust` program we made previously now works like a typical Unix command, 
but it doesn't really look like one. All programs should have _usage 
statements_ that tell users how to interact with the program. Usage statements 
are a simple form of essential documentation. Usage statements are usually 
displayed if you give a `-h` or `--help` on the command line.

```
gzip -h
wc --help
```

Check out the `demos` directory to see some examples of how to make proper 
usage statements in Python. You will also see how to read from stdin and how
to read the output from other programs.

There is also homework in the `programs` directory as usual.
