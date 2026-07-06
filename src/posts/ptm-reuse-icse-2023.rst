:orphan:
:blogpost: true
:date: May 14, 2023
:category: Blog Post, Artificial Intelligence, Software Engineering
:tags: Pre-Trained Models, Hugging Face, Empirical Study, ICSE
:nocomments:

Pre-Trained Model Reuse in Hugging Face: An Empirical Study (ICSE 2023)
=======================================================================

This paper was led by **Wenxin Jiang**, a PhD student at Purdue University working with **James C. Davis**.
I am one of the key leaders of this research project, contributing to the study design, analysis, and framing.
The work appeared at **ICSE 2023**, the flagship conference in software engineering.

Abstract / Summary
------------------

We conducted a large-scale empirical study of how developers reuse pre-trained models (PTMs) from the Hugging Face registry.
Hugging Face hosts hundreds of thousands of models, and reusing them has become standard practice in machine learning pipelines.
But how developers actually select and use these models had not been studied systematically.
We mined the registry and downstream repositories to answer that question.

Background
----------

Pre-trained models are now a central building block in applied machine learning.
Rather than training from scratch, developers download a model trained on a large dataset and adapt it for their task.
Hugging Face is the dominant platform for this, hosting models across NLP, vision, audio, and more.
Despite the scale of this ecosystem, there was almost no empirical understanding of reuse behavior: which models get used, how they are documented, and whether developers evaluate fit before adopting a model.

Key Contributions
-----------------

* A large-scale mining study of PTM reuse across Hugging Face and downstream GitHub repositories.
* Evidence that model reuse is widespread but largely undisciplined: most developers select models without systematic evaluation of task fit.
* A characterization of documentation quality across the registry, showing widespread inconsistency in model cards.
* A foundation for future work on the pre-trained model supply chain as a software engineering concern.

Findings
--------

Reuse is common, but the decision process is opaque.
Most consumers pick models based on name, download count, or informal search — not on documented task compatibility or benchmark performance.
Model cards, which are meant to explain what a model does and how it was trained, vary enormously in completeness.
Many popular models have minimal documentation despite high usage.

This matters because PTMs are increasingly embedded in production systems.
If a model is poorly understood or misapplied, downstream software inherits that risk.

Key Take-Aways
--------------

The pre-trained model ecosystem has grown faster than the engineering practices around it.
This paper establishes an empirical baseline for what reuse actually looks like today and raises the question of what better practice would require — better documentation standards, tooling for evaluating fit, and community norms around model governance.

Citation
~~~~~~~~

DOI: https://doi.org/10.1109/ICSE48619.2023.00074

Jiang, Wenxin, Nicholas Synovic, Matt Hyatt, Thomas R. Schorlemmer, Rohan Sethi, Yung-Hsiang Lu, George K. Thiruvathukal, and James C. Davis. *An Empirical Study of Pre-Trained Model Reuse in the Hugging Face Deep Learning Model Registry*. Proceedings of the 45th International Conference on Software Engineering (ICSE), 2023, pp. 2463–2475.

.. code-block:: bibtex

   @inproceedings{jiang_empirical_2023,
     author    = {Jiang, Wenxin and Synovic, Nicholas and Hyatt, Matt and Schorlemmer, Thomas R. and Sethi, Rohan and Lu, Yung-Hsiang and Thiruvathukal, George K. and Davis, James C.},
     title     = {An empirical study of pre-trained model reuse in the {Hugging Face} deep learning model registry},
     booktitle = {Proceedings of the 45th International Conference on Software Engineering (ICSE)},
     year      = {2023},
     pages     = {2463--2475},
     doi       = {10.1109/ICSE48619.2023.00074},
     url       = {https://doi.org/10.1109/ICSE48619.2023.00074}
   }
