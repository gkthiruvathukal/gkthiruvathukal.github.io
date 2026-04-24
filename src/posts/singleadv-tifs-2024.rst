:blogpost: true
:date: March 1, 2024
:category: Blog Post
:tags: Artificial Intelligence, 03-01-2024
:nocomments:

SingleAdv: Targeted Adversarial Attacks on Interpretable Deep Learning (IEEE TIFS 2024)
========================================================================================

This post covers work led by **Elmurod Abdukhamidov** and **Mohammed Abuhamad** (Hanyang University, Korea), with **Tamer Abuhmed** and myself (**George K. Thiruvathukal**) as co-authors.
I contributed to the threat modeling and evaluation framing for this collaboration.
The paper appeared in **IEEE Transactions on Information Forensics and Security**.

Interpretable AI systems — models that pair predictions with explanations — are increasingly used in high-stakes settings like medical imaging and content moderation.
This work demonstrates that such systems have a specific vulnerability: a single-class adversarial attack that causes misclassification for a targeted class while leaving other predictions intact, even as the model's explanation mechanism appears unaffected.

The result has practical significance: explanations can give users false confidence that a model is behaving correctly, when it has in fact been subverted for a specific class of inputs.
The paper proposes a taxonomy of attacks and defenses specific to this interpretability context.

Citation
~~~~~~~~

Abdukhamidov, E., Abuhamad, M., Thiruvathukal, G. K., Kim, H., & Abuhmed, T. (2024). SingleAdv: Single-class target-specific attack against interpretable deep learning systems. *IEEE Transactions on Information Forensics and Security*. https://doi.org/10.1109/TIFS.2024.3355942

.. code-block:: bibtex

   @article{abdukhamidov_singleadv_2024,
     author  = {Abdukhamidov, Elmurod and Abuhamad, Mohammed and Thiruvathukal, George K. and Kim, Hyoungshick and Abuhmed, Tamer},
     title   = {{SingleAdv}: Single-class target-specific attack against interpretable deep learning systems},
     journal = {IEEE Transactions on Information Forensics and Security},
     year    = {2024},
     doi     = {10.1109/TIFS.2024.3355942},
     url     = {https://doi.org/10.1109/TIFS.2024.3355942}
   }
