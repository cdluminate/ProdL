---
title: "ProdL: Productive Deep Learner"
author: Copyright (C) 2020-2021, Mo Zhou `<cdluminate@gmail.com>`
date: Version WIP, GFDL-1.3 License, June 2021 
---

ProdL: Productive Deep Learner (WIP)
===

Copyright (C) 2018-2021, Mo Zhou `<cdluminate@gmail.com>`

This document is released under the [GNU Free Documentation License (GFDL-1.3)
](https://www.gnu.org/licenses/fdl-1.3.html) license.

Click here to obtain the latest version of this document. [TODO]

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
in this document.

As a convention in the UNIX/Linux world, a notation composed by a word and a parenthesized number
denotes reference to a manual page. For instance, `signal(7)` means the
topic "signal" in manual page section 7. Type `man 7 signal` in a linux shell
to read the document. If you find the manual for a specific comman too lenthy
to read, you may also consult the [`tldr`](https://github.com/tldr-pages/tldr)
pages.

When talking about commands, `<keyword>` denotes a placeholder that should
be replaced by a sensible value according to the context, instead of being
copied from my examples literally.

When talking about keybindings, `Mod` means the modifier key for a specifically
discussed program. For example, the `Mod` key for `tmux` is `Ctrl+b` by default.
Any keybinding discussed in this document is case-sensitive. Any text rendered
in mono-spaced font are case-sensitive.

Should you find any error or discrepancy in the content, the author is willing
to correct the content. Please file a bug through the Github issues channel [TODO].

Table-of-Contents is only available in the PDF version of this document.

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

### 0.4. Computer Organization, Compiler, etc.

Computer organization [[1]](https://www.coursera.org/learn/jisuanji-zucheng)
[[2]](https://www.geeksforgeeks.org/computer-organization-and-architecture-tutorials/)
[[3]](https://csapp.cs.cmu.edu/)
is critical for you to correctly understand things that harms the performance
of your program. It is also (partly) helpful for you to avoid writing prototype
code without obvious performance flaw. Besides, such background knowledge is
critical for you to understand the performance
of dense numerical linear algebra.

In order to gain an in-depth image on computer programming (whatever in
interpreted language or compiled language), it is suggested to be aware
of [how compilers work](https://en.wikipedia.org/wiki/Compilers:_Principles,_Techniques,_and_Tools).
For example, the key concepts for a compiler involves
lexical analysis, syntax analysis, intermediate
representation, code optimization and target code generation.

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

Both `zsh` and `fish` can support syntax highlighting, automatic suggestion,
and smarter command line completion. I think these features are beneficial
for productivity.

For most linux distributions, POSIX shell is recommended if you are scripting
for the system.

#### 0.5.2. Core Utilities

A non-exhaustive set of core utilities. Here I'll only list their names and main usage.
Most of these utilities are extremely important, and are extremely valuable to learn.

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

In this section, we mainly discuss some tools for accessing remote hosts
(servers), as well as transferring files across different machines.
  
#### 0.7.1. OpenSSH -- Remote Login Client
  
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

### 0.7.2. Mosh -- Supporting Intermittent Connectivity

Working through SSH under a problematic network condition is definitely
frustrating. We can use `mosh` to avoid reconnecting the server again and
again, as `mosh` is able to automatically reconnect to the server when
the network is accessible again. Mosh relies on OpenSSH.

Mosh is not a default part of linux server installation. The user may have
to install the client and the server software on proper machines.

### 0.7.3. Tmux -- Terminal Multiplexer

Technically speaking tmux has no business with remote access, but tmux is
usually used in conjunction with ssh (or mosh). Simply type `tmux` to start a
tmux session.  With such a terminal multiplexer, you can start a new shell in
the tmux session without a new SSH connection (Key: `Mod+c`).  New processes
started in a tmux session will be put into different tmux windows. You can
re-organize these windows flexibly. For example, you can split the window
vertically (Key: `Mod+"`) or horizontally (Key: `Mod+%`) into two panes.  The
`Mod` key by default is `Ctrl+b`.

1. **Intermittent Connectivity:** Due to tmux's server-client architecture,
accidental SSH connection interruption will not lead to termination of programs
running under the tmux session. You can resume the last tmux session with
`tmux attach`. You can even detach again from the session by `Mod+d`, and
manually end the SSH connection.

2. **Scheduling experiments:** Tmux is so flexible that it is even scriptable.
Leveraging its advantages, we can schedule deep learning experiments with tmux
and automate program execution. [Here is an example](https://github.com/cdluminate/advrank/blob/master/Code/pipeline/train-mnist.sh)
for running four experiments under a new tmux session on four GPUs simultaneously.
More complicated scheduling can be implemented in the shell script.

An commonly used alternative to tmux is [GNU screen](https://www.gnu.org/software/screen/).
[Byobu](https://www.byobu.org/) is a high level wrapper on tmux or screen that
delivers out-of-box friendly experience.

### 0.7.3. Graphical solutions such as VNC and RDP

These solutions are fancy and, of course, have a much smoother and less steep
learning curve. I think these solutions are generally less robust than text-based
SSH solution, because (1) they have many vulnerabilities (CVEs); (2) they requires
much higher network bandwidth to function properly compared to SSH; (3) they
are not scalable to a computer cluster or multiple remote servers.
My suggestion is: use these on your preference, if it does not prevent
you from improving productivity.

### 0.7.4. Ansible

[Ansible](https://docs.ansible.com/) can be used to manage a computer cluster
(or multiple remote hosts) in a scalable way. With this tool, you can distribute
some local files (directories) to remote machines, gather remote files (directories)
to local machine, or execute commands on remote machines in parallel. Please
refer its documentation for full description of its functionalities.

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

### 0.7.5. Rsync -- Copying files across hosts

You may be familiar with `scp`,
a standard file transfer tool provided by OpenSSH. And you may have noticed
that `scp` will transfer all file contents when copying a directory to the
remote machine, even if we are overwriting a remote directory with merely some
minor modifications. This could greatly hamper productivity once the directory
to be transferred is huge.

`rsync` is an incremental file transfer tool that does not suffer from such
issue of `scp`. It is able to transfer and only transfer the incremental change
to the remote host, hence vastly improving efficiency especially in cases
where you have to frequently synchronize directories among multiple hosts.

`rsync` is able to transfer files through SSH connection. For example, we can transfer
a local directory to remote side by `rsync -Pav <local-directory> <user>@<ip-address>:~/my-work`,
or transfer a remote directory to the local machine by `rsync -Pav <user>@<ip-address>:~/my-work <local-directory>`. Argument `P`, `a`, `v` mean "show progress", "archive mode", and "verbose", respectively.
When the SSH service is listening on a non-standard port (instead of tcp/22), pass an extra argument
to rsync to use the correct port number: `rsync -e "ssh -p <port>"`.

A successful file transfer via `rsync` requires it to be installed on
both the machines of client and the server sides.

### 0.7.6. SSHFS -- Mounting remote directory through SSH+FUSE

`sshfs` allows you to mount a remote directory to a local path through
SSH and FUSE. For example, if you want to mount a remote directory to
a local path, in order to browse the images on the remote host later:
`sshfs <user>@<remote-host>:/<remote-directory> ~/<local-path>`.
In this way you don't have to copy these images to the local host in order
to browse them. Besides, files under the mountpoint can be manipulated with
standard file management tools such as cp, mv, etc as if are are manipulating
local files.

### 0.7.7. NFS

Network File System (NFS) is used for exporting server's local directories for some
specified clients, so that the clients are able to mount the exported directories
locally. It is similar to sshfs, but is much more scalable and robust for computer
clusters.

### 0.8. Software Engineering

Functional programming. (side effect)

test-driven development.

Reference book: 

[1] Eric S. Raymond, The Art of UNIX Programming.

### 0.9. Git Workflow (Version Control System)

Extremely important for production sanity, safety, and reliability.
I'm not interested in explaining exactly how important it is or why.

There are some alternative version control systems to git, such as svn, hg, etc.

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

Numerical Linear algebra is a very important part of scientific computation. Where there
is multi-dimensional arrays, there is numerical linear algebra. Judging on the difference
in how multi-dimensional arrays are organized in the memory, numerical linear algebra
can be either dense or sparse. Linear algebra operations that manipulates
a contiguous chunk of memory belong to dense numerical linear algebra.

The most computational intensive parts of deep neural networks, are covered
by numerical linear algebra. Namely, numerical linear algebra is largely
a computational performance bottleneck of a deep neural network.

[1] https://www.scicomp.uni-kl.de/about/scientific-computing/

### 2.1. IEEE 754 and Floating-Point Precision

In [numerical analysis](https://en.wikipedia.org/wiki/Numerical_analysis#Generation_and_propagation_of_errors),
the floating-point standard (IEEE 754) has a very strong implication on
floating-point precision and error due to limited machine number presentation.
There are round-off errors, truncation errors, discretization errors, and
numerical stability (overflow, underflow) issues.

In the code implementation of some machine learning algorithms, you may have
noticed that a very small constant `e` will be added to a fraction `a/(b+e)`
in order to maintain numerical stability, especially when `b` may be a very
small value (will lead to a very large value, which eventually overflows to
`+inf`). You may also see some mathematical operations transformed to other
forms for sake of better numerical stability during computation. Refer to
Section 4 of [Z2] for detail.

All scientific computing libraries, especially those important ones, must be
aware of floating-point precision, and ensure a sensible level of numerical
stability. For example, partial differential equation solvers in the physics or
chemistry fields are sensitive to precision (so they often use float64), while
deep neural networks, which are not quite sensitive to precision, can converge
to a proper state with lower precision (e.g., float32, bfloat16, float16) in
return of much higher throughput. In practice, training neural networks using
float64 is not necessary, and float32 is the default precision for most cases.

### 2.2. Numerical Linear Algebra

**Numerical linear algebra** focuses on linear algebra operations on
multi-dimensional numerical arrays, either dense or sparse. It covers
vector-vector, matrix-vector, matrix-matrix operations such as addition and
multiplication, as well as a series of matrix decomposition methods,
matrix inversions, least squared solvers, etc.

**Dense numerical linear algebra** manipulates numerical arrays stored in a
continuous chunk of memory (the whole array can be linearly indexed in the memory).
Example libraries include Basic Linear Algebra Subroutines (BLAS) and
Library of Linear Algebra Routines (LAPACK). The reference implementation for
both of them are written in Fortran, and have a very stable set of API and ABI.
Due to a very long history and very important roles in scientific computing,
BLAS and LAPACK can be regarded as a standard.

* BLAS: As you may have noticed, BLAS API follows a Fortran-flavor naming scheme.
The first character indicates precision (`s` for single-precision (float32),
`d` for double-precision (float64), `c` for single-precision complex, `z` for
double-precision complex). The trailing letters describe the abbreviated operation name.
BLAS functionalities can be divided into three groups: 
vector-vector subroutines (also called level-1 BLAS;
e.g., `sasum` for single-precision [s] absolute [a] sum [sum] of a vector;
`saxpy` for single-precision [s] (constant) alpha [a] * (vector) x [x] + [p] (vector) y [y];
`?scal` for scaling a vector by a constant; `?dot` for dot-product between two vectors;
`?swap` for swapping values between two vectors; `?copy` for copying a vector to another;
`?nrm2` for the L-2 norm of a vector),
matrix-vector subroutines (also called level-2 BLAS;
e.g., `sgemv` for single-precision [s] general [ge] matrix-vector [mv] multiplication;
`?ger` for multiplying a column vector with a row vector into a matrix),
and matrix-matrix subroutines (also called level-3 BLAS;
e.g., `sgemm` for single-precision [s] general [ge] matrix-matrix [mm] multiplication.
For level-2 and level-3 BLAS, there are operations for other types of matrices
for better efficiency. For example, `ssymv` is for single-precision symmetric [sy]
matrix-vector multiplication. BLAS also support specifying strides, matrix transpose,
upper/lower-triangular, etc. Please refer the netlib blas cheatsheet [todo] for more details
of the BLAS API.

* LAPACK: LAPACK involves higher-level linear algebra subroutines built upon
BLAS (BLAS is frequently used in LAPACK subroutines). For example, `?gesv` solves
linear system `AX=B`, `?gels` for solving generalized (underdetermined or
underdetermined) linear system using QR or LU decomposion, `?gesvd` performs
general singular value decomposition, and `?gesdd` is an alternative algorithm
to `?gesvd` for singular value decomposition in lower precision but faster speed.

**Sparse numerical linear algebra**, as is named, manipulates sparse numerical
arrays that are organized in specific ways (instead of a continuous chunk of
memory), because there are different measures to efficiently store a matrix
with most elements being zero. Example libraries include SuiteSparse and
Scipy (`scipy.sparse`). Sparse linear algebra provides similar functionalities
to dense linear algebra, and are simply specifically designed due to its special
array organization.

### 2.3. Dense Linear Algebra Acceleration

(1) cache access optimization (2) simd instruction sets (3) paralellelization
(4) dedicated hardware (GPU, TPU, FGPA).

### 2.4. DNN Libraries

cuDNN, oneDNN

## 3. High Performance Programming

### 3.1. Server Architecture

### 3.2. Profiling

linux perf (for elf executable)

CPU bound: algorithm complexity.

IO bound.

GPU latency. (cudaMemcpy)

GPU is not always faster than CPU in terms of linear algebra operations, as
`cudaMemcpy` is not something trivial. For instance, CPU could be much faster
than GPU in terms of very small matrix multiplication, because the `cudaMemcpy`
latency for transmitting the matrix from RAM to video memory already exceeded
the time comsumption of CPU.

### 3.3. IO and Storage System

IO bound: (1) /dev/shm (2) ssd (3) prefetch (4) parallel (5)...

### 3.4. High Performance Python (pure Python)

profiling (cProfile)

int is an object. overhead of magic methods.

### 3.5. Extending Python with Compiled Language

## 4. Program Review, Diagnosis and Debugging

### 4.1. Program Review

### 4.1. Program Tracing

### 4.2. Program Debugging

## 5. Scheduling Interactive Experiments

### 5.1. Interactive Experiments

### 5.2. Computational Debugging

## 6. Paper Reading and Reviewing

Paper reading and paper reviewing are two very similar process, but there
are still some subtle differences. The motivation of paper reading is usually
grasping new ideas and techniques and adding them into your knowledge graph,
and sometimes seeking for inspirations. The process of paper reviewing is
far beyond paper reading. One has to not only grasp the new ideas correctly,
but also has to think critically -- Is the proposed method technically correct
and sound? Is the paper logic fluent? Are the experiments designed scientifically?
etc.

In my opinion, when one is able to review a paper well, they are already
able to understand the key points for reading a paper. Thus, I shall omit
discusson on paper reading, and directly talk about paper reviewing.

### 6.1. Paper Reviewing

First we can refer to some paper review guidelines, e.g., [CVPR2020 reviewer
guideline](http://cvpr2020.thecvf.com/submission/main-conference/reviewer-guidelines)
in order to understand what is a good review, and what should a good review
represent. You can also read the [CVPR AC Guide](http://cvpr2020.thecvf.com/submission/main-conference/reviewer-guidelines)
to see what kind of review is helpful for the community, and what's not.

Carefully think about the following questions when you try to review a paper:
(I summarized these points based on external materials)

1. What is the problem addressed in this paper? Is this problem important?
A paper must has its core focus. An influential paper must be discussing about
something important.

2. What is the scientific hypothesis that the paper is trying to verify?
A good paper must has a good motivation. And a good, deterministic motivation
is highly likely leading to clear hypothesis before conducting experiments.

3. What are the related works? What are the most related works? A good paper
must has its uniqueness, and can be clearly differentiated from existing
works. The related works can help you embed this paper
in your knowledge network.

4. What is the key of the proposed solution in this paper? This is the core
contribution and novelty of this paper.

5. How are experiments designed? Are the quantitative and qualitative experiments
sufficient to support the effectiveness of the proposed method? Can the performance
improvement be attributed to the core contribution? Does the experiments support
the hypothesis of the paper?

6. What is possibly remaining problems? Or what could be the future work?
If nothing can be done subsequently, who will cite this paper then?

[1] https://www.msra.cn/zh-cn/news/outreach-articles/%E5%BE%AE%E8%BD%AF%E5%AF%BC%E5%B8%88%E4%BA%B2%E6%8E%88%E8%AE%BA%E6%96%87%E7%A0%94%E8%AF%BB%E5%8D%81%E9%97%AE%E5%9B%9E%E7%AD%94%E9%80%9A%E5%88%99

[2] https://zhuanlan.zhihu.com/p/163227375

### 6.2. Writing a Review for Paper

The review mainly consists of five parts: (1) paper summary; (2) paper strengths;
(3) paper weaknesses; (4) preliminary rating and justification; (5) detailed
comments (including minor issues of the paper).

Some aspects on which you can make a comment: Is the paper organization logically
fluent? Is the survey of related works adequate? Is the technical contribution
clearly described? Is the technical contribution original? Is the technical
contribution sound? Are the experiments
scientifically designed? Are the experiments sufficient to support the hypothesis
or demonstrate the effectivensss? Are there enough details for the reader to
reproduce this work? Can the performance improvement be attributed to the
contribution of this paper? Be sure to be specific when giving comments
on these aspects.

Of course, the reviwers can make some subjective judgements. For instance,
is the paper well written? Is the paper novel? Once you decide to give
such subjective comments, please be sure to be specific. Namely, you should
explain why the paper is (not) well-written (which paragraph / part, due to what?),
or explain why this paper lacks novelty (or originality).
Carelessly saying a paper lacks novelty without providing concrete reasons
and evidence is irresponsible and harmful for the research community.

If you find some errors in the manuscript, such as typo, small mathematical
error, missing definition for a symbol, etc. As long as they do not considerably
hamper understanding of this paper, they should be considered minor, and do
not constitute any reason for lowering the rating.

### 6.3. Surveying a New Area

I. Read the latest top conference papers, as well as the highly cited papers in
this field as the starting point. II. Recursively expand the network following
the references (related works section) in the papers you read. III. Create a
taxonomy to group and differentiate these works.

## 7. Organizing Preliminary Draft

### 7.1. LaTeX Typesetting

Advanced Techniques:

1. https://github.com/simonharrer/latex-best-practices

### 7.2. Drafting a Conference Paper

### 7.3. Drafting a Journal Paper

### 7.4. Polishing

### 7.5. Conference Rebuttal

Carefully read the official rebuttal instructions, e.g., the [ICCV2021
rebuttal instructions](http://iccv2021.thecvf.com/node/4#rebuttal-instructions),
and fetch the template. Then extract the questions from the reviews, and answer
them one by one.

TODO: key points for writing a rebuttal.

Don't always assume the reviewers are in good faith if you feel some reviewer
response strange. Always be prepared for the
worst case and the ensuing implications, say, when the reviewer is somehow
hostile or irresponsible. Whether or not such reviewer will devastate the
reputation of the research community, for oneself the most important thing is
happiness, as almost nothing can be done to fight against injustice or fate.
Reaching your family for support might be a good idea at this point.

References:

[1] https://www.zhihu.com/question/32055996

[2] https://zhuanlan.zhihu.com/p/104298923

[3] https://blog.csdn.net/Ema1997/article/details/107103487

### 7.6. Journal Response

### 7.7. Slides and Poster

## 8. A Tiny Bit on Art

Reference material: [how to draw ugly diagrams?](assets/ugly-diagram.pdf) [(svg source)](assets/ugly-diagram.svg)

Color, Shapes, Lines, Layout, Fonts

## A. Python Proficiency

### A.1. Proficiency

I'd like the emphasize again that the [python official tutorial](https://docs.python.org/3/tutorial/index.html) is one of the best (free-of-charge) learning materials.

Here I have some additional questions and hints on python programming.
Note, please make sure that you can instantly verify your programming idea
with `ipython`, and learn programming in an interactive way.

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

### A.9. Python Library Recommendation

Some very useful python libraries.

1. ipython3 (friendly REPL)
2. multiprocess / joblib (paralellization)
3. numba (jit for acceleration)
4. pandas (XLSX in python)
5. tqdm (progress bar + timer)

## B. Editors and IDEs

vim 

emacs

vscode

pycharm

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

1. Print image in a text-based remote shell: `catimg` and `chafa`.

2. Composing latex document (including Table) very quickly: `lyx`.

3. Vectorized graph editing: `inkscape`.

4. Bitmap editing: `gimp`.

## Z. References

[Z1] A collection of guides to successful scientific communication: https://mitcommlab.mit.edu/eecs/use-the-commkit/

[Z2] Ian Goodfellow, et al., deep learning.
