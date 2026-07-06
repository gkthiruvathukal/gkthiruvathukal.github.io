:orphan:
:blogpost: true
:date: March 1, 2024
:category: Blog Post, Artificial Intelligence, Security
:tags: Adversarial Attacks, Interpretability, Explainable AI, TIFS
:nocomments:

SingleAdv: Targeted Adversarial Attacks on Interpretable Deep Learning (IEEE TIFS 2024)
========================================================================================

This paper was led by **Elmurod Abdukhamidov** and **Mohammed Abuhamad** (Hanyang University, Korea), with **Hyoungshick Kim** and **Tamer Abuhmed** as co-leads.
I am one of the key leaders of this research project, contributing to the threat modeling and evaluation design.
The work appeared in **IEEE Transactions on Information Forensics and Security**.

Abstract / Summary
------------------

Interpretable deep learning systems pair their predictions with explanations — saliency maps, attention weights, or other attribution methods — so that users can understand why a model made a particular decision.
This paper introduces **SingleAdv**, an adversarial attack designed specifically for these systems.
The attack causes the model to misclassify inputs from a single targeted class while leaving all other classes unaffected, and crucially, while keeping the explanation output looking normal.

Background
----------

Adversarial attacks on deep learning models are well studied.
But most prior work targets standard classifiers where only the prediction matters.
Interpretable systems present a different problem: they are used in settings where trust is important — medical imaging, content moderation, financial decisions — and users rely on explanations to verify that the model is working correctly.
If an adversary can subvert the model while leaving the explanation intact, the user has no way to detect the attack through the interface designed to provide transparency.

Key Contributions
-----------------

* **SingleAdv**, the first adversarial attack targeting a single class within an interpretable deep learning system.
* A demonstration that the attack preserves the visual appearance of explanations, defeating the transparency mechanism.
* A taxonomy of attack scenarios specific to interpretable systems, extending prior adversarial ML frameworks.
* Evaluation across multiple model architectures and explanation methods, showing the attack generalizes broadly.
* Discussion of detection strategies and their limitations.

Findings
--------

SingleAdv is effective across a range of architectures and explanation methods.
The attack requires only moderate perturbations to inputs, making it hard to detect through standard input monitoring.
Explanation outputs remain visually similar to those of an unattacked model, meaning that human reviewers relying on explanations would not notice the compromise.

Key Take-Aways
--------------

Explanation mechanisms do not provide security guarantees.
A system that looks interpretable can still be subverted in a targeted way, and the explanation output can be engineered to conceal that subversion.
This has direct implications for high-stakes deployments: interpretability tools increase user confidence, but that confidence is not warranted if the system has not been evaluated for adversarial robustness specifically in the interpretability setting.

Citation
~~~~~~~~

DOI: https://doi.org/10.1109/TIFS.2024.3355942

Abdukhamidov, Elmurod, Mohammed Abuhamad, George K. Thiruvathukal, Hyoungshick Kim, and Tamer Abuhmed. *SingleAdv: Single-Class Target-Specific Attack Against Interpretable Deep Learning Systems*. IEEE Transactions on Information Forensics and Security, 2024.

.. code-block:: bibtex

   @article{abdukhamidov_singleadv_2024,
     author  = {Abdukhamidov, Elmurod and Abuhamad, Mohammed and Thiruvathukal, George K. and Kim, Hyoungshick and Abuhmed, Tamer},
     title   = {{SingleAdv}: Single-class target-specific attack against interpretable deep learning systems},
     journal = {IEEE Transactions on Information Forensics and Security},
     year    = {2024},
     doi     = {10.1109/TIFS.2024.3355942},
     url     = {https://doi.org/10.1109/TIFS.2024.3355942}
   }
