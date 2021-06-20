ProdL: Productive Deep Learner (WIP)
===

Copyright (C) 2020-2021, Mo Zhou `<cdluminate AT gmail.com>`

This document is released under the [GNU Free Documentation License (GFDL-1.3)
](https://www.gnu.org/licenses/fdl-1.3.html) license.

*ProdL* is a personal documentation project for collecting memos and hints
that may help one boost their productivity in Deep Learning study.
This project covers a wide range of topics, including but not limited to
computer programming, computer organization, operating system, software
engineering and practice, deep learning, scientific computing,
high performance programming, program debugging, paper reading / reviewing,
paper composing, rebuttal process, latex techniques, artistic design
for diagrams, and integrated development environment.

The author will try to deliver the content in a concise manner, and will
prefer to reference many external materials to reduce duplicated work.
Since the author is more or less an old-school UNIX/Linux proponent,
this document will not introduce any Windows-specific or MacOS-specific
information, and everything will be written may sense a strong odor of UNIX
in this document. As a convention in the UNIX/Linux world,
a notation composed by a word and a parenthesized number
denotes reference to a manual page. For instance, `signal(7)` means the
topic "signal" in manual page section 7. Type `man 7 signal` in a linux shell
to read the document.

**Table of Contents**

```md
## 0. Prerequisites
### 0.1. Critical Instinct
### 0.2. Programming Languages
### 0.3. Domain Specific Languages
### 0.4. Computer Organization, Compiler, etc.
### 0.5. Operating System and POSIX
### 0.7. Remote Access
### 0.8. Software Engineering
### 0.9. Git Workflow
## 1. Correctly Understanding Deep Learning Framework
### 1.1. Automatic Differentiation
### 1.2. Computation Graph
### 1.3. Deep Learning Framework Design
## 2. A Bit of Scientific Computation Background
### 2.1. Dense Numerical Linear Algebra
### 2.2. Linear Algebra Acceleration
## 3. High Performance Programming
### 3.1. Profiling
### 3.2. Server Architecture
### 3.3. IO and Storage System
### 3.4. High Performance Python (pure Python)
### 3.5. Extending Python with Compiled Language
## 4. Program Diagnosis and Debugging
### 4.1. Program Tracing
### 4.2. Program Debugging
## 5. Scheduling Interactive Experiments
### 5.1. Interactive Experiments
### 5.2. Computational Debugging
## 6. Paper Reading and Reviewing
## 7. Organizing Preliminary Draft
### 7.1. LaTeX Typesetting
### 7.2. Drafting a Conference Paper
### 7.3. Drafting a Journal Paper
### 7.4. Polishing
### 7.5. Conference Rebuttal
### 7.6. Journal Response
### 7.7. Slides and Poster
## 8. A Tiny Bit on Art
## Misc References
## A. Python Libraries
## B. Editors and IDEs
## C. Physical Server Management
```

## 0. Prerequisites

In this section, I shall point out some keywords for background knowledge
that would greatly help you throughout the journey on deep learning.
Some audience may found these contents useless for graduation or some
research works, but boosting one's productivity means they can enter
a higher level in a much faster pace.

### 0.1. Critical Instinct

Things may get much easier with the following instincts.

* Be aware of what you are doing, and what you intend to do.

* Carefully read and try to understand the output of programs.

* [Ask questions in a smart way.](http://www.catb.org/~esr/faqs/smart-questions.html)

* Be sensitive to the definitions of terms and mathematical things.

### 0.2. Programming Languages

For deep learning, I personally think some background knowledge on ANSI C,
C++ will be beneficial (in various aspects). Of course, one has to be proficient
in Python as well.

* ANSI C. It provides fundamental knowledge for programming in many other languages.
Reference book: [K&R C](https://en.wikipedia.org/wiki/The_C_Programming_Language)

* C++. The core parts of PyTorch, Tensorflow, as well as many other dependency
libraries such as OpenCV are written in C++. It is suitable for some
performance-critical tasks.

* Python. An interpreted "glue" language. The standard Python interpreter is
called `cpython`, which suffers from poor performance (compared to compiled
languages), and GIL for multi-thread programming.

I recommend the [Python Official Tutorial](https://docs.python.org/3/tutorial/index.html)
as the core reference if you are new to Python. Note, please stay away from
the ancient Python2 in case you intend to learn Python from other resources.

It is also recommended to correctly understand the difference between
compiled languages and interpreted languages. Generally speaking, interpreted
languages are friendly to human efficiency, while compiled languages are
friendly to machine efficiency.

### 0.3. Domain Specific Languages

#### 0.3.1. Markup Languages for Documentation

`Markdown` is a very useful markup language when you are going to write
documentation for your software project. Yet, its usage is not limited
to documenting. Given a correct tool such as `pandoc`, you can even write
slides and article draft, etc.

`RestructuredText` is a markup language that is very useful for documenting
Python projects. Likewise, you can write slides or articles with it given
a correct conversion tool such as `pandoc`.

`Pandoc` accepts many types of input format (incl. markdown, restructuredtext, etc),
and can convert them into latex, docx, etc.

References:
- [Github Markdown Tutorial](https://guides.github.com/features/mastering-markdown/)
- [Pandoc](https://github.com/jgm/pandoc)

#### 0.3.2. GNU Make for Automation of Simple Tasks

[GNU Make](https://www.gnu.org/software/make/) is mostly used for compiling
software projects written in C, C++, etc. That said, it is also suitable
for automating simple (or complicated) task pipelines in non-software projects.
For example, compiling documentations, or executing experiment pipelines.

For example, I usually keep such a `Makefile` in my CVPR draft directory:

```make
main: cvpr

cvpr: fig1.pdf
	pdflatex cvpr
	bibtex cvpr
	pdflatex cvpr
	pdflatex cvpr
	-evince cvpr.pdf
	$(MAKE) clean

clean:
	-$(RM) *.aux *.bbl *.blg *.brf *.log *.out

fig1.pdf:
	inkscape -o fig1.pdf fig1.svg
```

### 0.4. Computer Organization, Compiler, etc.

Computer organization [[1]](https://www.coursera.org/learn/jisuanji-zucheng)
[[2]](https://www.geeksforgeeks.org/computer-organization-and-architecture-tutorials/)
[[3]](https://csapp.cs.cmu.edu/)
is critical for you to correctly understand things that harms the performance
of your program. It is also (partly) helpful for you to avoid writing prototype
code without obvious performance flaw.

Such background knowledge is critical for you to understand the performance
of dense numerical linear algebra.

In order to gain an in-depth image on computer programming (whatever in
interpreted language or compiled language), it is suggested to be aware
of how compilers work.

TODO: GPU is not always faster than CPU -- `cudaMemcpy` is not something trivial.

### 0.5. Operating System and POSIX

[POSIX](https://en.wikipedia.org/wiki/POSIX) is a standard for UNIX operating
system, which defines some invariance between different Unix and other 
operating systems such as linux. Specifically, it covers system API,
shell and a set of core utilities.

Some important tools and programming interfaces under linux follow POSIX.

#### 0.5.1. POSIX Shell Scripting

The commonly seen shells include `bash` and `zsh`. Both of them are POSIX
compliant shells, and provides extended functionalities beyond what POSIX
defined.

- [POSIX shell Tutorial](https://www.grymoire.com/Unix/Sh.html)
- [Bash Documentation](https://www.gnu.org/software/bash/)

`zsh` can be easily configured with third-party configuration provides such
as [Oh-My-ZSH](https://ohmyz.sh/) to provide a rich set of features.
There are also some shells not compliant to POSIX for their own considerations,
such as `fish` (oriented for better user interaction). `fish` can work out-of-box
with a rich set of features without manually overriding any configuration.

For most linux distributions, POSIX shell is recommended if you are scripting
for the system.

#### 0.5.2. Core Utilities

A non-exhaustive set of core utilities. Here I'll only list their names and main usage.

Category 1: File and permission

```bash
ls         list files and directories
stat       show file info incl. permission
touch      create empty file
rm         remove file
rmdir      remove directory
mv         move file or directory
cp         copy file or directory
ln         symlink and hardlink
cat        show file content
head       show first several lines of a file
tail       show last several lines of a file
less       inspect a file in pager
sync       flush kernel IO buffers to disk
file       tell the type of a file according to its magic
tar        tarball creation or extraction
gzip       compression, decompression
xz         compression, decompression
md5sum     calculate hashsum
chmod      change mode of a file
chown      change owner of a file
chgrp      change group of a file
```

Category 2: Shell, processes, system resources

```bash
bash       the bash shell
ps         process information (e.g. ps aux; ps ux)
kill       send a signal to some processes
top        system monitor
nohup      block SIGHUP for the child process
iostat     show system io statistics
```

Category 3: File manipulation

```
sed        stream editor, useful in scripts
awk        awk programming language
sort       sort text lines
uniq       deduplicate text lines
wc         character, word, line count
find       file finder
grep       file content searcher
```

Category 4: Network

```
wget       download from a given URI
ssh        ssh client
```

For detailed tutorials see [[1]](http://linux.vbird.org)
or [Missing semester of Your CS Education](https://missing.csail.mit.edu/).

Besides, it is important to introduce some modern alternatives to the above
core utilities:

Category X: Modern Alternatives
```
rg         ripgrep, a much faster "grep"
htop       TUI-based system monitor
glances    TUI-based system monitor
dstat      system monitor
rsync      copy files between hosts
```

### 0.7. Remote Access and File Transferring

#### 0.7.1. OpenSSH (SSH) -- Remote Login Client

For what it's worth, I think OpenSSH is the most robust and resilient remote access solution.
Please refer to the public materials for its basic usage. I shall point out some
keys about it:

1. **Automatic authorization using RSA key.** The simplest way for authentication
is username + password, of course. However, it is widely known that many users
tend to adopt very weak passwords lest they forget them. As a result, linux
servers exposed to the public internet may be vulnerable to brute force SSH
attack which enumerates commonly seen usernames and weak passwords from a
pre-defined dictionary. Weak passwords can be easily compromised.
However, I'd like to point out that SSH supports RSA-key authentication, which
ensures a much stronger security level. To use such authentication method, you
need to (1) generate a pair of RSA keys (private key and public key) using `ssh-keygen`;
(2) Put yor public key as the `~/.ssh/authorized_keys` file on your server;
(3) Configure your local SSH client, setting RSA key as the default authentication method.

2. **Don't want to type the password again and again?** When we work on a linux server,
we may need to start new ssh sessions regularly, and enter the password again and again.
In fact, there is a daemon program named `ssh-agent` which can remember the password for
your RSA private key. It helps you skip entering the password anytime when you need to
authorize (e.g., ssh, scp, rsync, etc) until timeout or process termination.
If your desktop environment does not automatically launch the
daemon for you, you may need to do it manually somehow.

3. **Network Interruption:** SSH session may accidentally terminate under poor
network condition. To prevent the ensuing and undesired remote process termination,
we can (1) use `nohup(1)` to block `SIGHUP` (see `signal(7)`) for a child process;
(2) use `mosh` to auto-reconnect (will be discussed later) ;
(3) use `tmux` to manage working processes under a tmux session (will be discussed later).

OpenSSH is usually a part of standard linux server installation, so we expect
it to be available in most cases. In some special cases, such as remote login
of embedded devices, the server side may be running Dropbear, which is another
SSH implementation that implements the protocol-level compatibility.

### 0.7.2. Mosh -- Remote Terminal App that Supports Intermittent Connectivity

Working through SSH under a problematic network condition is definitely
frustrating. We can use `mosh` to avoid reconnecting the server again and
again, as `mosh` is able to automatically reconnect to the server when
the network is accessible again. Mosh relies on OpenSSH.

Mosh is not a default part of linux server installation. The user may have
to install the client and the server software on proper machines.

### 0.7.3. Graphical solutions such as VNC and RDP

These solutions are fancy and, of course, have a much smoother and less steep
learning curve. I think these solutions are generally less robust than text-based
SSH solution, because (1) they have many vulnerabilities (CVEs); (2) they requires
much higher network bandwidth to function properly compared to SSH; (3) they
are not scalable to a computer cluster or multiple remote servers.
My suggestion is: use these on your preference, if it does not prevent
you from improving productivity.

### 0.7.4. Ansible

### 0.7.5. Rsync -- Copying files across hosts

### 0.7.6. SSHFS -- Mounting remote directory through SSH+FUSE

### 0.8. Software Engineering

Functional programming.

Reference book: 

### 0.9. Git Workflow

Extremely important for production sanity, safety, and reliability.

## 1. Correctly Understanding Deep Learning Framework

### 1.1. Automatic Differentiation

### 1.2. Computation Graph

### 1.3. Deep Learning Framework Design

## 2. A Bit of Scientific Computation Background

### 2.1. Dense Numerical Linear Algebra

### 2.2. Linear Algebra Acceleration

## 3. High Performance Programming

### 3.1. Profiling

### 3.2. Server Architecture

### 3.3. IO and Storage System

### 3.4. High Performance Python (pure Python)

### 3.5. Extending Python with Compiled Language

## 4. Program Diagnosis and Debugging

### 4.1. Program Tracing

### 4.2. Program Debugging

## 5. Scheduling Interactive Experiments

### 5.1. Interactive Experiments

### 5.2. Computational Debugging

## 6. Paper Reading and Reviewing

## 7. Organizing Preliminary Draft

### 7.1. LaTeX Typesetting

Advanced Techniques:

1. https://github.com/simonharrer/latex-best-practices

### 7.2. Drafting a Conference Paper

### 7.3. Drafting a Journal Paper

### 7.4. Polishing

### 7.5. Conference Rebuttal

1. Carefully read the official rebuttal instructions, e.g., the [ICCV2021 rebuttal instructions](http://iccv2021.thecvf.com/node/4#rebuttal-instructions), and fetch the template.

### 7.6. Journal Response

### 7.7. Slides and Poster

## 8. A Tiny Bit on Art

Reference material: [how to draw ugly diagrams?](assets/ugly-diagram.pdf) [(svg source)](assets/ugly-diagram.svg)

Color, Shapes, Lines, Layout, Fonts

## Misc References

[1] A collection of guides to successful scientific communication: https://mitcommlab.mit.edu/eecs/use-the-commkit/

## A. Python Libraries

Some very useful python libraries.

## B. Editors and IDEs

## C. Physical Server Management

### C.1. IPMI
