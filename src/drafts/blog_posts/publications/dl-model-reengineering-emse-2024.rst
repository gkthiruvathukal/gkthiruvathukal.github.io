:blogpost: true
:date: January 30, 2024
:category: Blog Post
:tags: Software Engineering, Artificial Intelligence, 01-30-2024
:nocomments:

Deep Learning Model Reengineering: Challenges and Practices (EMSE 2024)
========================================================================

This post covers a case study led by **Wenxin Jiang** (Purdue University, supervised by **James C. Davis**), with contributions from **Vishnu Banna**, **Nikhil Vivek**, **Aditya Goel**, **Nicholas Synovic**, and myself as a named co-author.
The work appeared in the **Empirical Software Engineering** journal.

Reengineering deep learning models — adapting an existing model to a new task, framework, or deployment target — is increasingly common, but the engineering practices around it are poorly understood.
This case study follows teams working in the computer vision domain through model reengineering efforts and surfaces recurring challenges: insufficient documentation of training procedures, undisclosed hyperparameter choices, and the difficulty of reproducing baseline results from published papers.

The findings argue that model reengineering deserves recognition as a first-class software engineering activity, with its own lifecycle, tools, and best practices — rather than being treated as a minor downstream concern.

Citation
~~~~~~~~

Jiang, W., Banna, V., Vivek, N., Goel, A., Synovic, N., Thiruvathukal, G. K., & Davis, J. C. (2024). Challenges and practices of deep learning model reengineering: A case study on computer vision. *Empirical Software Engineering*. https://doi.org/10.1007/s10664-023-10415-3

.. code-block:: bibtex

   @article{jiang_challenges_2024,
     author  = {Jiang, Wenxin and Banna, Vishnu and Vivek, Nikhil and Goel, Aditya and Synovic, Nicholas and Thiruvathukal, George K. and Davis, James C.},
     title   = {Challenges and practices of deep learning model reengineering: {A} case study on computer vision},
     journal = {Empirical Software Engineering},
     year    = {2024},
     doi     = {10.1007/s10664-023-10415-3},
     url     = {https://doi.org/10.1007/s10664-023-10415-3}
   }
