:blogpost: true
:date: October 12, 2024
:category: Blog Post
:tags: Software Engineering, Artificial Intelligence, 10-12-2024
:nocomments:

LLMs for Energy-Efficient Code: Emerging Results and Future Directions (2024)
==============================================================================

This post covers emerging results from a collaboration led by **Huiyun Peng** and **Akhil Gupte** (Purdue University), with **Nicholas J. Eliopoulos** and other collaborators including myself as external supervisor.
The work appears as an arXiv preprint (arXiv:2410.09241) and represents an active research direction in our group.

Large language models are increasingly used to generate and optimize code, but their impact on software energy efficiency is poorly understood.
This paper presents initial empirical results showing that LLM-generated code is not automatically energy-efficient — and in some cases introduces significant overhead — but that targeted prompting strategies and fine-tuning can close the gap.

The broader ambition is to make energy efficiency a first-class concern in AI-assisted software development, treating power consumption alongside correctness and performance.
This work sits at the intersection of green computing and software engineering, and we see it as a foundation for future tooling and benchmarks.

Citation
~~~~~~~~

Peng, H., Gupte, A., Eliopoulos, N. J., Ho, C. C., Mantri, R., Deng, L., Jiang, W., Thiruvathukal, G. K., Davis, J. C., & Lu, Y.-H. (2024). Large language models for energy-efficient code: Emerging results and future directions. *arXiv:2410.09241*. https://arxiv.org/abs/2410.09241

.. code-block:: bibtex

   @misc{peng_llm_energycode_2024,
     author        = {Peng, Huiyun and Gupte, Akhil and Eliopoulos, Nicholas J. and Ho, Chi-Chang and Mantri, Rohan and Deng, Leyong and Jiang, Wenxin and Thiruvathukal, George K. and Davis, James C. and Lu, Yung-Hsiang},
     title         = {Large language models for energy-efficient code: {Emerging} results and future directions},
     year          = {2024},
     eprint        = {2410.09241},
     archivePrefix = {arXiv},
     primaryClass  = {cs.SE},
     url           = {https://arxiv.org/abs/2410.09241}
   }
