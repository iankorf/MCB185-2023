Unit 0: Tools of the Trade
==========================

## Outline ##

+ Install Linux
+ Explore the Unix CLI with the terminal and shell
+ Choose a programming editor
+ Organize your home directory
+ Manage documents with Git
+ Write documentation with Markdown
+ Write your first Python program

------------------------------------------------------------------------------

## Unix/Linux ##

Most professional bioinformatics is done in a Unix/Linux environment. You don't
have to love Unix/Linux, but you do have to be proficient at it. The file,
`REFERENCE.md`, contains all of the Unix commands we use in the course (also
all of the Python programming concepts).

### What's the deal with Unix vs. Linux? ###

Most people about to embark on an adventure in bioinformatics programming will
be using some flavor of Linux (e.g. Debian, Fedora, LinuxLite, Mint, Ubuntu,
etc.) and not actually Unix. Is there a difference between Linux and Unix? No
and yes. Linux was designed to be just like Unix, so from a practical
standpoint they are very similar. Despite looking the same, they share no
source code in common. The biggest difference is philosophical. Unix is a
commercial product and Linux is free open source software (FOSS). From a
philosophical perspective, they are very different. In this document, the terms
_Linux_ and _Unix_ are used somewhat interchangeably.

### Where do I get Linux? ###

Before we begin, you need a command line Linux environment on your computer.
Why a CLI (command line interface) rather than a GUI (graphical user
interface)? When it comes to automating tasks, it's easier to automate text
commands than mouse clicks. Also, most computer clusters run Linux because it's
free and robust. For these reasons, most professional bioinformatics is done
with a Linux CLI. If you have any aspirations of becoming a bioinformatics
programmer, you need to become comfortable with the Linux CLI. But before we
get to that, you need Linux.

### Unix on Mac ###

If your computer is a Mac, you already have Unix installed, and your specific
flavor of Unix is called Darwin. You can get to the CLI with the _Terminal_
application. However, you might not have `git` and other developer tools
installed by default. To install these, type the following in your terminal and
follow the instructions:

```
xcode-select --install
```

By default, your home directory might not be shown in your sidebar. If you want
it there, change that in Finder->Preferences.

### Linux on PC ###

If your computer is a PC currently running Windows, you will have to install
Linux _somehow_ and you have several choices. Each of these has advantages and
disadvantages, which are described in more detail below.

+ Virtual machine - recommended
+ Install Linux on a PC - best if you have a spare PC
+ Cygwin - good for advanced users
+ Git bash - good for advanced users
+ Windows Subsystem for Linux - official Microsoft solution (not recommended)
+ Chromebook - inexpensive and works okay
+ Raspberry Pi - fun little gizmo
+ Remote login - a little inconvenient at times

### Virtual Machine ###

This is the current recommendation for Linux on a PC.

A virtual machine (VM) is a _fictional_ computer running inside your normal
Windows operating system. The virtualization _host_ software (e.g. VirtualBox)
running on the Windows PC (host) tricks the new _guest_ operating system
(Linux) into thinking it is attached to its own motherboard, CPU, keyboard,
mouse, monitor, etc.

The upside of virtualization is that it's safe and inexpensive. It's hard to
destroy data on your computer and you don't have to buy any new hardware.
VirtualBox is free software that works very well. Other popular virtualization
products include VMware and Parallels. If you want commercial support, you may
like those.

The downside of a VM is that your virtual machines will take away some RAM,
CPU, and storage from your host OS. RAM is the most critical resource because
it isn't easily shared. If you have less than 8 GB of RAM in your computer, you
will probably not want to run a VM.

On the CPU side, your programs running in a VM will run slower than they could.
The difference is pretty negligible though. We're talking 1-10% slower. You
will also have to dedicate about 20 GB of hard disk space. Even with the
downsides, VMs are a great way to run Linux on your PC.

One additional complication is that your BIOS might need to be modified to run
virtual machines. Some manufacturers ship their products with virtualization
disabled. This is easily changed in BIOs. Hold down the F10 key - or sometimes
it's F1, F2, F12, or DEL to enter BIOS. Navigate to CPU (sometimes it's in
security). Enable virtualization, save changes, and reboot.

There are many distributions of Linux. The most obvious differences among them
is the default desktop Graphical User Interface (GUI). Some look like
old-school Windows while others look like Mac OS, and still others offer their
own unique look and feel. Here are some recommendations for setting up your VM.

