:blogpost: true
:date: January 30, 2024
:category: Blog Post
:tags: Software Engineering, Artificial Intelligence, 01-30-2024
:nocomments:

Deep Learning Model Reengineering: Challenges and Practices (EMSE 2024)
========================================================================

This paper was led by **Wenxin Jiang** (Purdue University, working with **James C. Davis**), with contributions from **Vishnu Banna**, **Nikhil Vivek**, **Aditya Goel**, and **Nicholas Synovic**.
I am one of the key leaders of this research project.
The work appeared in the **Empirical Software Engineering** journal.

Abstract / Summary
------------------

Reengineering a deep learning model — taking an existing model and adapting it for a new task, framework, or deployment target — is common practice, but the engineering challenges involved are poorly documented.
This paper uses a case study approach to study how teams in the computer vision domain carry out model reengineering in practice, what goes wrong, and what better practices might look like.

Background
----------

Software reengineering is a mature concept in traditional software engineering: you take existing code, understand it, and adapt or extend it for new requirements.
With deep learning, the same need arises — researchers reproduce published results, adapt models to new datasets, or port them to new frameworks — but the tooling, documentation, and community practices are far less mature.
Published papers often omit the implementation details needed to reproduce or adapt their results, and there is no established playbook for model reengineering.

Key Contributions
-----------------

* A case study of model reengineering efforts in computer vision, covering teams attempting to reproduce and adapt published models.
* A catalog of the specific challenges that arise: missing training details, undisclosed hyperparameters, unstated hardware requirements, and incompatible framework versions.
* Evidence that reproducing published baseline results is frequently a substantial effort, even when code is available.
* Recommendations for researchers, publishers, and tool developers on reducing reengineering costs.

Findings
--------

The most common failure points are not bugs in the reengineered code — they are missing information in the original publication.
Teams spent significant time reverse-engineering hyperparameter choices, tracking down compatible library versions, and reconstructing training pipelines from partial information.
When the original authors' code was available, it helped, but was rarely sufficient on its own.

Key Take-Aways
--------------

Model reengineering should be treated as a distinct and legitimate software engineering activity, not a minor detail of using published research.
Better artifact standards — requiring training configurations, environment specifications, and validation procedures alongside model weights — would substantially reduce the effort involved.
This paper provides an empirical basis for those recommendations.

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
