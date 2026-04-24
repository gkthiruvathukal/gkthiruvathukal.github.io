:blogpost: true
:date: May 6, 2025
:category: Blog Post
:tags: Software Engineering, Artificial Intelligence, 05-06-2025
:nocomments:

Improving Deep Learning Reproducibility: A Case Study Investigation (2025)
===========================================================================

This paper was led by **Nadia Ravi** and **Aditya Goel** (Purdue University), working with **James C. Davis**.
I am one of the key leaders of this research project.
The work is available as an arXiv preprint (arXiv:2505.03165).

Abstract / Summary
------------------

Deep learning reproducibility is widely discussed but rarely studied concretely.
This paper asks a specific question: given a published deep learning paper and its associated artifacts, can a researcher actually reproduce the reported results?
Through a structured case study, we document where and why reproduction fails, even when code is nominally available, and offer guidance for researchers, reviewers, and venues.

Background
----------

Reproducibility in science means that an independent researcher, following a published method, should be able to obtain the same results.
In deep learning, this is harder than it sounds.
Models are sensitive to random seeds, framework versions, hardware, and undocumented training decisions.
Papers often report final numbers without providing the full configuration needed to reproduce them.
Artifact evaluation at conferences has improved the situation, but problems remain widespread.
Most prior work on DL reproducibility focuses on statistical variation across runs; this paper focuses on a more basic question: can you reproduce the result at all from what is provided?

Key Contributions
-----------------

* A structured case study methodology for evaluating deep learning reproducibility from published artifacts.
* A catalog of failure modes observed in practice: missing dependencies, incompatible library versions, undocumented hyperparameters, and implicit hardware assumptions.
* Evidence that code availability alone does not guarantee reproducibility.
* Practical recommendations for authors, reviewers, and artifact evaluation committees.

Findings
--------

Reproduction failures cluster around a small set of recurring problems.
Environment setup is the most common barrier: dependencies are pinned incompletely, or the code assumes a specific hardware configuration that is not stated.
Hyperparameters that affect final performance are sometimes omitted from both the paper and the released code, requiring guesswork.
When all of these are resolved, stochastic variation in training can still produce results that differ from reported numbers by a meaningful margin.

Key Take-Aways
--------------

Making code available is necessary but not sufficient for reproducibility.
What is needed is a more complete artifact: a pinned environment specification, explicit hyperparameter listings, hardware requirements, and a validation procedure that confirms the artifact produces results matching the paper.
This work supports the case for stronger artifact standards at ML venues and provides a concrete framework for evaluating whether those standards are being met.

Citation
~~~~~~~~

Ravi, N., Goel, A., Davis, J. C., & Thiruvathukal, G. K. (2025). Improving the reproducibility of deep learning software: An initial investigation through a case study analysis. *arXiv:2505.03165*. https://arxiv.org/abs/2505.03165

.. code-block:: bibtex

   @misc{ravi_reproducibility_2025,
     author        = {Ravi, Nadia and Goel, Aditya and Davis, James C. and Thiruvathukal, George K.},
     title         = {Improving the reproducibility of deep learning software: {An} initial investigation through a case study analysis},
     year          = {2025},
     eprint        = {2505.03165},
     archivePrefix = {arXiv},
     primaryClass  = {cs.SE},
     url           = {https://arxiv.org/abs/2505.03165}
   }
