:orphan:
:blogpost: true
:date: February 28, 2025
:category: Blog Post, Artificial Intelligence
:tags: Vision Transformers, Model Pruning, Edge Computing, Computer Vision, WACV
:nocomments:

Pruning One More Token Is Enough: Efficient Vision Transformers on the Edge (WACV 2025)
========================================================================================

This paper was led by **Nicholas J. Eliopoulos** (Purdue University), working with **James C. Davis**, **Guoqing Liu**, and **Yung-Hsiang Lu**.
I am one of the key leaders of this research project.
The work appeared at **WACV 2025** (IEEE/CVF Winter Conference on Applications of Computer Vision).

Abstract / Summary
------------------

Vision Transformers (ViTs) achieve strong accuracy on image tasks but are computationally expensive for edge deployment.
Token pruning — dropping less-informative image patches from the input sequence — is a standard way to reduce that cost.
This paper shows that the relationship between tokens pruned and latency saved is not linear: due to hardware-level batching effects, pruning a few extra tokens at the right threshold can yield a disproportionate latency reduction at no additional accuracy cost.

Background
----------

Deploying vision models on edge devices — cameras, mobile phones, embedded systems — requires balancing accuracy against compute and memory constraints.
ViTs are attractive for their strong performance, but their self-attention mechanism scales quadratically with input length.
Token pruning addresses this by removing uninformative patches early in the network, reducing the sequence length that attention operates on.
Prior work on token pruning typically models latency savings as proportional to the number of tokens removed.
This assumption turns out to be incomplete.

Key Contributions
-----------------

* Identification of a latency-workload non-linearity in ViT inference on edge hardware caused by batch processing thresholds.
* A pruning strategy that exploits this non-linearity to achieve better latency reduction than uniformly distributed pruning at the same token budget.
* Empirical evaluation on standard vision benchmarks showing competitive accuracy-latency tradeoffs without retraining.
* Analysis of how this effect varies across hardware platforms and batch sizes.

Findings
--------

On the hardware platforms tested, token count interacts with batch processing in a step-wise manner.
Pruning to just below a batch boundary yields only modest latency savings; pruning one more token — crossing the threshold — triggers a larger reduction.
By accounting for this in the pruning decision, the approach achieves better real-world speed with the same or better accuracy compared to baselines that ignore hardware structure.

Key Take-Aways
--------------

Efficient inference on real hardware requires thinking about the hardware, not just the model.
A pruning strategy optimized in isolation from deployment constraints will leave performance on the table.
This work is a practical example of how hardware-aware design can yield meaningful gains without any change to the underlying model architecture or training procedure.

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
