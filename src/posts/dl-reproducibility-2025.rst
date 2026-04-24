:blogpost: true
:date: May 6, 2025
:category: Blog Post
:tags: Software Engineering, Artificial Intelligence, 05-06-2025
:nocomments:

Improving Deep Learning Reproducibility: A Case Study Investigation (2025)
===========================================================================

This post covers a case study led by **Nadia Ravi** and **Aditya Goel** (Purdue University), co-authored with **James C. Davis** and myself (**George K. Thiruvathukal**) as senior co-author.
The paper is available as arXiv:2505.03165 and represents our group's ongoing commitment to making research software engineering more rigorous.

Reproducibility is a well-known challenge in deep learning, but most prior work focuses on statistical reproducibility across runs.
This paper digs into a different problem: can researchers actually reproduce a published result from the artifacts provided?
Through a structured case study of publicly available deep learning repositories, we document the specific failure modes — missing dependencies, undocumented hyperparameters, hardware assumptions — that prevent reproduction even when code is nominally available.

The paper offers concrete guidance for practitioners and reviewers and contributes to the broader movement toward artifact evaluation standards in machine learning conferences and journals.

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
