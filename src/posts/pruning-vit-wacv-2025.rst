:blogpost: true
:date: February 28, 2025
:category: Blog Post
:tags: Artificial Intelligence, 02-28-2025
:nocomments:

Pruning One More Token Is Enough: Efficient Vision Transformers on the Edge (WACV 2025)
========================================================================================

This post highlights work led by **Nicholas J. Eliopoulos** (Purdue University), co-supervised by **James C. Davis**, **Guoqing Liu**, **Yung-Hsiang Lu**, and myself.
The paper appeared at **WACV 2025** (IEEE/CVF Winter Conference on Applications of Computer Vision).

Vision Transformers (ViTs) are powerful but expensive — too expensive for most edge devices.
Token pruning removes less-informative patches from the input sequence to reduce computation, but prior work treats the latency savings as roughly linear in the number of tokens removed.
This paper reveals a non-linearity: hardware-level batching means that pruning a small number of additional tokens can yield disproportionate latency improvements at no additional accuracy cost.

By exploiting this latency-workload non-linearity in the pruning decision, our approach achieves competitive accuracy-latency tradeoffs on standard benchmarks without additional training.
The result matters for anyone deploying ViTs on devices where memory bandwidth and compute are tightly constrained.

Citation
~~~~~~~~

Eliopoulos, N. J., Jajal, P., Davis, J. C., Liu, G., Thiruvathukal, G. K., & Lu, Y.-H. (2025). Pruning one more token is enough: Leveraging latency-workload non-linearities for vision transformers on the edge. *Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)*.

.. code-block:: bibtex

   @inproceedings{eliopoulos_pruning_2025,
     author    = {Eliopoulos, Nicholas J. and Jajal, Purvish and Davis, James C. and Liu, Guoqing and Thiruvathukal, George K. and Lu, Yung-Hsiang},
     title     = {Pruning one more token is enough: {Leveraging} latency-workload non-linearities for vision transformers on the edge},
     booktitle = {Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)},
     year      = {2025}
   }