+ Linux: Lubuntu
+ VM Memory: 2 GB (or 4 GB if your computer has more than 8 GB)
+ Disk: use default types, 40G is a good amount

Make sure you read the installation directions fully. There are some
post-install customizations you might need to do. On VirtualBox these include:

+ Install the Guest Additions "CD"
+ Switch the virtual video card if you can't resize the screen
+ Set up a shared folder if you want Linux and Windows to share files
+ Set up shared clipboard if you want to copy-paste between host and VM

If you're having problems with the install or post-install, ask for help.

Mac users can also install VMs, but the experience is sometimes not as good as
PC users.

### Install Linux on PC ###

This is the native way to run Linux, but it may change your PC permanently.

There are a variety of ways you can install Linux on a hard disk. This could be
an external hard disk you plug in when you want to run Linux (e.g. a flash
drive), or you can split your current hard disk into multiple partitions, or
you can wipe Windows and install Linux instead. All of these methods will give
you Linux with all of the RAM and CPU. Each one is slightly destructive,
however, and you may accidentally wipe your Windows partition even if you
didn't intend to. For these reasons, if you only have 1 computer, I don't
recommend installing Linux directly. Use VirtualBox or Cygwin instead. However
if you do have a spare computer, installing Linux will give you that fully
immersive experience that helps you learn Linux faster.

You can sometimes pick up old PCs for $50. Old Macs make great Linux boxes. I
have a 2015 iMac and 2012 Mac Mini that are too old to work with the current
MacOS, but both continue to work flawlessly as Linux machines.

### Cygwin on Windows ###

Cygwin is not an entire operating system but rather a terminal with POSIX
commands (POSIX is a standard for portable Unix). Cygwin does not come
pre-installed with Python, so you will have to run the Cygwin `Setup.exe` to
install it and possibly other programming tools (git, nanot). For basic Python
programming, I've found Cygwin to work great. However, installing some external
libraries can be frustrating. Since we don't use external libraries in this
course, Cygwin will work great. Later, it may become a pain.

Your Windows C drive is mounted at `/cygdrive/c`. Your Cygwin root depends on
where you chose to install it (probably `C:\cygdrive64`).

### Git Bash on Windows ###

Git Bash is software intended for running git commands on Windows PCs using a
command line interface. It can be used for more tasks, such as Python
programming. Some programming languages are built-in (e.g. Perl) but Python is
not by default. Git Bash feels very similar to Cygwin but software installation
is slightly more complex.

### Windows Subsystem for Linux ###

The official Microsoft solution for running Linux is called the Windows
Subsystem for Linux (WSL). There are two types of WSL, Type 1 and Type 2. Type
1 is older. It is also compatible with virtual machines like VirtualBox. If you
want to run both WSL and VirtualBox on the same machine, you should use WSL
Type 1.

If you want to be more up-to-date, then use WSL Type 2. Unfortunately,
installing WSL2 will stop VirtualBox from running. You can have WSL2 and
VirtualBox on the same computer, but not running at the same time; you will
have to edit some settings and restart to switch between the two. This is a
pain, so don't do it.

