---
title: "ProdL: Productive Deep Learner"
author: Mo Zhou `<cdluminate@gmail.com>`
date: June 2021, GFDL-1.3 License
---

ProdL: Productive Deep Learner (WIP)
===

Copyright (C) 2018-2021, Mo Zhou `<cdluminate@gmail.com>`

This document is released under the [GNU Free Documentation License (GFDL-1.3)
](https://www.gnu.org/licenses/fdl-1.3.html) license.
[Click here to obtain the latest version of this document.](https://github.com/cdluminate/ProdL)

Document Version: WIP.

*ProdL* is a personal documentation project for collecting memos and hints that
may help one boost their productivity in Deep Learning study.  This project
covers a wide range of topics, including but not limited to computer
programming, computer organization, operating system, software engineering and
practice, deep learning, scientific computing, high performance programming,
program debugging, paper reading / reviewing, paper composing, rebuttal
process, latex techniques, artistic design for diagrams, and integrated
development environment.

The author will try to deliver the content in a concise manner, and will prefer
to reference many external materials to reduce duplicated work.  Since the
author is more or less an old-school UNIX/Linux proponent, this document will
not introduce any Windows-specific or MacOS-specific information, and
everything will be written may sense a strong odor of UNIX in this document.

As a convention in the UNIX/Linux world, a notation composed by a word and a
parenthesized number denotes reference to a manual page. For instance,
`signal(7)` means the topic "signal" in manual page section 7. Type `man 7
signal` in a linux shell to read the document. If you find the manual for a
specific command too lengthy to read, you may also consult the
[`tldr`](https://github.com/tldr-pages/tldr) pages.

When talking about commands, `<keyword>` denotes a placeholder that should be
replaced by a sensible value according to the context, instead of being copied
from my examples literally.

When talking about keybindings, `Mod` means the modifier key for a specifically
discussed program. For example, the `Mod` key for `tmux` is `Ctrl+b` by
default.  Any keybinding discussed in this document is case-sensitive. Any text
rendered in mono-spaced font are case-sensitive.

Should you find any error or discrepancy in the content, the author is willing
to correct the content. Please file a bug through the [Github issues
channel](https://github.com/cdluminate/ProdL/issues).

Table-of-Contents is only available in the PDF version of this document.

## 0. Miscellaneous Prerequisites

In this section, I shall point out some keywords for background knowledge that
would greatly help you throughout the journey on deep learning.  Some audience
may found these contents useless for graduation or some research works, but
boosting one's productivity means they can enter a higher level in a much
faster pace.

### 0.1. Critical Instinct

Things may get much easier with the following instincts.

* **Be aware of what you are doing, and what you intend to do.**

* **Carefully read and try to understand the output of programs.**

* [**Ask questions in a smart way.**](http://www.catb.org/~esr/faqs/smart-questions.html)

* **Be sensitive to the definitions of terms and mathematical things.**

That this subsection does not contain bulky texts does not mean it's not
important. Let me omit explanations and negative examples regarding the above
points.

### 0.2. Programming Languages

[Wikipedia: programming language](https://en.wikipedia.org/wiki/Programming_language)

For deep learning, I personally think some background knowledge on ANSI C, C++
will be beneficial (in various aspects). Of course, one has to be proficient in
Python as well.

* ANSI C. It provides fundamental knowledge for programming in many other languages.
Reference book: [K&R C](https://en.wikipedia.org/wiki/The_C_Programming_Language)

* C++. The core parts of PyTorch, Tensorflow, as well as many other dependency
libraries such as OpenCV are written in C++. It is suitable for some
performance-critical tasks.

* Python. An interpreted "glue" language. The standard Python interpreter
implementation is called `cpython`, which suffers from poor performance
(compared to compiled languages), and GIL for multi-thread programming.  Other
python implementations such as [Pypy](https://www.pypy.org/) and RustPython
exist, but, for instance, [Pypy's support for numpy is still not mature
enough](https://doc.pypy.org/en/latest/faq.html?highlight=numpy#what-about-numpy-numpypy-micronumpy).

I recommend the [Python Official
Tutorial](https://docs.python.org/3/tutorial/index.html) as the core reference
if you are new to Python. Note, please stay away from the ancient Python2 in
case you intend to learn Python from other resources.

It is also recommended to correctly understand the difference between compiled
languages and interpreted languages. Generally speaking, interpreted languages
are friendly to human efficiency, while compiled languages are friendly to
machine efficiency.

Python, in terms of language design, is still not perfect. It still lacks some
features in modern languages. To some extent, it is good to know the existence
of some other existing languages and there highlights.

* [Julia](https://julialang.org/) is a modern language for scientfic computing.
It is a compiled language that provides a feeling of interpreted language. It
is designed for high performance via LLVM's JIT compilation. It supports many
good language features that does not ever exist in python. Julia suffers from
some issues such as significant JIT compilation time consumption for the
first-time-plot. By the way, Julia uses column-major indexing for internal
arrays following Fortran instead of C.

* [Rust programming language](https://www.rust-lang.org/) is a modern compiled
language that aims for performance and reliability. It helps the programmer
eliminate the need to run valgrind from time to time when debugging memory
issues for a C++ program. Rust has a relatively steep learning curve.

* [Awk](https://www.gnu.org/software/gawk/manual/gawk.html) is a small language
that works like magic especially when you are processing line-based texts in
a shell. Most proficient linux users should be aware of its fundamental usage.

Refer to the [TIOBE list](https://www.tiobe.com/tiobe-index/) for more
reference on programming languages.

### 0.3. Domain Specific Languages

[Wikipedia: domain-specific language](https://en.wikipedia.org/wiki/Domain-specific_language)

Domain-specific languages are not necessarily turing-incomplete.

#### 0.3.1. Markup Languages for Documentation

`Markdown` is a very useful markup language when you are going to write
documentation for your software project. Yet, its usage is not limited to
documenting. Given a correct tool such as `pandoc`, you can even write slides
and article draft, etc.

`RestructuredText` is a markup language that is very useful for documenting
Python projects. Likewise, you can write slides or articles with it given a
correct conversion tool such as `pandoc`.

`Pandoc` accepts many types of input format (incl. markdown, restructured-text,
etc), and can convert them into latex, docx, etc.

For example, this document you are currently reading is written in Markdown.
Its online version is rendered into HTML by Github. Its PDF version is
converted from Markdown source by Pandoc.

Writting source code without documentation is one of the best ways to prevent
yourself from understanding your own code written in the last week. *Although
writing splendid code with clear documentation may also mean your job can be
easier taken away by collegues or newcomers in some business context, at least
there should be some documentation for personal research projects.*

References:

- [Github Markdown Tutorial](https://guides.github.com/features/mastering-markdown/)  
- [Pandoc](https://github.com/jgm/pandoc)  
- [Learn X in Y minutes: RST](https://learnxinyminutes.com/docs/rst/)  

#### 0.3.2. GNU Make for Automation of Simple Tasks

[GNU Make](https://www.gnu.org/software/make/) is mostly used for compiling
software projects written in C, C++, etc. That said, it is also suitable for
automating simple (or complicated) task pipelines in non-software projects.
For example, compiling documentations, or executing experiment pipelines.

For example, I usually keep such a `Makefile` in my CVPR draft directory:

```makefile
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

In the above Makefile, the main (default) target is `cvpr` PDF compilation.
The target `cvpr` depends on target (file) `fig1.pdf`. Since target `fig1.pdf`
is not PHONY, `make` will convert the SVG into PDF first using `inkscape` if
the corresponding PDF file does not exist, or skip the PDF conversion if it
already exists.  The `evince` is the PDF viewer for Gnome3 desktop environment.
The leading dash sign `-` to `evince` means that the target may continue even
if the `evince` command failed. After compilation of the `cvpr.pdf`, temporary
files are automatically cleaned.

And I also use Makefile to process miscellaneous works in code repositories.
For example, here is the [Makefile for
my RobBank project](https://github.com/cdluminate/robrank/blob/main/Makefile).

### 0.4. Computer Organization, Compiler, etc.

Computer organization [[1]](https://www.coursera.org/learn/jisuanji-zucheng)
[[2]](https://www.geeksforgeeks.org/computer-organization-and-architecture-tutorials/)
[[3]](https://csapp.cs.cmu.edu/) is critical for you to correctly understand
things that harms the performance of your program. It is also (partly) helpful
for you to avoid writing prototype code without obvious performance flaw.
Besides, such background knowledge is critical for you to understand the
performance of dense numerical linear algebra.

In order to gain an in-depth image on computer programming (whatever in
interpreted language or compiled language), it is suggested to be aware of [how
compilers
work](https://en.wikipedia.org/wiki/Compilers:_Principles,_Techniques,_and_Tools).
For example, the key concepts for a compiler involves lexical analysis, syntax
analysis, intermediate representation, code optimization and target code
generation.

Some extra background knowledge on programming paradigms is helpful.
For example, [**Functional programming**](https://en.wikipedia.org/wiki/Functional_programming)
introduces concepts such as "pure functions" (free of side effects).
Try to follow some of these paradigms may help you write more robust code.

### 0.5. POSIX Operating System and Shell Script

[POSIX](https://en.wikipedia.org/wiki/POSIX) is a standard for UNIX operating
system, which defines some invariance between different Unix and other
operating systems such as linux. Specifically, it covers system API, shell and
a set of core utilities.

Some important tools and programming interfaces under linux follow POSIX.

#### 0.5.1. POSIX Shell Scripting

The commonly seen shells include `bash` and `zsh`. Both of them are POSIX
compliant shells, and provides extended functionalities beyond what POSIX
defined.

- [POSIX shell Tutorial](https://www.grymoire.com/Unix/Sh.html)
- [Bash Documentation](https://www.gnu.org/software/bash/)

`zsh` can be easily configured with third-party configuration provides such as
[Oh-My-ZSH](https://ohmyz.sh/) to provide a rich set of features.  There are
also some shells not compliant to POSIX for their own considerations, such as
`fish` (oriented for better user interaction). `fish` can work out-of-box with
a rich set of features without manually overriding any configuration.

Both `zsh` and `fish` can support syntax highlighting, automatic suggestion,
and smarter command line completion. I think these features are beneficial for
productivity.

For most linux distributions, POSIX shell is recommended if you are scripting
for the system.

#### 0.5.2. Frequently Used Utilities

A non-exhaustive set of core utilities. Here I'll only list their names and
main usage.  Most of these utilities are extremely important, and are extremely
valuable to learn.

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

For detailed tutorials see [[1]](http://linux.vbird.org) or [Missing semester
of Your CS Education](https://missing.csail.mit.edu/).

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

There are [more modern alternative to traditional unix
utilities](https://github.com/ibraheemdev/modern-unix). But take heed, although
we may love fancy (sometimes faster) tools, a fact is that the availability of
the traditional tools is still higher than these fancy alternatives.

### 0.6. UNIX Magics

This part will discuss some important UNIX tools that works like a charm.  They
are also frequently used in shell scripting. I like them.

#### 0.6.1. Awk for Quick Text Processing

Let's start with an example.

Assume that we have the following text output from a program:
```
some noise ...
Batch[0] accuracy 0.2542995026760726
some noise ...
Batch[1] accuracy 0.009208118471664362
Batch[2] accuracy 0.7542131873404234
some noise ...
Batch[3] accuracy 0.37011115810462947
some noise ...
Batch[4] accuracy 0.09099862645817958
Batch[5] accuracy 0.5073895063975833
some noise ...
Batch[6] accuracy 0.5207971298596508
Batch[7] accuracy 0.19669099449350658
some noise ...
Batch[8] accuracy 0.6605649333264325
some noise ...
Batch[9] accuracy 0.12726328140498144
```
which is actually produced by a toy program
```python
import random
for i in range(10):
    if random.random() > 0.5:
        print('some noise ...')
    print(f'Batch[{i}] accuracy {random.random()}')
```
What should we do if we want to calculate the averaged accuracy across batches?

We may want to write another python script, including lines like this
```python
for line in [x.split(' ') for x in lines]:
	if does_not_contain_accuracy():
		continue
	accuracy += float(line[-1])
	n += 1
accuracy /= n
```
But actually this can be done with a one-liner:
```shell
$ python3 foobar.py | awk '/Batch/{a+=$3;n+=1}END{print a/n}'
0.604364
```

The `/Batch/{a+=$3;n+=1}END{print a/n}` is a complete Awk program.  Awk can be
understood as a text-line-oriented state machine. Before scanning text lines,
it execute code in the `BEGIN{}` block, which is omitted in this case. The
`/Batch/` is for regex matching, which means only lines that match the regex
`Batch` will be processed by the following code block `{a+=$3;n+=1}`. After
scanning all lines, Awk executes code in the `END{}` block. Awk variables
can be initialized implicitly. In brief, such awk one-liner is much more
efficient than python code, especially if the python code will not be reused
in foreseeable future.

If you don't want to use awk, there are still other magics:
```shell
$ python3 foobar.py | grep Batch | cut -d' ' -f3
0.2529907447588151
0.24730314298222944
0.4739566597503019
0.40976192552727086
0.22660965559362434
0.48954082611477445
0.9067330192751845
0.2698054854245503
0.13595466616301244
0.8901862421743295
$ python3 foobar.py | grep Batch | cut -d' ' -f3 > array.txt
```
I shall not expand on the piped command as this part is for awk.
Anyway, `numpy` is able to directly load the resulting `array.txt`.

Dirty hacks are also possible. In some terminals (e.g., gnome-terminal), you
can select several column of text by pressing Ctrl and the left mouse button.
Copying the columns containing accuracy values and pasting the text to octave
or julia is feasible for the average value calculation. If gnome-terminal is
not available, vim can also select multiple columns of text (`Ctrl^v`).

Refer to the [GNU Awk Manual](https://www.gnu.org/software/gawk/manual/gawk.html)
if you are interested in this language.

#### 0.6.2. Find and Grep

#### 0.6.3. Some other command pipeline examples

### 0.7. Remote Access and File Transferring

In this section, we mainly discuss some tools for accessing remote hosts
(servers), as well as transferring files across different machines.
  
#### 0.7.1. OpenSSH -- Remote Login Client
  
For what it's worth, I think OpenSSH is the most robust and resilient remote
access solution.  Please refer to the public materials for its basic usage. I
shall point out some keys about it:

1. **Automatic authorization using RSA key.** The simplest way for
authentication is username + password, of course. However, it is widely
known that many users tend to adopt very weak passwords lest they forget them.
As a result, linux servers exposed to the public internet may be vulnerable to
brute force SSH attack which enumerates commonly seen usernames and weak
passwords from a pre-defined dictionary. Weak passwords can be easily
compromised.  However, I'd like to point out that SSH supports RSA-key
authentication, which ensures a much stronger security level. To use such
authentication method, you need to (1) generate a pair of RSA keys (private key
and public key) using `ssh-keygen`; (2) Put yor public key as the
`~/.ssh/authorized_keys` file on your server; (3) Configure your local SSH
client, setting RSA key as the default authentication method.

2. **Don't want to type the password again and again?** When we work on a linux
   server, we may need to start new ssh sessions regularly, and enter the
password again and again.  In fact, there is a daemon program named `ssh-agent`
which can remember the password for your RSA private key. It helps you skip
entering the password anytime when you need to authorize (e.g., ssh, scp,
rsync, etc) until timeout or process termination.  If your desktop environment
does not automatically launch the daemon for you, you may need to do it
manually somehow.

3. **Network Interruption:** SSH session may accidentally terminate under poor
   network condition. To prevent the ensuing and undesired remote process
termination, we can (1) use `nohup(1)` to block `SIGHUP` (see `signal(7)`) for
a child process; (2) use `mosh` to auto-reconnect (will be discussed later);
and (3) use `tmux` to manage working processes under a tmux session (will be
discussed later).

OpenSSH is usually a part of standard linux server installation, so we expect
it to be available in most cases. In some special cases, such as remote login
of embedded devices, the server side may be running Dropbear, which is another
SSH implementation that implements the protocol-level compatibility.

#### 0.7.2. Mosh -- Supporting Intermittent Connectivity

Working through SSH under a problematic network condition is definitely
frustrating. We can use `mosh` to avoid reconnecting the server again and
again, as `mosh` is able to automatically reconnect to the server when the
network is accessible again. Mosh relies on OpenSSH.

Mosh is not a default part of linux server installation. The user may have to
install the client and the server software on proper machines.

#### 0.7.3. Tmux -- Terminal Multiplexer

Technically speaking tmux has no business with remote access, but tmux is
usually used in conjunction with ssh (or mosh). Simply type `tmux` to start a
tmux session.  With such a terminal multiplexer, you can start a new shell in
the tmux session without a new SSH connection (Key: `Mod+c`).  New processes
started in a tmux session will be put into different tmux windows. You can
re-organize these windows flexibly. For example, you can split the window
vertically (Key: `Mod+"`) or horizontally (Key: `Mod+%`) into two panes.  The
`Mod` key by default is `Ctrl+b`.

1. **Intermittent Connectivity:** Due to tmux's server-client architecture,
accidental SSH connection interruption will not lead to termination of
programs running under the tmux session. You can resume the last tmux session
with `tmux attach`. You can even detach again from the session by `Mod+d`, and
manually end the SSH connection.

2. **Scheduling experiments:** Tmux is so flexible that it is even scriptable.
Leveraging its advantages, we can schedule deep learning experiments with
tmux and automate program execution. [Here is an
example](https://github.com/cdluminate/advrank/blob/master/Code/pipeline/train-mnist.sh)
for running four experiments under a new tmux session on four GPUs
simultaneously.  More complicated scheduling can be implemented in the shell
script.

An commonly used alternative to tmux is [GNU
screen](https://www.gnu.org/software/screen/).  [Byobu](https://www.byobu.org/)
is a high level wrapper on tmux or screen that delivers out-of-box friendly
experience.

#### 0.7.3. Graphical solutions such as VNC and RDP

These solutions are fancy and, of course, have a much smoother and less steep
learning curve. I think these solutions are generally less robust than
text-based SSH solution, because (1) they have many vulnerabilities (CVEs); (2)
they requires much higher network bandwidth to function properly compared to
SSH; (3) they are not scalable to a computer cluster or multiple remote
servers.  My suggestion is: use these on your preference, if it does not
prevent you from improving productivity.

#### 0.7.4. Ansible

[Ansible](https://docs.ansible.com/) can be used to manage a computer cluster
(or multiple remote hosts) in a scalable way. With this tool, you can
distribute some local files (directories) to remote machines, gather remote
files (directories) to local machine, or execute commands on remote machines in
parallel. Please refer its documentation for full description of its
functionalities.

1. **Query GPU usage:** We can query the GPU usage of a group of servers in
parallel with ansible, which automates the boring manual check process.
First you may create a `servers.txt` which contains the IP addresses of the
remote hosts (an IP address per line). Make sure that the RSA key is properly
setup for every remote hosts. Then we can quickly check whether these machines
are online: `ansible -i servers.txt all -m ping -o`. Or query the GPU usage
within several seconds: `ansible -i servers.txt all -m shell -a "gpustat"`.

My project [gpu-load-watcher](https://github.com/cdluminate/gpu-load-watcher)
is based on ansible for sqlite3 database collection, as well as remote command
execution, etc.

#### 0.7.5. Rsync -- Copying files across hosts

You may be familiar with `scp`, a standard file transfer tool provided by
OpenSSH. And you may have noticed that `scp` will transfer all file contents
when copying a directory to the remote machine, even if we are overwriting a
remote directory with merely some minor modifications. This could greatly
hamper productivity once the directory to be transferred is huge.

`rsync` is an incremental file transfer tool that does not suffer from such
issue of `scp`. It is able to transfer and only transfer the incremental change
to the remote host, hence vastly improving efficiency especially in cases where
you have to frequently synchronize directories among multiple hosts.

`rsync` is able to transfer files through SSH connection. For example, we can
transfer a local directory to remote side by `rsync -Pav <local-directory>
<user>@<ip-address>:~/my-work`, or transfer a remote directory to the local
machine by `rsync -Pav <user>@<ip-address>:~/my-work <local-directory>`.
Argument `P`, `a`, `v` mean "show progress", "archive mode", and "verbose",
respectively.  When the SSH service is listening on a non-standard port
(instead of tcp/22), pass an extra argument to rsync to use the correct port
number: `rsync -e "ssh -p <port>"`.

A successful file transfer via `rsync` requires it to be installed on both the
machines of client and the server sides.

#### 0.7.6. SSHFS -- Mounting remote directory through SSH+FUSE

`sshfs` allows you to mount a remote directory to a local path through SSH and
FUSE. For example, if you want to mount a remote directory to a local path, in
order to browse the images on the remote host later: `sshfs
<user>@<remote-host>:/<remote-directory> ~/<local-path>`.  In this way you
don't have to copy these images to the local host in order to browse them.
Besides, files under the mount-point can be manipulated with standard file
management tools such as cp, mv, etc as if are are manipulating local files.

#### 0.7.7. NFS

Network File System (NFS) is used for exporting server's local directories for
some specified clients, so that the clients are able to mount the exported
directories locally. It is similar to sshfs, but is much more scalable and
robust for computer clusters.

### 0.8. Software Engineering

For software architecture (design), book [1] is a good reference.

For people who like the `pytest` library, "test-driven development" is
something good to know. 

[1] Eric S. Raymond, The Art of UNIX Programming.

### 0.9. Git Version Control System and Workflow

Extremely important for production sanity, safety, and reliability.  There are
also alternative version control systems, such as svn, hg, etc., but Git is the
most prevalent one of its kind.

I shall skip explaining exactly how important it is or why, but I can
list some pains that will hardly exist with a good git practice.

1. Wrongly edited and broken the code / paper, and wanted to revert the change.  
2. Forgotten the exact work progress of yesterday and felt unhappy.  
3. The code stopped working (or the paper stopped compiling) again, but didn't
know what latest change triggered that problem.  
4. Difficulty in understanding why a line of code exists.  
5. Afraid of unrecoverable loss due to large-scale rewrite or refactor, but still
suffer from the problematic old code architecture.  
6. Hundreds of copies of similar code in the comment lines -- and finally started
to be confused by the different versions of commented code.  
7. Hundreds of working copies of similar code -- the code eventually becomes
messy and nearly unreadable.  
8. Deleted the code or paper by mistake.  
9. The server where my only copy of code and paper is stored is down.  
10. Wanted to elegantly edit the same code with collaborators simultaneously.  
11. Collaborators gave some advices regarding paper draft v3, but the paper
draft is already revised into v4.  
12. Wanted to check a historical version of code / paper.  
13. Wanted to collaborate with others but have no idea on synchronization and workflow.  
14. Identified a bug and wanted to know when the bug was introduced and how many
conclusions were affected, as well as some other implications.  
15. Difficulty in locating a hidden bug introduced in some historical version.  
16. Wanted to implement some bold ideas based on the code, but hesitate to break the
code due to fear of unrecoverable lost.  
17. I copied my code to my 100 remote servers -- each server a copy. I don't know
whether I have modified some of these copies on the servers.  
18. I'm not interested in academics, but I still find Git important for the industry.  

Documentations as well as tutorials can be found following the [official site
of Git](https://git-scm.com/). We are not doing duplicated work to write another
Git tutorials here, but at least we can group the Git subcommands and mention
some keywords. 

* Linear Workflow (simple commands): config, init, clone, add (adding files to
staging area), commit, push, pull, clean (`.gitignore`), diff, show, log,
grep, tag, status. These should be enough for a linear workflow.

* Non-linear workflow: branch, checkout, cherry-pick, fetch, merge, rebase (`rebase -i`),
revert, stash, worktree, bisect, format-patch, am.

* Other: archive, gc, repack, submodule, remote, blame, 

Manpages are also a good resource for learning Git. `gittutorial(7)` is a
tutorial introduction to Git, `gitworkflows(7)` is an overview of recommended
workflows with Git.

## 1. Correctly Understanding Deep Learning Framework

### 1.1. Computation Graph

### 1.2. Automatic Differentiation

### 1.3. Deep Learning Framework Design

[1] [MegEngine Design](https://www.bilibili.com/video/BV11C4y1t7xH?from=search&seid=4625351944580914076)

## 2. A Bit of Scientific Computation Background

Mathematical software mainly involves two kinds: Numerical system (such as
Julia, Matlab, NumPy) and symbolic system (e.g., Mathematica, Maxima, SymPy).
Multi-dimensional numerical arrays are the central part of a numerical system,
while symbolic systems aim to simplify (or solve, etc) equations in a symbolic
form without actually calculating numbers.

[Scientific computation](https://en.wikipedia.org/wiki/Computational_science)
is the collection of tools, techniques, and theories required to solve on a
computer mathematical models of problems in science and engineering.

Numerical Linear algebra is a very important part of scientific computation.
Where there is multi-dimensional arrays, there is numerical linear algebra.
Judging on the difference in how multi-dimensional arrays are organized in the
memory, numerical linear algebra can be either dense or sparse. Linear algebra
operations that manipulates a contiguous chunk of memory belong to dense
numerical linear algebra.

The most computational intensive parts of deep neural networks, are covered by
numerical linear algebra. Namely, numerical linear algebra is largely a
computational performance bottleneck of a deep neural network.

[1] https://www.scicomp.uni-kl.de/about/scientific-computing/

### 2.1. IEEE 754 and Floating-Point Precision

In [numerical
analysis](https://en.wikipedia.org/wiki/Numerical_analysis#Generation_and_propagation_of_errors),
the floating-point standard (IEEE 754) has a very strong implication on
floating-point precision and error due to limited machine number presentation.
There are round-off errors, truncation errors, discretization errors, and
numerical stability (overflow, underflow) issues.

In the code implementation of some machine learning algorithms, you may have
noticed that a very small constant `e` will be added to a fraction `a/(b+e)` in
order to maintain numerical stability, especially when `b` may be a very small
value (will lead to a very large value, which eventually overflows to `+inf`).
You may also see some mathematical operations transformed to other forms for
sake of better numerical stability during computation. Refer to Section 4 of
[Z2] for detail.

All scientific computing libraries, especially those important ones, must be
aware of floating-point precision, and ensure a sensible level of numerical
stability. For example, partial differential equation solvers in the physics or
chemistry fields are sensitive to precision (so they often use float64), while
deep neural networks, which are not quite sensitive to precision, can converge
to a proper state with lower precision (e.g., float32, bfloat16, float16) in
return of much higher throughput. In practice, training neural networks using
float64 is not necessary, and float32 is the default precision for most cases.

TODO: simple examples in C language

### 2.2. Numerical Linear Algebra

**Numerical linear algebra** focuses on linear algebra operations on
multi-dimensional numerical arrays, either dense or sparse. It covers
vector-vector, matrix-vector, matrix-matrix operations such as addition and
multiplication, as well as a series of matrix decomposition methods, matrix
inversions, least squared solvers, etc.

**Dense numerical linear algebra** manipulates numerical arrays stored in a
continuous chunk of memory (the whole array can be linearly indexed in the
memory).  Example libraries include Basic Linear Algebra Subroutines (BLAS) and
Library of Linear Algebra Routines (LAPACK). The reference implementation for
both of them are written in Fortran, and have a very stable set of API and ABI.
Due to a very long history and very important roles in scientific computing,
BLAS and LAPACK can be regarded as a standard.

* BLAS: As you may have noticed, BLAS API follows a Fortran-flavor naming
scheme.  The first character indicates precision (`s` for single-precision
(float32), `d` for double-precision (float64), `c` for single-precision
complex, `z` for double-precision complex). The trailing letters describe the
abbreviated operation name.  BLAS functionalities can be divided into three
groups: vector-vector subroutines (also called level-1 BLAS; e.g., `sasum`
for single-precision [s] absolute [a] sum [sum] of a vector; `saxpy` for
single-precision [s] (constant) alpha [a] * (vector) x [x] + [p] (vector) y
[y]; `?scal` for scaling a vector by a constant; `?dot` for dot-product
between two vectors; `?swap` for swapping values between two vectors; `?copy`
for copying a vector to another; `?nrm2` for the L-2 norm of a vector),
matrix-vector subroutines (also called level-2 BLAS; e.g., `sgemv` for
single-precision [s] general [ge] matrix-vector [mv] multiplication; `?ger`
for multiplying a column vector with a row vector into a matrix), and
matrix-matrix subroutines (also called level-3 BLAS; e.g., `sgemm` for
single-precision [s] general [ge] matrix-matrix [mm] multiplication.  For
level-2 and level-3 BLAS, there are operations for other types of matrices
for better efficiency. For example, `ssymv` is for single-precision symmetric
[sy] matrix-vector multiplication. BLAS also support specifying strides,
matrix transpose, upper/lower-triangular, etc. Please refer the [netlib blas
quick reference](http://www.netlib.org/blas/blasqr.pdf) for more details of
the BLAS API.

* LAPACK: LAPACK involves higher-level linear algebra subroutines built upon
BLAS (BLAS is frequently used in LAPACK subroutines). For example, `?gesv`
solves linear system `AX=B`, `?gels` for solving generalized
(under-determined or over-determined) linear system using QR or LU
decomposition, `?gesvd` performs general singular value decomposition, and
`?gesdd` is an alternative algorithm to `?gesvd` for singular value
decomposition in lower precision but faster speed. Please refer to the
[lapack user guide](http://www.netlib.org/lapack/lug/lapack_lug.html) for
more details.

**Sparse numerical linear algebra**, as is named, manipulates sparse numerical
arrays that are organized in specific ways (instead of a continuous chunk of
memory), because there are different measures to efficiently store a matrix
with most elements being zero. Example libraries include SuiteSparse and Scipy
(`scipy.sparse`). Sparse linear algebra provides similar functionalities to
dense linear algebra, and are simply specifically designed due to its special
array organization.

### 2.3. Dense Linear Algebra Acceleration

(1) cache access optimization (2) simd instruction sets (3) paralellelization
(4) dedicated hardware (GPU, TPU, FGPA).

batched operation and unfolded operation: cache misses
(http://ithare.com/infographics-operation-costs-in-cpu-clock-cycles/)

### 2.4. DNN Libraries

cuDNN, oneDNN

## 3. Program Review, Diagnosis and Debugging

### 3.1. Program Review

### 3.1. Program Tracing

### 3.2. Program Debugging

## 4. High Performance Programming

### 4.1. System Monitoring

Linux kernel provides a wide range of statistics through `sysfs` and `procfs`,
etc.  You may directly read the system informations such as CPU idle time and
available RAM from these special file systems (in fact, you have to read data
in this way if you want to write a system monitor). However, for sake of higher
efficiency, we usually use some sweet utilities.

Here are some decent system monitoring tools.

1. `htop`. You may be aware of `top`, a traditional tool for displaying unix
system resource. `htop` is a friently alternative to it. Using `htop`, you may
monitor: CPU usage, RAM usage, SWAP usage, ZFS ARC usage, System Load, CPU
usage per process, RAM usage per process, etc. Example command line: `htop`.

2. `iostat`. This utility can monitor the real-time IO statistics for all block
devices attached to the current system. If you want to investigate whether
your program performance is limited by the IO performance of some block device,
you may use this utility to help diagnosis based on the configuration of the
physical device (SATA HDD, SATA SSD, M.2 NVMe SSD, U.2 NVMe SSD, Device Mapper,
etc).

3. `dstat` is an overall system monitor that provides condensed summary.

4. `glances` is also an overall system monitor that provides detailed summary.

There are many other unmentioned alternatives. Here we only talk about a
couple of them.

### 4.1. Server Architecture

### 4.2. Profiling

linux perf (for elf executable)

CPU bound: algorithm complexity.

IO bound.

GPU latency. (cudaMemcpy)

GPU is not always faster than CPU in terms of linear algebra operations, as
`cudaMemcpy` is not something trivial. For instance, CPU could be much faster
than GPU in terms of very small matrix multiplication, because the `cudaMemcpy`
latency for transmitting the matrix from RAM to video memory already exceeded
the time consumption of CPU.

### 4.3. IO and Storage System

IO bound: (1) /dev/shm (2) ssd (3) prefetch (4) parallel (5)...

### 4.4. High Performance Python (pure Python)

profiling (cProfile)

int is an object. overhead of magic methods.

### 4.5. Extending Python with Compiled Language

python extension

Foreign Function Interface (FFI)

## 5. Scheduling Interactive Experiments

### 5.1. Interactive Experiments

### 5.2. Computational Debugging

## 6. Paper Reading and Reviewing

In the past, I used to ask my advisor: "I don't have idea about what to study
next. Could you please give me some advice?".  Now I realized that asking such
kind of question basically indicates the lack of paper reading, or the reading
technique and strategy is questionable.

Paper reading and paper reviewing are two very similar process, but there are
still some subtle differences. The motivation of paper reading is usually
grasping new ideas and techniques and adding them into your knowledge graph,
and sometimes seeking for inspirations. The process of paper reviewing is far
beyond paper reading. One has to not only grasp the new ideas correctly, but
also has to think critically -- Is the proposed method technically correct and
sound? Is the paper logic fluent? Are the experiments designed scientifically?
etc.

In my opinion, when one is able to review a paper well, they are already able
to understand the key points for reading a paper. Thus, I shall omit discussion
on paper reading, and directly talk about paper reviewing.

### 6.1. Paper Reviewing

First we can refer to some paper review guidelines, e.g., [CVPR2020 reviewer
guideline](http://cvpr2020.thecvf.com/submission/main-conference/reviewer-guidelines)
in order to understand what is a good review, and what should a good review
represent. You can also read the [CVPR AC
Guide](http://cvpr2020.thecvf.com/submission/main-conference/reviewer-guidelines)
to see what kind of review is helpful for the community, and what's not.

Carefully think about the following questions when you try to review a paper:
(I summarized these points based on external materials)

1. What is the problem addressed in this paper? Is this problem important?  How
well is the problem addressed? What are possibly remaining but valuable
problems? A paper must has its core focus. An influential paper must be
discussing about something important. Besides, if nothing can be done following
this work, then who will cite this paper?

2. What is the scientific hypothesis that the paper is trying to verify?
A good paper must has a good motivation. And a good, deterministic motivation
is highly likely leading to clear hypothesis before conducting experiments.

3. What are the related works? Are the differences compared to the most
relevant works clearly justified? A good paper must has its uniqueness, and
can be clearly differentiated from existing works. The related works can help
you embed this paper in your knowledge network.

4. What is the key of the proposed solution in this paper? This is the core
contribution and novelty of this paper.

5. How are experiments designed? Are the quantitative and qualitative experiments
sufficient to support the effectiveness of the proposed method? Can the performance
improvement be attributed to the core contribution? Does the experiments support
the hypothesis of the paper?

[1] [external reference](https://www.msra.cn/zh-cn/news/outreach-articles/%E5%BE%AE%E8%BD%AF%E5%AF%BC%E5%B8%88%E4%BA%B2%E6%8E%88%E8%AE%BA%E6%96%87%E7%A0%94%E8%AF%BB%E5%8D%81%E9%97%AE%E5%9B%9E%E7%AD%94%E9%80%9A%E5%88%99)

[2] https://zhuanlan.zhihu.com/p/163227375

### 6.2. Writing a Review for Paper

The review mainly consists of five parts: (1) paper summary; (2) paper
strengths; (3) paper weaknesses; (4) preliminary rating and justification; (5)
detailed comments (including minor issues of the paper).

Some aspects on which you can make a comment: Is the paper organization
logically fluent? Is the survey of related works adequate? Is the technical
contribution clearly described? Is the technical contribution original? Is the
technical contribution sound? Are the experiments scientifically designed? Are
the experiments sufficient to support the hypothesis or demonstrate the
effectiveness? Are there enough details for the reader to reproduce this work?
Can the performance improvement be attributed to the contribution of this
paper? Be sure to be specific when giving comments on these aspects.

Of course, the reviewers can make some subjective judgements. For instance, is
the paper well written? Is the paper novel? Once you decide to give such
subjective comments, please be sure to be specific. Namely, you should explain
why the paper is (not) well-written (which paragraph / part, due to what?), or
explain why this paper lacks novelty (or originality).  Carelessly saying a
paper lacks novelty without providing concrete reasons and evidence is
irresponsible and harmful for the research community.

If you find some errors in the manuscript, such as typo, small mathematical
error, missing definition for a symbol, etc. As long as they do not
considerably hamper understanding of this paper, they should be considered
minor, and do not constitute any reason for lowering the rating.

#### 6.2.1. Excerpt from CVPR reviewer guide

This is directly taken from CVPR reviewer guide for your reference.

**Summary:** explain the key ideas contributions, and their significance. This
is your abstract of this paper. This summary helps the AC and the authors
understand the rest of your review and be confident that you understand the
paper.

**Strengths:** what about the paper provides value -- interesting ideas that
are experimentally validated, an insightful organization of related work, new
tools, impressive results, something else? most importantly, what can someone
interested in the topic learn from the paper?

**Weakness:** what detracts from the contributions? does the paper lack
controlled experiments to validate the contributions? are there misleading
claims or technical errors? is it possible to understand (and ideally
reproduce) the method and experimental setups by reading the paper?

**Rating and Justification:** carefully explain why the paper should be
accepted or not, this section should make clear which of the strengths and
weaknesses you consider most significant.

**Additional comments:** minor suggestions, questions, corrections, etc. that
can help the authors improve the paper, but are not crucial for the overall
recommendation.

### 6.3. Surveying a New Area

I. Read the latest top conference papers, as well as the highly cited papers in
this field as the starting point. II. Recursively expand the network following
the references (related works section) in the papers you read. III. Create a
taxonomy to group and differentiate these works.

### 6.4. Incubation of New Ideas

It will be interesting.

TODO

## 7. Organizing Preliminary Draft

This section mainly discuss latex typesetting, drafting conference / journal
papers, polishing papers before submission, conference / journal rebuttal,
slides and poster composing.

### 7.1. LaTeX Typesetting

LaTeX is not a What-You-See-Is-What-You-Get (WYSIWYG) text composing system,
but it is prevalent for professional typesetting, such as paper composing.

My most recommended quick reference for LaTeX is ["A short introduction to
latex 2e"](https://ctan.org/pkg/lshort). If you want to master latex, you
may directly read [Knuth's original TexBook](https://ctan.org/pkg/texbook).

The following are some additional resources about latex, including tips and
some advanced techniques:

[1] https://github.com/simonharrer/latex-best-practices

### 7.2. Drafting a Conference Paper

I shall cover all aspects of drafting a conference paper.  My discussion is
based on CVPR submission.  I'm not a experienced researcher, please don't take
my personal opinions seriously. Only use the following content as a reference,
please.

Those influential (highly-cited) papers are very good examples from which you
can learn how a good paper is composed. Try to analysis their organization,
think about why each part exists, and how each part is connected.

#### 7.2.1. Selecting a Decent Research Topic

If you have not determined a concrete topic to study, you may first try to find
a research field of your interest and pleasure. Then assemble an informal
survey (or mind-map) for this field. Be sensitive to the taxonomy of existing
works, the trend of a field, the remaining (but important) problems in a field.

In practice, a pure research topic might be saturated already (e.g., image
classification), but cross-discipline topics can still provide an amount of
low-hanging fruits, or new inspirations, or even new problems. But take heed,
don't combine different topics directly and casually. Some of such combination
problems are indeed not yet explored, but are they really valuable, reasonable,
and novel?

Choice is sometimes more important than effort. Besides novelty and value,
there are also some other practical factors to concern when you choose a
research topic.  For instance, computational resource and dataset access must
be a concern for not rich researchers intending to study facial recognition
techniques. Big rich companies can allocate thousands of GPUs for a group of
researchers, while the demand for tens of GPUs could be an unsolvable problem
for people in universities (especially non-top universities). Unless one has
unique and ingenious idea in such fields, I think it is very hard to compete
with the others. Anyway, one should probably carefully evaluate the demand of
resource when choosing a concrete topic.

When your have a preliminary new idea, it is very important to instantly setup
a prototype to validate the idea. Some ablation study or parameter search may
involve in the process, but it should not take too long time for you to
validate whether or not the new idea works. Not every new idea will work as you
expected. Being able to quickly verify whether or not it works is equivalent to
saving one's life, or at least buying more time and energy.  The methodology of
ablation study and parameter search is discussed in separate section of this
material.

For academic research, a good new idea and its prototype is not necessarily a
complicated product.  Complicated products significantly increases the cost for
the readers to understand, accept, and reproduce the work. On the contrary,
small and delicate (simple and beautiful) ideas that works decently can also be
influential, and widely adopted by the community. Recall one of the UNIX
philosophies -- do one thing, and do it well. In my opinion, a good paper may
have some of the following merits: (1) small, simple, delicate and beautiful
mathematical core; (2) highly motivated, and focuses on a clear, specific
problem; (3) the problem is valuable, while the solution is novel and original;
(4) the logical flow of the paper is basically linear and fluent; (5) adequate
and strong experimental evaluations; (6) instructive or inspiring for readers
(potential to become a highly-cited paper).

#### 7.2.2. Selecting a Title.

The title conveys some key information to the reader -- what idea or method is
proposed for what purpose? The title should be composed of a few key words
covering: (1) the problem that this paper focuses on; (2) the idea, method, or
novelty of this paper. Besides conveying ideas to the reader, the title must
also be easily searchable (unless you don't want to be cited).

Sometimes we may see fancy titles using metaphors, etc. These titles, if the
corresponding paper does not present very influential work, may impose
difficulty on the readers to correctly understand what this paper is doing when
they browse the paper lists. When you browse a list of papers, will you really
read the abstract and pay more time on a paper with a strange title from which
you cannot immediately grasp the underlying idea? Do you think you can find
such related works (using fancy and indirect titles) with the commonly used
keywords?  However, if the work will be influential, fancy titles may become a
plus.

#### 7.2.3. Abstract.

Concise and fluent, but does not lack of technical detail -- that's what an
abstract should look like.

Abstract is the zoom-out version of the whole manuscript. It summarizes the
content of the whole paper in a concise manner, while pointing out some of the
key technical details. Ideally, the abstract is logically fluent, and a
sentence in the abstract corresponds to a part in the introduction.  Thus, the
**consistency** between the abstract and introduction will make the reading
process easier, and avoids distraction of reader's attention due to anomaly
(i.e., inconsistency). For example, the abstract covers our content A, but
missed our content B. When we introduce content B in the introduction, it feels
abnormal and abrupt, and hence distracting the reader.

Try not to introduce too many new concepts in the abstract. They prevents the
reader from quickly understanding your work. Replacing new concepts with plain
and naive descriptions may be a good idea for reducing the understanding
obstacle.

After finishing a good abstract, the reader should be roughly aware of what the
paper is doing, and what is the key point of this paper.  Hence, the readers
can properly build their attention based on such prior knowledge, and better
understand the paper.

Rethink of the abstract if your friend unfamiliar with related fields cannot
grasp even a bit of idea from it.  Rewrite the abstract if your collaborator
cannot obtain the discussed information from it.

If you don't know how to write an abstract for your almost-finished paper, try
to force yourself to present the work to the others within two or three
minutes. This process may help you condense the paper and extract the core
parts from it.

A good abstract should not waste too much space for the background. It is
suggested to fastly transit from background introduction to the observations,
motivations, and core contributions.

A preliminary abstract may look like a combination of four key points: (1)
background introduction; (2) observation and motivation; (3) insightful
solution for such problem; (4) how the proposed solution is evaluated; (5)
conclusion from the experiments. Note, abstract is flexible, and this template
can at most serve for a preliminary draft.

#### 7.2.4. Introduction

In the most ideal case, every part of the introduction can be corresponded to a
word in the abstract. Namely, the introduction can be seen as an extended
version of the abstract. Similarly, the storyline of the introduction should be
logically linear for ease of writing and understanding.

The introduction part has abound space for smooth connection between the key
points of the paper to make the story line simple and linear. Some important
but transitional sentences will not be written in the abstract -- the
introduction is where they should be put.

Being logically linear is quite important. Many readers will only skim the
abstract (and figures). Some of them will skim more until the end of
introduction.  Abrupt logical organization or too much irrelevant content will
definitely distract the reader from whatever they should focus on.

A fast reading technique is to read only the first sentence of a paragraph.
When you write a paragraph, it is also a good practice to only include one key
point in a paragraph, and clearly state the key point of this paragraph in the
first sentence. This is merely optional.

In the end of the introduction, the contributions of a paper should be
summarized following the convention. This summarization is also helpful for
rushy reviewers that do not really have much spare time on the paper --
explicit pointers on the paper contribution sometimes help.

By the way, I don't think things like "extensive experiments" can be listed as
a contribution (in most cases). The experiments are a part of the proposed
method for validating its effectiveness, instead of a standalone point.
Besides, is "extensive experiments" something novel enough to highlight the
paper?

#### 7.2.5. Related Works

An adequate survey work will make writing this section much easier.

Instead of simply introducing the related works, it is suggested to organize
these works in a clear rule: publish time? Influence? Or a certain taxonomy?
In general, a part of related works focuses on a key word. In the related works
section, these parts can be sorted by relevance to the main topic of the whole
paper.

Besides introducing related works, you can also clearly state the difference
between this paper and the existing works. This section is a good place to
emphasize any difference by contrast.

#### 7.2.6. Our Approach

This section mainly involves formulations and detailed solution. Try to keep
the storyline as simple as possible. This section cannot be written along the
logic of pseudo-code of your algorithm.

Although we focus on technical (mathematical) details in this section, please
don't hard-code any concrete parameter. Don't abruptly present conclusions from
experimental results neither.

Linearity is also important for this section. For example, our proposed method
has several variants. In pseudo-code, these variants can be organized in an
if-else (switch-case) structure, but writing a section 3 such structure is a
disaster. In this case, which one is the default method? What is the difference
between these variants? What variant should be used in what scenario?  Can
these variants be generalized into a united form? What concrete variant should
the reader pay most attention to? It is suggested to finish describing a whole
variant first, and then discuss the way of adapting it into other variants.
The adaptation procedure can be omitted if it's simple and repetitive.

If you don't know how to start section 3, try to briefly review the
mathematical definition of the problem that you are trying to solve. Then
briefly review the common practice (from mathematical point of view) in related
works. Next, it may be the time for you to describe your observed problems,
your motivation, and smoothly transit to the discussion on core topic.

#### 7.2.7. Experiments

This part is relatively easy to write, as long as you have a clear mind on
what to experiment or verify, and what result supports what hypothesis.

In convention, we may first introduce the experimental settings, such as
dataset information and the model details such as hyper-parameters, optimizer
parameters, data pre-processing pipeline, and some minor implementation details
that better ensures the reproducibility of this work. Anyway, don't hide
important details.

Then, you may try to describe how your experiment is organized and conducted,
as well as why you do such experiment. Then you may explain how the result
tables and figures mean, and compare your solution with the previous works.
Besides some shallow conclusions (e.g., the results demonstrate the
effectiveness of our proposed method), try to dive deeper into the reason why
your solution works, while surpassing the existing works (e.g., the solution
overcomes the XXX problem that the previous methods unanimously neglected; of
course, you may immediately realize that you need some ablation study or
parameter search to support your claim).

In brief, the template for the experiments section is (1) what to do; (2) why
doing it; (3) how to do it; (4) what is the result, and how good is it
comparing with previous works; (5) what does the result imply; (6) why do we
obtain such a result, or can we attribute the improvement to our core
contribution; (7) what's possibly the remaining limitation.

Note, if you need to add equations in the experiments section, please always
explain the physical meaning first. Don't throw equations on the reader's face.

#### 7.2.8. Discussions

#### 7.2.9. Conclusion

The conclusion is more or less a "conjugate" version of the abstract. Their
difference is subtle. The abstract can be written in a somewhat hypothetical
tone (e.g., we think some problem should be solved in what way), while the
conclusion can be written in a "determined" tone (e.g., we discover what way
can properly solve what problem).

If there is still enough space to write some words, you may also discuss
the potential future works or research directions for the reader's reference.

Anyway, redirect your energy for designing a good conclusion into designing a
good abstract. Although I should not say something like "only a small portion
of readers will read till the end of conclusion", do you really carefully read
the conclusion of a paper?

#### 7.2.10. Supplementary Material

You may include (but not limited to) these things into the supplementary
material: (1) more visualizations; (2) a detailed explanation of some condensed
content in the main manuscript, e.g., mathematical proofs; (3) less important
experiments that are not necessary to be presented in the main manuscript; etc.

Note, if you really have some important experiments in the supplementary
material because there is no enough space in the main manuscript, you may
simply mention the experiments and its most important conclusions at a proper
place of the main manuscript.

Don't break your promise in the main manuscript that you will put something in
the supplementary material. Don't put unrealiable bits in the supplementary.

#### 7.2.11. Meta Key-Points

There are still some key-points that applies to a large portion of this paper.

1. **Ratio of original content.** Apart from Section 2, most of rest part of
the paper should be discussing your original work. They are stages for you
to present your own work, instead of the others'. Even if we have to recall
the previous works in order to make the paper self-contained or provide enough
technical background for the reader, why should we drown our own contribution
by showing others' work?

2. **Tense and Tone.** Keeping a consistent simple present tense is enough.
Try to reduce the use of "we" as a leading word of sentences. These
sentences are relatively subjective compared to those written in passive tense
(relatively objective).

3. **Logical flow.** Important things can be repeated many times. The logical
flow should be as simple and linear as possible.

### 7.3. Drafting a Journal Paper

### 7.4. Self-Reviewing and Polishing

### 7.5. Conference Rebuttal

Carefully read the official rebuttal instructions, e.g., the [ICCV2021 rebuttal
instructions](http://iccv2021.thecvf.com/node/4#rebuttal-instructions), and
fetch the template. Then extract the questions from the reviews, and answer
them one by one.

TODO: key points for writing a rebuttal.

Don't always assume the reviewers are in good faith if you feel some reviewer
response strange. Always be prepared for the worst case and the ensuing
implications, say, when the reviewer is somehow hostile or irresponsible.
Whether or not such reviewer will devastate the reputation of the research
community, for oneself the most important thing is happiness, as almost nothing
can be done to fight against injustice or fate.  Reaching your family for
support might be a good idea at this point.

References:

[1] https://www.zhihu.com/question/32055996

[2] https://zhuanlan.zhihu.com/p/104298923

[3] https://blog.csdn.net/Ema1997/article/details/107103487

### 7.6. Journal Response

### 7.7. Slides and Poster

#### 7.7.1. Slides

#### 7.7.2. Poster

The core essense of a poster is a free-style composition to advertise your
work, technical but easy to grasp.

CVPR poster is usually a 48 inch x 96 inch long picture (aspect ratio is 2:1).
Some other poster templates are based on the standard A0 sized paper. The
concrete poster size varies across different conferences. When creating your
poster, make sure to leave enough space to the paper margin, because you may
want to cut the paper to fit the frame. Besides, check if your printer can
print within 0.5 inch to the very edge of the paper.

Font size recommendtation: Normal text 64pt. Small text 56pt. Fonts smaller
than 48pt may be hard to read from a distant view point. Title font size can
be some value bewtween 100pt to 144pt.

Font recommendtation: Choose as your pleasure. Serief-free fonts may be easier
to read from a far place. Serief fonts looks more consistent with mathematical
equations in CVPR manuscript.

Page layout recommendation: For A0 paper size (aspect ratio: 1:sqrt(2)),
double-column typesetting is feasible. For long posters (aspect ratio is 1:2),
three-column typesetting is feasible. Note, the poster session may be very
crowded. A multi-column layout design enable your crowded audience to read
your whole poster while walking from left side to right side.

Content recommendation: Use pictures, diagrams, tables to tell the story.
People like those. For ease of understanding, organize these informations in a
linear logic. Put more visualizations than the main manuscript. Put important
things that may attract the audience to read the main manuscript. Don't copy
the main manuscript onto the poster. If a poster looks like a zoomed-in version
of a manuscript, people may want to skip it and read the manuscript directly.

How much portion on poster should some content occupy? The poster should mainly
present visual informations, and use textual informations as supplementary.
Somesay that the portion of textual information can be 20%~25%, that of visual
information can be 40%~45%, while the rest space should be left blank.

The upper left corner can be the logo of your university or organization, while
the upper right corner can be the conference logo. Put your paper title at the
top center position. Right below are author list and affiliations.  Add QR
codes to your arxiv preprint and git repository at a proper corner of your
poster. QR codes makes one's life easier.

### 7.8. Miscellaneous Questions and Answers

- Uploading something to Arxiv? This is too tricky. This is not a proper place
for discussing arxiv usage, as the reasons may be subjective, which makes it
extremely hard to tell true reasons from false reasons.

- Suggestions towards mistakes frequently made by authors? (1) Plan ahead and
stick to your plan. The plan may be subject to change, but there should be a
plan. A good plan makes your work with collaborators error-tolerant; (2)
Improve the workflow. When there is multiple collaborators working on the same
project, a sane version control system is mandatory for ensuring safety and
efficiency; (3) Keep specific terms and typesetting consistent throughtout the
whole manuscript; (4) Don't introduce too many unnecessary terms in the
manuscript; (5) Don't resue mathematical symbols. You may borrow the
mathematical symbol definitions from ICLR tex template; (6) Write smooth
story line and avoid making it fork-shaped; (7) Parameter settings is not a
part of Section 3; (8) Captions may imply groupping of a set of subfigures;
(9) Avoid ugly diagrams with problematic color, shape, size, layout, alignment
and content.

## 8. A Tiny Bit on Art

Reference material: [how to draw ugly diagrams?](assets/ugly-diagram.pdf) [(svg source)](assets/ugly-diagram.svg)

Color, Shapes, Lines, Layout, Fonts

## A. Python Proficiency

### A.1. Python Library Recommendation

The [python standard libraries](https://docs.python.org/3/library/index.html)
are already extremely useful. Before looking for external python libraries,
make sure whether the [python standard
library](https://docs.python.org/3/library/index.html) provides what you need.
Here are some standard libraries that I think are sometimes useful in the
context of deep learning research:

1. `re` -- regular expression  
2. `collections.abc` -- abstract base classes for containers  
3. `itertools`, `functools`, `operator` -- functional programming  
4. `glob` -- unix style pathname pattern expansion  
5. `csv` -- CSV file reading and writing  
6. `configparser` -- configuration file (.ini) parser  
7. `ctypes` -- foreign function library  
8. `multiprocessing` -- process-based parallelism  
9. `subprocess` -- subprocess management  
10. `json` -- JSON encoder and decoder  
11. `urllib` -- URL handling modules  
12. `typing` -- type hints  
13. `dataclases` -- data classes  
14. `contextlib` -- utilities for `with`-statement contexts  
15. `gc` -- garbage collector interface  
16. `importlib` -- implementation of `import`  

In scientific computing context, standard libraries like `math`, `random` and
`statistics` are very likely replaced by `numpy`. Standard library `pickle`
is well-wrapped by `torch.save`. Very frequently used standard libraries
such as `os`, `sys`, `io`, `time`, `argparse` are needless to discuss.

Here are some useful third-party python libraries (I may also mention the
standard library if there is an alternative).

1. `ipython3` (friendly REPL)  
2. `multiprocess` / `joblib` (paralellization)  
3. `numba` (acceleration with JIT compilation)  
4. `pandas` (XLSX in python)  
5. `tqdm` (progress bar + timer)  
6. `h5py` (storing large amount of data)  
7. `click`, `fire` (alternative to `argparse`)  
8. `pytest` (unit testing)  
9. `faiss` (fast clustering and similarity search)  
10. `nltk`, `spacy` (many tasks in the NLP field)  
11. `rich` (beautiful terminal output)  
12. `seaborn` (beautiful statistics graphs)  
13. `ujson` (faster `json` alternative)  

Standard scientific computing and machine learning libraries such as `numpy`,
`tensorflow`, `torch`, `scipy`, `skimage`, `sklearn`, `matplotlib` are needless
to mention here.

### A.2. Proficiency

I'd like the emphasize again that the [python official
tutorial](https://docs.python.org/3/tutorial/index.html) is one of the best
(free-of-charge) learning materials. It is also recommended to read the
changelogs of minor python releases (e.g., python 3.8, python 3.9, python
3.10), and be aware of language changes and new features.

Here I have some additional questions and hints on python programming.  Note,
please make sure that you can instantly verify your programming idea with
`ipython`, and learn programming in an interactive way.

1. Do you know what `'string'`, `"string"`, `"""string"""`, `r'string'`
and `f'string'` mean in python? Which one should be used in what scenario?
Besides, different people prefer to write formatted strings in different ways,
such as `"..." & (...)`, `f"... {foobar} ..."`, `"...".format(...)`. You may
need to understand these in order to understand other people's code.

hints: [strings](https://docs.python.org/3/tutorial/introduction.html#strings)
[f-string](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting)

2. Do you know that a python program will go through lexical analysis and
syntax analysis before being interpreted? The following is a example of
abstract syntax tree (AST).

```python
In [1]: import ast

In [2]: src = '''
   ...: a = 1
   ...: b = 2
   ...: c = a + b
   ...: '''

In [3]: print(ast.dump(ast.parse(src), indent=2))
Module(
  body=[
    Assign(
      targets=[
        Name(id='a', ctx=Store())],
      value=Constant(value=1)),
    Assign(
      targets=[
        Name(id='b', ctx=Store())],
      value=Constant(value=2)),
    Assign(
      targets=[
        Name(id='c', ctx=Store())],
      value=BinOp(
        left=Name(id='a', ctx=Load()),
        op=Add(),
        right=Name(id='b', ctx=Load())))],
  type_ignores=[])
```

## B. Editors and IDEs

The two traditional text editors for Linux are `vim` and `emacs`. I personally
recommend `vim`.

Currently I have no idea on how to discuss modern editors such as vscode and pycharm.

## C. Physical Server Management

### C.1. IPMI

IPMI can be used to hardware-reset a machine remotely, in case of kernel panic
or other server troubles. Let's assume that the IPv6 address of the IMPI card
on the machine of interest is `fe80::abcd`. Then, we can first query its power
status:
```
ipmitool -I lanplus -H fe80::abcd%eno1 \
	-U <USER> -P <PASSWORD> chassis power status
```
Or directly reboot it (hardware reset):
```
ipmitool -I lanplus -H fe80::abcd%eno1 \
	-U <USER> -P <PASSWORD> chassis power reset
```

Here I use IPv6 address because in some cases the IMPI card of the remote machine
is unconfigured, and hence has no IPv4 address. Assume the ethernet port of our local
host is directly connected to the RJ45 port of the IPMI card, we can first setup
an IPv6 link-local connection (see network-manager `nmtui` for details). If our
network device is called `eno1`, then we can ping the pre-defined IPv6 multicast
address `ping6 ff02::1%eno1`, and see which IPv6 addresses will respond. After
taking out the local IPv6 address of `eno1` and the local IMPI IPv6 address (if
any; use `sudo ipmitool lan print` to check the MAC address and IPv6) from the
responder list, we should be able to identify the remote IPMI card IPv6 address.

## D. Extra Linux Productivity Utilities

All these utilities are available under linux. I don't know whether they are
available on windows or macosx.

1. Printing image in a text-based terminal: `catimg` and `chafa`.

2. Composing latex document very quickly: `lyx`. It has a brilliant GUI for
drawing tables easity, and can export the document into pdflatex format.

3. Vectorized graph editing: `inkscape`.

4. Bitmap editing: `gimp`.

5. `build-essential` is the meta-package containing compiler toolchains
for Debian-based linux distributions (e.g., Ubuntu).

6. `codespell` can be used for fixing typos in your code project.

7. `fail2ban` enhances security of your linux server against brute force attack.

8. `filezilla` is a GUI program for transmitting files via sftp protocol, etc.

9. `fish` and `zsh` are two user-friendly feature-rich shells.

10. `flameshot` is used for taking screenshots.

11. `freeplane` for mind-map.

12. `fd` (rust) as an alternative to `find` in findutils.

13. `fzf` (go) for fuzzy file searching.

14. `gdb` for debugging binary programs.

15. `git` for version control.

16. `gitea` and `gitlab` for hosting your own git service.

17. `htop`, `dstat` and `glances` for system monitoring.

18. `grc` for colorizing linux command outputs.

19. `ufw` linux firewall (Ubuntu). `gufw` GUI for ufw.

20. `ipython3` for interactive python project development.

21. `ncdu` disk usage analysis.

22. `ranger` text-based file browser.

23. `octave` free alternative to matlab.

24. `ipdb` ipython-based python debugger.

25. `sagemath` free alternative to commercial math systems.

26. `smartmontools` for SMART statistics of hard drives.

27. `testdisk` data rescue.

28. `tig` Git TUI.

29. `wxmaxima` free symbolic math system.

This list is selected based on an assumption that they may be helpful for
deep learning related works.

More insights and details can be found my other documentation project: LiSG. [todo]

## X. Fun Bits

## Y. English Corner

In this appendix section, we discuss English issues that frequently occurs,
and some tips for technical writing.

English issues are very minor (and useless) in the paper reviewing process, and
do not constitute a reason for paper rejection. But a submission aboundant of
English issues will look unprofessional, ugly and rude. It may also imply that
the author has a careless attitude towards the submission, and hence trigger
some reviewers.

Anyway, once a paper is written in the English language, this language itself
should be respected.

## Z. References

[Z1] A collection of guides to successful scientific communication: https://mitcommlab.mit.edu/eecs/use-the-commkit/

[Z2] Ian Goodfellow, et al., deep learning.
