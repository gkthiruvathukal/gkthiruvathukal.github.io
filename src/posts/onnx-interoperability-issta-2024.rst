:blogpost: true
:date: September 16, 2024
:category: Blog Post
:tags: Software Engineering, Artificial Intelligence, 09-16-2024
:nocomments:

When ONNX Converters Fail: Interoperability Risks in Deep Learning (ISSTA 2024)
================================================================================

This paper was led by **Purvish Jajal** and **Wenxin Jiang** (Purdue University, working with **James C. Davis** and **Yung-Hsiang Lu**).
I am one of the key leaders of this research project.
The work appeared at **ISSTA 2024** (ACM International Symposium on Software Testing and Analysis).

Abstract / Summary
------------------

ONNX is the most widely used standard for exchanging deep learning models across frameworks — converting a PyTorch model to TensorFlow, for example, or deploying it to a runtime like ONNX Runtime.
This paper studies how reliable that conversion process actually is.
We surveyed practitioners about their experiences and systematically tested ONNX converter tools, cataloging the failures that occur and why.

Background
----------

Interoperability in deep learning is hard.
Frameworks like PyTorch, TensorFlow, and JAX each have their own model representations, and the ecosystem depends on conversion tools to move models between them.
ONNX was designed to solve this — a common intermediate format that any framework can export to and import from.
In practice, the conversion process is fragile, and failures are common but poorly understood.
There was no systematic study of where and why these conversions break.

Key Contributions
-----------------

* A user survey of practitioners documenting real-world experiences with ONNX conversion failures.
* A systematic testing study of ONNX converter tools, cataloging failure modes by type and frequency.
* A taxonomy of conversion failures: operator coverage gaps, silent numeric errors, shape inference errors, and opaque error messages.
* Concrete recommendations for tool developers and practitioners on where the ecosystem needs improvement.

Findings
--------

Conversion failures are common and often subtle.
Operators that exist in one framework may have no ONNX equivalent, or the ONNX version behaves differently in edge cases.
Silent numeric errors — where conversion succeeds but model outputs differ from the original — are particularly dangerous because they do not trigger any warning.
Many practitioners reported abandoning ONNX conversion entirely after repeated failures, falling back to framework-specific deployment paths.

Key Take-Aways
--------------

The interoperability promise of ONNX does not match its everyday reliability.
For practitioners, this means conversion should always be validated with test cases that compare outputs numerically, not just checked for syntactic success.
For the research and tooling community, this paper identifies the specific failure categories that need targeted investment — better operator coverage, clearer error messages, and automated regression testing for converters.

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
