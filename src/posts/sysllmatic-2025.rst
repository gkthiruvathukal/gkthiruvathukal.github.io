:orphan:
:blogpost: true
:date: June 2, 2025
:category: Blog Post, Artificial Intelligence, Software Engineering
:tags: Large Language Models, Performance Optimization, Systems Configuration, arXiv
:nocomments:

SysLLMatic: Large Language Models as Software System Optimizers (2025)
=======================================================================

This paper was led by **Huiyun Peng** and **Akhil Gupte** (Purdue University), working with **James C. Davis**, **Yung-Hsiang Lu**, and others including **Ryan Hasler** and **Nicholas J. Eliopoulos**.
I am one of the key leaders of this research project.
The work is available as an arXiv preprint (arXiv:2506.01249).

Abstract / Summary
------------------

Software systems performance depends heavily on configuration: thread pool sizes, buffer limits, cache policies, scheduler parameters.
Getting these right typically requires deep expertise and iterative experimentation.
SysLLMatic investigates whether large language models can assist with this task — given a system description and a performance objective, can an LLM reason about configuration options and suggest good settings?
The paper presents a framework and early results showing that LLMs can meaningfully contribute to systems optimization when given appropriate context.

Background
----------

Systems performance tuning is an expert activity.
The search space of configurations is large, the interactions between parameters are nonlinear, and the right settings depend on workload characteristics that change over time.
Existing automated approaches — Bayesian optimization, evolutionary search — work but require many evaluation runs and do not generalize across systems.
LLMs have shown surprising capability at reasoning about code and systems behavior, which raises the question of whether they can accelerate or replace parts of the tuning loop.

Key Contributions
-----------------

* **SysLLMatic**, a framework for using LLMs to propose and iterate on system configuration settings given a performance objective.
* An evaluation across multiple software systems and workloads, comparing LLM-guided tuning against baselines including random search and Bayesian optimization.
* Analysis of LLM reasoning traces to identify which types of system knowledge help and where documentation gaps limit performance.
* A characterization of where LLMs add value in the tuning loop and where they do not.

Findings
--------

LLMs with access to system documentation can outperform random search on several benchmarks and match Bayesian optimization in some settings, with far fewer evaluation runs.
When LLMs fail, it is often because system documentation is incomplete or misleading about the effect of a parameter.
The reasoning traces produced by LLMs are useful in themselves: they surface which configuration options the model considers important and which documentation gaps prevent confident recommendations.

Key Take-Aways
--------------

LLMs can serve as practical assistants for software systems optimization, particularly in the early exploration phase where an expert would otherwise need to read documentation and form hypotheses manually.
They are not a replacement for systematic search, but they reduce the number of evaluations needed to find a good starting configuration.
This work also highlights that better systems documentation — not just more capable models — is a key lever for improving LLM-assisted tuning.

Citation
~~~~~~~~

arXiv: https://arxiv.org/abs/2506.01249

Peng, Huiyun, Akhil Gupte, Ryan Hasler, Nicholas J. Eliopoulos, Chi-Chang Ho, Rohan Mantri, Leyong Deng, George K. Thiruvathukal, James C. Davis, and Yung-Hsiang Lu. *SysLLMatic: Large Language Models Are Software System Optimizers*. arXiv:2506.01249, 2025.

.. code-block:: bibtex

   @misc{peng_sysllmatic_2025,
     author        = {Peng, Huiyun and Gupte, Akhil and Hasler, Ryan and Eliopoulos, Nicholas J. and Ho, Chi-Chang and Mantri, Rohan and Deng, Leyong and Thiruvathukal, George K. and Davis, James C. and Lu, Yung-Hsiang},
     title         = {{SysLLMatic}: Large language models are software system optimizers},
     year          = {2025},
     eprint        = {2506.01249},
     archivePrefix = {arXiv},
     primaryClass  = {cs.SE},
     url           = {https://arxiv.org/abs/2506.01249}
   }
