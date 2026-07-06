:orphan:
:blogpost: true
:date: April 15, 2024
:category: Blog Post, Artificial Intelligence, Software Engineering
:tags: Pre-Trained Models, Hugging Face, Mining Software Repositories, Software Supply Chain Security, MSR
:nocomments:

PeaTMOSS: Mining Pre-Trained Models in Open-Source Software (MSR 2024)
=======================================================================

This paper was led by **Wenxin Jiang** (Purdue University, working with **James C. Davis**).
I am one of the key leaders of this research project and contributed to its design and analysis.
The work appeared at **MSR 2024** (International Conference on Mining Software Repositories).

Abstract / Summary
------------------

PeaTMOSS is a dataset that links pre-trained models on Hugging Face to the open-source GitHub projects that use them.
We built this dataset to enable researchers to study the pre-trained model supply chain at scale — tracing how models flow from registries into downstream software.
The paper presents the dataset and an initial analysis of reuse patterns, licensing, and provenance across the ecosystem.

Background
----------

Mining software repositories is a well-established method for understanding how software evolves and how developers work.
But the rise of pre-trained models as reusable artifacts has created a new kind of dependency that existing tools do not capture.
A project on GitHub may depend on dozens of PTMs without any formal dependency declaration — the model is just downloaded at runtime from Hugging Face.
PeaTMOSS is designed to make those invisible dependencies visible.

Key Contributions
-----------------

* A large-scale dataset linking Hugging Face model cards to downstream open-source repositories on GitHub.
* Tooling to discover PTM usage in source code, configuration files, and scripts.
* An initial analysis of reuse concentration, license compatibility, and provenance completeness.
* A publicly available resource for the research community studying AI software ecosystems.

Findings
--------

PTM reuse is heavily concentrated: a small number of models accounts for the large majority of downstream usage, while most models are rarely or never used outside of their original context.
License information is frequently missing or incompatible with downstream project licenses — a practical risk that developers are largely unaware of.
Provenance (information about training data, lineage, and modifications) is sparse even for widely reused models.

Key Take-Aways
--------------

PeaTMOSS gives researchers a concrete foundation for studying PTMs as supply chain artifacts rather than standalone tools.
The immediate finding — that popular models often lack the documentation needed for responsible reuse — reinforces the need for better standards around model publishing.
The dataset is open and intended to support follow-on work on licensing, security, and reproducibility in the AI ecosystem.

Citation
~~~~~~~~

DOI: https://doi.org/10.1145/3643991.3644886

Jiang, Wenxin, Jerin Yasmin, Jason Jones, Nicholas Synovic, Julian Kuo, Nathan Bielanski, Yuan Tian, George K. Thiruvathukal, and James C. Davis. *PeaTMOSS: A Dataset and Initial Analysis of Pre-Trained Models in Open-Source Software*. Proceedings of the 21st International Conference on Mining Software Repositories (MSR), 2024.

.. code-block:: bibtex

   @inproceedings{jiang_peatmoss_2024,
     author    = {Jiang, Wenxin and Yasmin, Jerin and Jones, Jason and Synovic, Nicholas and Kuo, Julian and Bielanski, Nathan and Tian, Yuan and Thiruvathukal, George K. and Davis, James C.},
     title     = {{PeaTMOSS}: A dataset and initial analysis of pre-trained models in open-source software},
     booktitle = {Proceedings of the 21st International Conference on Mining Software Repositories (MSR)},
     year      = {2024},
     doi       = {10.1145/3643991.3644886},
     url       = {https://doi.org/10.1145/3643991.3644886}
   }
