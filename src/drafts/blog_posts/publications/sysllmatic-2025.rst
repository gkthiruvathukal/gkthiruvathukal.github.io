:blogpost: true
:date: June 2, 2025
:category: Blog Post
:tags: Software Engineering, Artificial Intelligence, 06-02-2025
:nocomments:

SysLLMatic: Large Language Models as Software System Optimizers (2025)
=======================================================================

This post highlights **SysLLMatic**, a project led by **Huiyun Peng** (Purdue University), with contributions from **Akhil Gupte**, **Ryan Hasler**, **Nicholas J. Eliopoulos**, and other collaborators, including myself as external supervisor.
The work is available as arXiv:2506.01249.

Software systems optimization — tuning parameters like thread counts, buffer sizes, and scheduler settings — is typically done by experienced engineers through trial and error.
SysLLMatic investigates whether large language models can take on this role: given a system description and performance objective, can an LLM reason about configuration options and propose effective settings?

The initial results are encouraging: LLMs with access to system documentation can outperform random search on several standard optimization benchmarks, and their reasoning traces expose which documentation gaps most hamper performance.
This points toward a future where LLMs serve as interactive optimization assistants for systems software, not just code generation tools.

Citation
~~~~~~~~

Peng, H., Gupte, A., Hasler, R., Eliopoulos, N. J., Ho, C. C., Mantri, R., Deng, L., Thiruvathukal, G. K., Davis, J. C., & Lu, Y.-H. (2025). SysLLMatic: Large language models are software system optimizers. *arXiv:2506.01249*. https://arxiv.org/abs/2506.01249

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
