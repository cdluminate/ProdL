ProdL: Productive Deep Learner (WIP)
===

Copyright (C) 2020-2021, Mo Zhou `<cdluminate AT gmail.com>`

This document is released under the [GNU Free Documentation License (GFDL-1.3)
](https://www.gnu.org/licenses/fdl-1.3.html) license.

*ProdL* is a personal documentation project for collecting memos and hints
that may help one boost their productivity in Deep Learning study.
Since the author is more or less an old-school UNIX/Linux proponent,
you may sense a strong odor of UNIX in this document.

## 0. Prerequisites

In this section, I shall point out some keywords for background knowledge
that would greatly help you throughout the journey on deep learning.

### 0.1. Critical Instinct

Things may get much easier with the following instincts.

* Be aware of what you are doing, and what you intend to do.

* Carefully read and try to understand the output of programs.

* [Ask questions in a smart way.](http://www.catb.org/~esr/faqs/smart-questions.html)

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

### 0.4. Computer Organization

Computer organization [[1]](https://www.coursera.org/learn/jisuanji-zucheng)
[[2]](https://www.geeksforgeeks.org/computer-organization-and-architecture-tutorials/)
[[3]](https://csapp.cs.cmu.edu/)
is critical for you to correctly understand things that harms the performance
of your program. It is also (partly) helpful for you to avoid writting prototype
code without obvious performance flaw.

### 0.5. Operating System and POSIX

### 0.6. Fundamental Utilities

Including coreutils, findutils, etc.

References:

[1] Missing Course of Your CS Education: https://missing.csail.mit.edu/

### 0.7. Remote Access

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

## 6. Paper Reading

## 7. Organizing Preliminary Draft

### 7.1. LaTeX Typesetting

## 8. A Tiny Bit on Art

Reference material: [how to draw ugly diagrams?](assets/ugly-diagram.pdf) [(svg source)](assets/ugly-diagram.svg)

Color, Shapes, Lines, Layout, Fonts

## Misc References

[1] A collection of guides to successful scientific communication: https://mitcommlab.mit.edu/eecs/use-the-commkit/

## A. Algorithms

## B. Python Libraries

Some very useful python libraries.

## C. Editors and IDEs