The upside of WSL is that it is the official Microsoft product. Most of the
time it works great. It uses less resources than a VM, so your actual and
virtual computers will be faster with WSL. The downside of WSL is the Windows
and Linux filesystems do not play well together. When Windows programs save
files in the Linux filesystem, some permissions may get reset (meaning you
can't read or write files until until you `chmod`). It can be annoying. As WSL
matures, it may become the best way to run Linux on Windows, but as of now I
don't recommend it.

From WSL, your Windows C drive is conveniently mounted at `/mnt/c`. Finding
your Linux filesystem root from Windows is not so easy.

### Linux on Chromebook ###

Chromebooks are some of the least expensive computers you can buy.
Conveniently, Linux is built right in. Select the clock from the lower right
corner and then go to Settings->Advanced->Developers.

Scroll down to "Linux development environment" and turn it on. It takes a few
minutes to install. To get to the Linux CLI, use the Terminal application. This
takes a little while to launch the first time.

I don't really recommend Chromebooks because it's not a popular platform for
professional bioinformatics work. However, they will work great for this
course.

### Raspberry Pi ###

The Raspberry Pi is an inexpensive ($50-100) single board computer that is
about the size of a deck of cards. You can also get one built into a slim
keyboard. They use Linux as their OS. You just need to provide a mouse,
keyboard, and monitor. They work great as a learning platform, but can be
limiting later on as some useful bioinformatics software isn't compiled for the
Pi.

### Remote Login ###

Another way to work with Linux is to use your computer as a terminal to another
computer located somewhere on the Internet. This might be part of a larger
cloud computing service (e.g. Google, Amazon, etc.) or a computer located at
your school. The downside here is that you'll need a network connection and
you'll need to figure out how to edit remote files from your favorite desktop
editor (unless you like terminal-based editors).

### Linux on Tablet ###

I don't have any experience with Linux on tablets. I've seen it done, and it
seems to work okay, but I expect there will be some issues with precompiled
binaries as there are with the other cellphone-chip-based solutions (Pi,
Chromebook).

------------------------------------------------------------------------------

## Unix CLI: Terminal & Shell ##

There are many terminal applications. Generally, it doesn't matter which one
you use. It's sort of like choosing between Firefox and Chrome: they look a
little different, but both let you navigate the Internet. Find a terminal
application on your computer. The name might be 'Terminal', 'xterm', 'Qterm' or
something with 'term' in it somewhere. Create a shortcut in your dock/launchbar
so you can access it quickly.

The terminal is the application where you use the command line interface (CLI)
to make things happen.

Every terminal has a command line interpreter called a shell. There are many
flavors of shell with names like `sh`, `bash`, `zsh`, `csh`, `ksh`, etc. The
shell interprets what you type on the command line. For example, when you type
`ls` followed by return, the shell interprets that to mean you want to run the
`ls` program. The shell is actually a programming language. The various flavors
of shell are like different dialects. We won't be using many features of shell
programming in this course, so the choice of shell doesn't really matter.

------------------------------------------------------------------------------

## Programming Editor ##

You will spend a lot of time using a text editor designed for programming. A
text editor is not a word processor. We won't be using MS Word or Google Docs
ever. Popular text editors include:

+ Sublime Text
+ Atom
+ Notepad++ (Windows only)
+ BBedit (Mac only)
+ Caret (Chromebook only)

If you're using a VM, the Linux distribution will come bundled with an
acceptable editor like FeatherPad or gedit. However, you're encouraged to
explore other editors. You will be spending a lot of time editing code, so you
might as well use one you like.

A lot of programmers use an IDE (integrated development environment). This is
sort of like having your editor, terminal, and other useful stuff all in one
application. Popular IDEs include:

+ Visual Studio
+ Eclipse
+ PyCharm
+ IDLE

We will not be using IDEs in this class. One of the goals of the class is for
you to become Unix savvy, so I want you using the terminal as much as possible.
If you want to use an IDE solely as an editor, that's fine.

Another useful technology we won't be using is Jupyter. Notebook computing is
very powerful and intuitive, but it doesn't lend itself to creating
distributable software. It also isolates you from Unix.

### LF vs CRLF ###

All of the files we use in this course are text files. Text files are just a
bunch of letters, numbers, and punctation with no real formatting. Text files
exist in Linux, Mac, and Windows. However, there may be slight differences
among them.

+ Unix uses a linefeed (LF) at the end of a line
+ Windows uses carriage return plus linefeed (CRLF) at the end of a line
+ Mac used to use carriage return (CR) at the end of a line, but now LF

All files should use Unix (LF) line endings. If you're on a Windows computer,
you may run into some CRLF text files. By default, your programming editor may
be set up to use CRLF. You'll want to change that as some Linux programs won't
work with Windows line endings.

Most Mac software has switched over to LF line endings, but check your editor
to make sure it doesn't use CR.


### Editor Customization ###

Every source code editor has a lot of options. Make sure your editor is set up
for the following:

+ Syntax highlighting for Python
+ Displays line numbers (helps when discussing code)
+ Tab key inserts tab character (not spaces)
+ Shows 80-column gutter (we follow the 80-column rule)
+ Saves with Unix line ending (LF) by default, not Windows (CRLF)

In addition, you might want to change the theme. Some people like light
characters on a dark background while others prefer the reverse. You should
theme the terminal similarly to the editor.



------------------------------------------------------------------------------

## Home Directory ##

The CLI always has a **focus**. When you first start up your terminal, the
focus is your home directory. To examine the contents of your home directory,
start up your terminal and they type:

```
ls
```

The `ls` command lists and sorts your files. You will probably see directories
(folders) for Desktop, Documents, and Downloads, as well as other directories
that depend on your operating system. Your home directory is located at a
specific point in your filesystem. The root of the Unix filesystem is `/`. All
directories and files are hierarchically under "slash". For example, your home
directory might be in `/home/your_name`. The exact location depends on your
operating system. Let's examine the path to your home directory with the `pwd`
command, which stands for "print working directory".

```
pwd
```

To change directory, use the `cd` command. Let's change to the `Desktop`
directory.

```
cd Desktop
```

If that last command had an error, make sure you spelled everything correctly.
Unix is case-sensitive, so `desktop` and `Desktop` are not the same thing
(except weirdly on Macs where some filesystems are not case-sensitive). Now try
the `ls` command again and you will see the path to your current focus has
changed. That's because the current focus of the `ls` command is your `Desktop`
directory.

```
ls
pwd
```

To get back to your home directory, you have two choices (for now, later you
will have many more).

```
cd
cd ~
```

Using `cd` by itself will change focus to your home directory. Your home
directory is so important that there is a simple shortcut to get to it: the
tilde key `~`. If you've never used this key before, it's probably at top left
of your keyboard (depends on where your keyboard was made). Try one of these
methods and check examine the location of your home with `pwd`.

### Code Directory ###

We are going to organize all of our programming efforts in a directory called
`Code`. The life cycle of source code (and other documents) can be very complex.
There may be multiple authors who contribute at various times and to varying
degrees. To manage these complex histories, we use Git (see below). Let's make
the `Code` directory in our home directory.

```
mkdir ~/Code
```

### DATA Directory ###

Data is very different from code. It tends to be huge and pretty stable. For
these reasons, code and data should be managed very differently. Data belongs
in an entirely different place, possibly not even in your home directory or
even on your physical computer (e.g. mounted over a network). Imagine a shared
computing environment where multiple users are all accessing the same file
(e.g. the human genome). It would be wasteful for each person to have a copy of
a huge data file in their home directory. Large data files should be shared in
a place where everyone can get to them (and also write-protected to prevent
them from being changed).

Let's make the `DATA` directory now.

```
mkdir ~/DATA
```

Notice that the `DATA` directory is in all caps. Why is this? Because it's
thematically different from other directories. All the contents should be
shared and read-only. For now, we'll keep it in our home directory but later
you might want to move it.


### File-naming Conventions ###

+ Use lowercase in general
+ Don't put spaces or punctuation in your file names
+ Use underscores to separate words (e.g. `human_genome.fa.gz`)
+ Use Uppercase for directories in your home directory (e.g. `Code`)

------------------------------------------------------------------------------

## Git ##

Git is the most popular version control software. While it was designed for
source code management, it can be used to manage all kinds of projects. Git
allows multiple people to work on the same files without anyone over-writing
anyone else's work. You will always know who did what and when.

## GitHub Account ##

GitHub is a website that lets you store your git repositories for free. There
are several similar sites, but GitHub is the most popular. Every bioinformatics
developer should have a GitHub account. Your repositories and activity are part
of your CV. If you don't have a GitHub account, it's time to point your web
browser to [GitHub](https://github.com) and create an account.

Choose a username. It's okay to be clever, but don't be silly. Remember, this
will be part of your CV. I use my full name. After setting your email and
password, choose the free plan and then answer a few questions about your
interests to create your account. Go to your email to verify your email
address.

### Create a Repository ###

It's time to create your first repository, which we often shorten to _repo_.
Before we begin, we need to talk a little about ownership, privacy, and
security.

When you create a repo, you own it. You can read it, write to it, or even
delete it. Later, you can invite collaborators who can join you in your
efforts, but by default, only you can make edits.

When a repo is created, it can be either _Public_ or _Private_. A Public
repository allows other people to download a copy of your repo. This is called
_cloning_. There is no security risk in cloning a Public repository (unless you
put sensitive info in there). If people modify their clones, it does not affect
your files. If you want people to be able to edit files in your repo, you have
to invite them as collaborators.

A Private repository is invisible to everyone but you. You can add
collaborators to Public or Private repos and specify what kinds of permissions
each collaborator may have. As the owner, you can change a repo from Public to
Private and back. Most of my repos are public because I believe in openly
sharing (but hands off my sandwich).

Now let's go make a repo. Go to the GitHub website and click on the green "New"
button to create a new repo. Name this "homework" because this is where you'll
be submitting your homework. Make it **public**. Does this mean that students
can see each others' homework? Yes. You're actually encouraged to work with
other students in this class. Click the checkboxes to initialize with a README,
add a .gitignore, and add a license. Scroll through the .gitignore options
until you get to "Python". Choose whichever license you like. I generally use
MIT. Click the "Create Repository" and you will be transported to your new
mostly empty repo.

### Personal Access Token ###

When you interact with the GitHub website, you use a username and password.
When you interact with GitHub using the Linux CLI, you **cannot use your
website password**. Instead you have to use a "personal access token" (PAT). So
the first thing we need to do is to generate a PAT.

Log into GitHub and then click on the icon in the top right corner. This will
drop down a menu where you will find "Settings". Follow that link and you will
get to your various account settings. Scroll down to the bottom to find
"Developer Settings". On the next page you will see "Personal access tokens".
Click on the link to "Generate a personal access token".

In the "Note" you might put in "programming" or something. It doesn't matter.

For "Expiration" you can use any of the values. If you don't want to do this
again, use the "No expiration" option.

Click on the "repo" checkbox, which will also check the subordinate boxes.

This personal access token is given to you once. Copy it and save it somewhere
safe. You can never get to this PAT again. Ever. However, you can generate a
new one anytime you like, so if you lose your PAT, you can just generate a new
one. I put my PAT in a personal message to myself in Slack. I also keep it in a
file on Dropbox.

### Cloning Repos from the CLI ###

Your current homework repo is located on GitHub, but not in your Linux
computer. Type the following commands in your terminal, substituting
`YOUR_GITHUB_HANDLE` for whatever your GitHub user name is.

```

cd ~/Code
git clone https://github.com/YOUR_GITHUB_HANDLE/homework
```

You should now see your homework directory. Also clone the MCB185-2023 repo so
that you have all of the course content on your computer.

```
git clone https://github.com/iankorf/MCB185-2023
ls
```

You should now see both your homework and the course repos in your Code
directory. Since you own your homework repo, you will be able to make changes
to it and the files on the website will change. However, you don't own
MCB185-2023 and I haven't invited you as a collaborator, so you won't be able
to make changes to my repo. You can edit the files all you want on your
computer, you just can't change the files on the website.

Let's get one more repository and put this in our `DATA` directory. Note that
most of the time data isn't managed by git. It's usually too large. But in this
case, the data is small enough that it's okay.

```
cd ~/DATA
git clone https://github.com/iankorf/E.coli
```

As the name suggests, this is some data from the E. coli genome. There are 5
files inside.

```
ls ~/DATA/E.coli
```

+ GCF_000005845.2_ASM584v2_genomic.fna.gz - genome in FASTA
+ GCF_000005845.2_ASM584v2_genomic.gbff.gz - annotation in GFF
+ GCF_000005845.2_ASM584v2_genomic.gff.gz - genome and annotation in GenBank
+ GCF_000005845.2_ASM584v2_protein.faa.gz - proteins in FASTA
+ README.md - notes about the data


### Git Commands ###

Enter your homework repository and check its status.

```
cd ~/Code/homework
git status
```

You will see that git reports that your repository is up to date. Let's modify
a file and see what happens. Edit the `README.md` file with your text editor
and save it.

After saving your changes, do another `git status`.

This shows that `README.md` has been changed. In order to put those changes
back into GitHub, you'll need to `add`, `commit`, and `push`.

```
git add README.md
git commit -m update
git push
```

The `add` argument tells `git` we intend to put this file in our repo. Not all
files in your current directory need to go into your repo. For example, you may
have some temporary program output you were using for debugging.

The `commit` tells `git` we are done with edits, and the `-m` provides a short
message about what work was done. The message might be as simple as "update" or
"edit" or "new", but might be more complex such as "finally squashed the
formatting bug". If you have edited multiple files, they will all get the same
commit message. If you want different commit tags for different files, `add`
and `commit` them separately.

Once you're done with all the `add` and `commit` work, `git push` tells git to
upload all of the modified files back to GitHub.

When git prompts you for your username, use your GitHub username. For the
password, copy-paste your GitHub personal access token.

If you don't like copy-pasting your PAT again and again, use the following
commands to make git remember you. Change "username" to your GitHub username.

```
git config --global user.name "username"
git config --global credential.helper store
```

Sometimes you will have to deal with merge conflicts. When this happens, `git`
may launch `vi` or `vim`, which are difficult to use unless you already know
how to use them. To make sure you get `nano`, type the following:

```
git config --global core.editor "nano"
```

Now let's go to the GitHub website. Look at your `README.md` there and verify
that the text has chagned. If it has not, you didn't do something right. Ask
for help and go back and fix it.

You can also edit files directly on GitHub. Click the edit button for the
`README.md` file and make some changes. Scroll to the bottom of the page and
click the green button to commit changes.

At this point, your local repository in Linux is not up to date with the repo
on GitHub. To get the latest documents you have to pull them into your local
repo. Make sure you're in your homework repo and the do a `git pull`.

```
cd ~/Code/homework
git pull
```

Your local repo now has the changes you made on the website. If you're working
on multiple computers, your git activity cycle will look like this:


1. `git pull` at the start of your session
2. edit files
3. `git push` at the end of your session

------------------------------------------------------------------------------

## Markdown and Text Files ##

Most of the files we work with in Linux are plain text files. Many things
change in this world, but not the format of text files. Got some old poetry you
wrote in WriteNow? Well, that software doesn't exist anymore, so good luck
viewing it. However, any text file since the dawn of Unix still works just
fine. Markdown files, like this one, are plain text files. However, there are
Markdown processors that will turn you Markdown files into beautiful PDF, HTML,
etc.

### Text vs Binary ###

There are two main types of files you will encounter: text and binary. You can
view text files with `less` and edit them with `nano`, for example. All of the
programs we write in this course will be plain text files. You can also view
and edit binary files but they look like gobbledygook, not English. If you want
to see what a binary file looks like, try the following.

```
less /bin/ls
```

You're looking at the machine code for the `ls` program. It's not meant to be
human-readable. So what makes a file text or binary? To answer that, we need to
delve into the world of bits and bytes.

### Bits, Bytes, and ASCII ###

A _bit_ is a single binary digit representing a 0 or 1. The number "1" is just
1 as we know it. The number "10" is 2 in decimal notation. There is a "1" in
the 2s place and a 0 in the "1s" place, so 2 + 0 = 2. Similarly, the number
"11" in binary is 3 in decimal and the number "101" in binary is "5" in decimal
(1 four, 0 two, 1 one).

A byte is 8 bits in a row. Computers usually deal in bytes. So we don't
normally talk about a number like "101" to represent 5 but rather the 8-digit
version of that "00000101". So what number is "10000000"? Well that depends if
you're working in base 2, decimal, or something else entirely. In order to
clarify these things, people often put two characters at the front to signify
the base when it's not base-10. Prepending the numerals with "0b" tells people
"I'm using binary". So "0b10000000" means 128 and not ten million.

We actually use the "byte" more frequently than you might guess. However, when
we do so, it's usually in _hexadecimal_ notation. In base 2, there are 2
symbols: 0 and 1. In base 10 (ordinary decimal) there are 10 symbols: 0, 1, 2,
3, 4, 5, 6, 7, 8 , and 9. In base 16 (hexadecimal), there are 16 symbols: 0, 1,
2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, and F. So the symbol "B" in hexadecimal
means "11" in decimal. To specify that a number is in hex, it is proceeded with
"0x". Therefore "0x10" is 16 (1 value in the 16s and nothing in the 1s).

Have you ever seen internet addresses of the form 192.168.1.1? Ever wondered
what those 4 numbers are? Each one is a byte. So each one can have a value from
"0b00000000" to "0b11111111". In other words, each value can be from "0x00" to
"0xFF". Or more familiarly, from 0 to 255. These same byte notations are used
all over the place in computers. For example, you may have had to dig up the
MAC (media access control) address of your network adapter, which may have
looked like "f0:18:98:e9:f2:be". Each of those number-like things separated by
a colon is a byte in the range of 00-ff (upper and lowercase don't matter in
hexadecimal).

### Colorspace ###

Another place you may have seen hexadecimal notation is to represent colors. In
a computer, color is made by mixing three colors of light: red, green, and
blue. Each of those colors can have an intensity from 0 to 255, which in hex is
00-FF. For example, if you want to make bright red, you use FF in the red
channel, 00 in the green channel, and 00 in the blue channel. The most
efficient way to write this is to mash them all together as FF0000. This can
also be written as 0xFF0000 or even #FF0000.

Here are some common colors:

+ FF0000 Red (only the red channel)
+ 00FF00 Green (only the green channel)
+ 0000FF Blue (only the blue channel)
+ 000000 Black (all channels off)
+ FFFFFF White (all channels on)
+ 808080 Gray (all channels at half)

If you think about the color spectrum, yellow is halfway between red and green.
So how do we make a color halfway between the two? By turning on those two
channels. Similarly, halfway between green and blue is cyan. If you think of
the spectrum as a circle rather than a line, then halfway between blue and red
is magenta.

+ FFFF00 Yellow
+ 00FFFF Cyan
+ FF00FF Magenta

What about the other colors, such as orange? Orange isn't halfway between any
of the channels. However, it is halfway between red and yellow. To make orange,
we have to decrease the green channel so that the average is closer to red. How
about we cut the green in half? FF8000 = Orange.

At this point, you're probably asking yourself, "but what about all of that
stuff I learned in art class where red + green = brown?". Paints are pigments,
not sources of life. You have to think about those in the absorption spectrum.
Red pigment block green and blue, allowing red to come through. Similarly,
green pigment blocks red and blue, allowing green to come through. When you mix
pigments, you average the absorptive properties of the two. So red + green
pigments completely block the blue spectrum and allow about half of the red and
green to come through. If we were to express that in hex it would look like
808000, which is a dark yellow, which might as well be brown.

### Back to Binary ###

So now it's time to understand the difference between text and binary files. A
text file uses only the 7 bits defined by ASCII (American Standard Code for
Information Interchange). That is, each byte is confined to the range from 0 to
127. In binary that's "0b00000000" to "0b01111111". In hex, that's "0x00" to
"0x7F". All of the numbers equal to or greater than than "0b10000000" or "0x80"
or 128 are outside the ACSII space. Any file using values outside of ASCII is
binary.

In a plain text file, every symbol (e.g letter or punctuation) has a
corresponding value in the range of 0-127. For example, capital "A" is
"0b01000001" or "0x41" or 65 (decimal). Similarly, capital "B" is "0b01000010"
or "0x42" or 66. As you can see in the chart below, the letters and numbers are
organized neatly if you consider the Hex numbers rather than the decimal
numbers. In the table below, you can't see 32 or 127 because 32 is space and
127 is delete. Everything below 32 is an invisible control character of some
kind.

```
| Dec | Hex | C | Dec | Hex | C | Dec | Hex | C |
|:---:|:---:|:-:|:---:|:---:|:-:|:---:|:---:|:-:|
|  32 |  20 |   |  64 |  40 | @ |  96 |  60 | ` |
|  33 |  21 | ! |  65 |  41 | A |  97 |  61 | a |
|  34 |  22 | " |  66 |  42 | B |  98 |  62 | b |
|  35 |  23 | # |  67 |  43 | C |  99 |  63 | c |
|  36 |  24 | $ |  68 |  44 | D | 100 |  64 | d |
|  37 |  25 | % |  69 |  45 | E | 101 |  65 | e |
|  38 |  26 | & |  70 |  46 | F | 102 |  66 | f |
|  39 |  27 | ' |  71 |  47 | G | 103 |  67 | g |
|  40 |  28 | ( |  72 |  48 | H | 104 |  68 | h |
|  41 |  29 | ) |  73 |  49 | I | 105 |  69 | i |
|  42 |  2a | * |  74 |  4a | J | 106 |  6a | j |
|  43 |  2b | + |  75 |  4b | K | 107 |  6b | k |
|  44 |  2c | , |  76 |  4c | L | 108 |  6c | l |
|  45 |  2d | - |  77 |  4d | M | 109 |  6d | m |
|  46 |  2e | . |  78 |  4e | N | 110 |  6e | n |
|  47 |  2f | / |  79 |  4f | O | 111 |  6f | o |
|  48 |  30 | 0 |  80 |  50 | P | 112 |  70 | p |
|  49 |  31 | 1 |  81 |  51 | Q | 113 |  71 | q |
|  50 |  32 | 2 |  82 |  52 | R | 114 |  72 | r |
|  51 |  33 | 3 |  83 |  53 | S | 115 |  73 | s |
|  52 |  34 | 4 |  84 |  54 | T | 116 |  74 | t |
|  53 |  35 | 5 |  85 |  55 | U | 117 |  75 | u |
|  54 |  36 | 6 |  86 |  56 | V | 118 |  76 | v |
|  55 |  37 | 7 |  87 |  57 | W | 119 |  77 | w |
|  56 |  38 | 8 |  88 |  58 | X | 120 |  78 | x |
|  57 |  39 | 9 |  89 |  59 | Y | 121 |  79 | y |
|  58 |  3a | : |  90 |  5a | Z | 122 |  7a | z |
|  59 |  3b | ; |  91 |  5b | [ | 123 |  7b | { |
|  60 |  3c | < |  92 |  5c | \ | 124 |  7c | | |
|  61 |  3d | = |  93 |  5d | ] | 125 |  7d | } |
|  62 |  3e | > |  94 |  5e | ^ | 126 |  7e | ~ |
|  63 |  3f | ? |  95 |  5f | _ | 127 |  7f |   |
```

At this point you may be wondering about other alphabets and how they get
encoded in a computer. Surely you can't fit all of the symbols in known human
language into the range of 0-127. You can't. However, there are multi-byte
encodings that offer many more symbols. But for now, we are only considering
ASCII.

### Formatting Plain Text ###

Text files are incredibly simple. There are no choices of ruler settings, font
family, font style, lists, or tables you expect to find in a word processing
document. However, sometimes you want part of a text file to look like a
heading, or boldface, or a list. There are lots of ways you can imagine doing
that from the use of capital letters to punctuation. Markdown is a global
standard for formatting text files. If you follow the standard, you can turn
your plain text documents into beautifully formatted HTML or PDF that has
actual headings, hyperlinks, font styles, lists, etc.

To find out how to write Markdown, check out the website linked below. This is
the official home of vanilla Markdown. There are a few customizations of
Markdown that add a few more things like tables.

[Markdown](https://daringfireball.net/projects/markdown)

Another way to learn Markdown is to compare an HTML or PDF file to its original
Markdown plain text source document. If you're viewing this document on GitHub,
you're viewing it formatted as HTML. You can also look at the raw text either
on the website or in your forked repo.

Here are the basics of Markdown:

# Level 1 Heading - use a single leading hash

## Level 2 Heading - use a double leading hash

### Level 3 Heading - use a triple leading hash

Alternatively, you can underline titles with equals sign or minus sign for
headings. These look better when viewed as text files.

Level 1 Heading
===============

Level 2 Heading
---------------


Bulletted lists can use plus, minus, or star (and even mix them).

+ Enroll in MCB185
+ Install Linux
+ Get a GitHub account
+ Learn about Markdown
- Learn some Unix commands
- Learn some Python
* Do cool stuff

Formatting text can be _emphasized_ with underline or *stars* or made bold-face
with **double-stars**. For in-line fixed-width font, such as to indicate code
or stuff you're supposed type in a terminal, use `backticks`. For longer code
use triple backticks.

```
your code here
```

Hyperlinks use square brackets for the text followed by parentheses for the
URL. You can also put links in as plain text and make your users copy-paste
them into their browser.

[Markdown](https://daringfireball.net/projects/markdown)

------------------------------------------------------------------------------

## Python: Hello World ##

It's time to write your first Python program (for this course anyway). Change
directory to your homework repo and create a file with the `touch` command.

```
cd ~/Code/homework
touch 00helloworld.py
```

Open your editor, find this file using the GUI, and write the following
one-liner.

```
print('hello world')
```

Save the file. Now run the program.

```
python3 00helloworld.py
```

If all goes well, you should see your welcome message in the terminal. If you
don't, stop now and get help. Don't continue on thinking you'll fix this later.

Now let's add your program to your homework repo. `git status` will show that
this is currently not tracked. So let's `add` it, create a `commit` message,
and then `push` it back to the website. Remember, you don't use your website
password here, but rather you github personal access token (PAT). You'll have
to copy-paste that, as it's a bit too long to type.

If you get an error, it may be because the copy-paste didn't work. Do a
right-click-based paste rather than using the keyboard.

```
git add 00helloworld.py
git commit -m new
git push
```

Check the GitHub website. Your `00helloworld.py` file should now be in the
repo. If it is not, refresh the page or get help if that's not the problem.

It might seem like git is a lot of effort just to upload your code to a website.
If that's all git did, it would be too much effort, but git allows you to do a
lot more. Git tracks every change you make to a file, allowing you to rewind it
to any point in time. Git allows you to make a _branch_ of related work and
then later merge it back in with the main trunk if desired. More importantly,
git allows multiple developers to work simultaneously on the same project
without destroying each others work. We aren't using those advanced features
yet. Right now, our focus is on backing up our code and logging our programming
activity to the GitHub website.

## Homework ##

To get full credit for your homework, submit the following:

+ URL of your homework repository
+ 00helloworld.py in your repo
