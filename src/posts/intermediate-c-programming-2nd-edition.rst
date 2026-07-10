:orphan:
:blogpost: true
:date: February 9, 2024
:category: Blog Post, Software Engineering, Books
:tags: C Programming, Software Engineering Education, Version Control, Debugging, Routledge
:nocomments:

Intermediate C Programming, 2nd Edition
=========================================

I'm happy to share the second edition of **Intermediate C Programming**, co-authored with **Yung-Hsiang Lu** (Purdue University) and published by **Routledge / Taylor & Francis Group**.
This edition expands the software engineering coverage that much of my own teaching in the Software Systems Laboratory (COMP 310) draws on.

What the Book Is About
----------------------

The C programming language remains vital to modern topics such as cybersecurity, computer systems, computer engineering, and scientific computing — but most introductory courses stop well short of what it takes to write real, professional-grade C.
This book is meant as the bridge: it takes students from short, correct-enough programs to code that can survive debugging, testing, collaboration, and reuse.

What's Inside
-------------

The book is organized into four parts, 24 chapters in total:

* **Part I — Storage: Memory and File.** Program execution, stack memory, debugging techniques, pointers, multi-file programs, strings, heap memory, file I/O, and security considerations.
* **Part II — Recursion.** Recursive problem solving through examples like ball selection, the Tower of Hanoi, integer partitions, binary search, and quicksort.
* **Part III — Structure.** Custom data types, objects, linked lists, and binary search trees.
* **Part IV — Applications.** Real-world problems: maze navigation, Sudoku solving, image processing, and Huffman compression.

New in this second edition is expanded software engineering material: version control with git and GitHub, unit testing with the Google Test framework, and threading with POSIX threads — alongside the existing use of standard Linux tools like ``ddd`` and ``valgrind`` for debugging.

Why It Matters
---------------

Most C textbooks either stay introductory or jump straight into advanced systems topics.
This book is deliberately aimed at the space in between: the practices — clean code, testing, version control, debugging discipline — that turn a student who can write a program into an engineer who can write software other people can depend on.
It's also the textbook backbone for the examples in my `systems-code-examples <https://github.com/gkthiruvathukal/systems-code-examples>`__ repository, so readers of the book and users of that repo are working from the same foundation.

Citation
~~~~~~~~

Link: https://www.routledge.com/Intermediate-C-Programming/Lu-Thiruvathukal/p/book/9781032189819

Lu, Yung-Hsiang, and George K. Thiruvathukal. *Intermediate C Programming*. 2nd ed., Routledge, 2024.

.. code-block:: bibtex

   @book{lu_intermediate_2024,
     author    = {Lu, Yung-Hsiang and Thiruvathukal, George K.},
     title     = {Intermediate C Programming},
     edition   = {2nd},
     publisher = {Routledge},
     year      = {2024},
     isbn      = {9781032189819}
   }
