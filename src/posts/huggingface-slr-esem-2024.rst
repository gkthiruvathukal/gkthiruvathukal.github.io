:orphan:
:blogpost: true
:date: October 24, 2024
:category: Blog Post, Artificial Intelligence, Software Engineering
:tags: Hugging Face, Pre-Trained Models, Systematic Literature Review, ESEM
:nocomments:

What Do We Know About Hugging Face? A Systematic Literature Review (ESEM 2024)
===============================================================================

This paper was led by **Jason Jones** and **Wenxin Jiang** (Purdue University, working with **James C. Davis**).
I am one of the key leaders of this research project and contributed to the analysis and synthesis.
The work appeared at **ESEM 2024** (ACM/IEEE International Symposium on Empirical Software Engineering and Measurement).

Abstract / Summary
------------------

Hugging Face has become the central platform for sharing and discovering pre-trained models, yet the research literature about it is scattered and uneven.
This paper conducts a systematic literature review of published work on Hugging Face, extracts qualitative claims from that literature, and then validates those claims quantitatively against data from the platform itself.
The goal is to give the research community a reliable, evidence-based picture of what we actually know.

Background
----------

As Hugging Face grew rapidly, so did papers studying it — but without coordination.
Papers made contradictory claims, studied different subsets of the platform, or drew conclusions from outdated snapshots.
A systematic review was needed to consolidate findings, identify where claims were supported by data and where they were speculation, and map the gaps where research is still thin.

Key Contributions
-----------------

* A systematic literature review covering empirical work on Hugging Face across software engineering, machine learning, and security venues.
* Extraction and categorization of qualitative claims from the literature.
* Quantitative validation of those claims against current platform data, distinguishing what holds up from what does not.
* A structured map of findings and an agenda for where future empirical work is most needed.

Findings
--------

Several commonly repeated claims in the literature do not hold up when tested against platform data at scale.
Model cards are widely described as a solution to documentation problems, but in practice the majority remain incomplete or are auto-generated with minimal content.
Reproducibility is cited as a concern in many papers, but few studies operationalize it concretely.
Governance and licensing receive little empirical attention despite being practically significant.

Key Take-Aways
--------------

The HF ecosystem is larger and more complex than most individual studies capture, and the research community has not yet converged on shared definitions or measurement approaches.
This review gives researchers a baseline to build from and highlights the areas — governance, licensing, reproducibility, security — where systematic empirical work is still lacking.

Citation
~~~~~~~~

DOI: https://doi.org/10.1145/3674805.3686678

Jones, Jason, Wenxin Jiang, Nicholas Synovic, George K. Thiruvathukal, and James C. Davis. *What Do We Know About Hugging Face? A Systematic Literature Review and Quantitative Validation of Qualitative Claims*. Proceedings of the 18th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM), 2024.

.. code-block:: bibtex

   @inproceedings{jones_huggingface_2024,
     author    = {Jones, Jason and Jiang, Wenxin and Synovic, Nicholas and Thiruvathukal, George K. and Davis, James C.},
     title     = {What do we know about {Hugging Face}? {A} systematic literature review and quantitative validation of qualitative claims},
     booktitle = {Proceedings of the 18th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)},
     year      = {2024},
     doi       = {10.1145/3674805.3686678},
     url       = {https://doi.org/10.1145/3674805.3686678}
   }
