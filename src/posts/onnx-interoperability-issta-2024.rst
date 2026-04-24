:blogpost: true
:date: September 16, 2024
:category: Blog Post
:tags: Software Engineering, Artificial Intelligence, 09-16-2024
:nocomments:

When ONNX Converters Fail: Interoperability Risks in Deep Learning (ISSTA 2024)
================================================================================

This post covers a user study and failure analysis led by **Purvish Jajal** and **Wenxin Jiang** (Purdue University, supervised by **James C. Davis**), with contributions from **Yung-Hsiang Lu** and myself as external collaborators.
The work appeared at **ISSTA 2024** (ACM International Symposium on Software Testing and Analysis).

ONNX is the de facto standard for exchanging deep learning models across frameworks.
But in practice, converting a model to ONNX — or from ONNX to another framework — is surprisingly fragile.
Our study surveyed practitioners, collected real-world failures, and systematically analyzed ONNX converter tools.
We found that operator coverage gaps, silent numeric errors, and opaque error messages are pervasive, and that practitioners frequently abandon conversion entirely when they hit a wall.

The findings point to a significant gap between the interoperability promise of ONNX and its everyday reliability, with concrete implications for how ML engineering toolchains should be tested and validated.

Citation
~~~~~~~~

Jajal, P., Jiang, W., Tewari, A., Kocinare, E., Woo, J., Sarraf, A., Lu, Y.-H., Thiruvathukal, G. K., & Davis, J. C. (2024). Interoperability in deep learning: A user survey and failure analysis of ONNX model converters. *Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA)*. https://doi.org/10.1145/3650212.3652133

.. code-block:: bibtex

   @inproceedings{jajal_interoperability_2024,
     author    = {Jajal, Purvish and Jiang, Wenxin and Tewari, Arav and Kocinare, Ece and Woo, Joseph and Sarraf, Anirudh and Lu, Yung-Hsiang and Thiruvathukal, George K. and Davis, James C.},
     title     = {Interoperability in deep learning: {A} user survey and failure analysis of {ONNX} model converters},
     booktitle = {Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA)},
     year      = {2024},
     doi       = {10.1145/3650212.3652133},
     url       = {https://doi.org/10.1145/3650212.3652133}
   }
