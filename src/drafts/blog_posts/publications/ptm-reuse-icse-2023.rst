:blogpost: true
:date: May 14, 2023
:category: Blog Post
:tags: Software Engineering, Artificial Intelligence, 05-14-2023
:nocomments:

Pre-Trained Model Reuse in Hugging Face: An Empirical Study (ICSE 2023)
=======================================================================

This post highlights work led by **Wenxin Jiang**, a PhD student at Purdue University advised by **James C. Davis**, with whom I collaborate closely.
I served as an external supervisor and co-author on this project.
The paper appeared at **ICSE 2023**, one of the flagship venues in software engineering.

The study examines how developers reuse pre-trained models (PTMs) from the Hugging Face registry.
Through a large-scale empirical analysis, we found that model reuse is widespread but poorly understood: most consumers make no systematic effort to evaluate whether a PTM actually fits their task, and documentation is inconsistent across thousands of models.

This work set the foundation for a multi-year research agenda around the "pre-trained model supply chain" — understanding how PTMs are published, discovered, and reused, and what engineering disciplines need to evolve to support that ecosystem responsibly.

Citation
~~~~~~~~

Jiang, W., Synovic, N., Hyatt, M., Schorlemmer, T. R., Sethi, R., Lu, Y.-H., Thiruvathukal, G. K., & Davis, J. C. (2023). An empirical study of pre-trained model reuse in the Hugging Face deep learning model registry. *Proceedings of the 45th International Conference on Software Engineering (ICSE)*, pp. 2463–2475. https://doi.org/10.1109/ICSE48619.2023.00074

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
