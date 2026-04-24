:blogpost: true
:date: April 15, 2024
:category: Blog Post
:tags: Software Engineering, Artificial Intelligence, 04-15-2024
:nocomments:

PeaTMOSS: Mining Pre-Trained Models in Open-Source Software (MSR 2024)
=======================================================================

This post highlights **PeaTMOSS**, a dataset and analysis led by **Wenxin Jiang** (Purdue University, advised by **James C. Davis**).
I contributed as an external collaborator and committee member.
The work appeared at **MSR 2024** (International Conference on Mining Software Repositories).

PeaTMOSS is a large-scale dataset that captures how pre-trained deep learning models from Hugging Face are used across open-source GitHub repositories.
The dataset links model cards to downstream projects, enabling researchers to study dependency relationships in the AI supply chain at scale.

The initial analysis reveals that PTM reuse is heavily concentrated: a small fraction of models accounts for the vast majority of downstream usage, and many popular models lack basic provenance or licensing information.
PeaTMOSS is openly available to the research community and serves as a foundation for studying how PTMs propagate through software ecosystems.

Citation
~~~~~~~~

Jiang, W., Yasmin, J., Jones, J., Synovic, N., Kuo, J., Bielanski, N., Tian, Y., Thiruvathukal, G. K., & Davis, J. C. (2024). PeaTMOSS: A dataset and initial analysis of pre-trained models in open-source software. *Proceedings of the 21st International Conference on Mining Software Repositories (MSR)*. https://doi.org/10.1145/3643991.3644886

.. code-block:: bibtex

   @inproceedings{jiang_peatmoss_2024,
     author    = {Jiang, Wenxin and Yasmin, Jerin and Jones, Jason and Synovic, Nicholas and Kuo, Julian and Bielanski, Nathan and Tian, Yuan and Thiruvathukal, George K. and Davis, James C.},
     title     = {{PeaTMOSS}: A dataset and initial analysis of pre-trained models in open-source software},
     booktitle = {Proceedings of the 21st International Conference on Mining Software Repositories (MSR)},
     year      = {2024},
     doi       = {10.1145/3643991.3644886},
     url       = {https://doi.org/10.1145/3643991.3644886}
   }
