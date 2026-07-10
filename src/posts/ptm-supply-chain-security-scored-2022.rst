:orphan:
:blogpost: true
:date: November 7, 2022
:category: Blog Post, Artificial Intelligence, Security, Software Engineering
:tags: Pre-Trained Models, Software Supply Chain Security, SCORED
:nocomments:

An Empirical Study of Artifacts and Security Risks in the Pre-Trained Model Supply Chain (SCORED 2022)
=========================================================================================================

This paper was led by **Wenxin Jiang** (Purdue University, working with **James C. Davis**), with contributions from **Nicholas Synovic**, **Rohan Sethi**, **Aryan Indarapu**, **Matt Hyatt**, and **Taylor R. Schorlemmer**.
I am one of the key leaders of this research project.
The work appeared at **SCORED '22** (ACM Workshop on Software Supply Chain Offensive Research and Ecosystem Defenses), co-located with ACM CCS 2022.

Abstract / Summary
------------------

Pre-trained models (PTMs) are now downloaded and reused the way traditional software depends on packages from registries like npm or PyPI — but unlike those registries, the PTM supply chain has had almost no systematic security study.
This paper maps the structure of that supply chain across eight model hubs, catalogs the security features (or lack thereof) each one offers, and shows where existing supply-chain defenses fail to carry over from traditional software.

Background
----------

Model hubs such as Hugging Face now rival traditional package registries in scale and popularity, yet PTMs face threats that traditional packages don't: direct attacks such as backdoors, trojans, and injected malware, as well as indirect attacks through data poisoning, on top of the ordinary software supply chain risks that already apply to any downloaded artifact.
Despite this, there had been no structural account of how PTM supply chains are organized or how well existing hubs guard against these risks.

Key Contributions
-----------------

* A structural mapping of artifacts across eight model hubs, identified and classified as open (anyone can upload), gated (approval required), or commercial (internal-only).
* A catalog of the security features and threat models associated with each hub type.
* A comparative analysis of PTM supply chains against traditional software supply chains, focused on versioning and security properties.
* Two concrete risk categories — maintainer reach and model discrepancies — with empirical measurements of each.

Findings
--------

Hugging Face alone hosts over 60,000 public PTMs, with download volumes comparable to major traditional package ecosystems.
Two risks stood out. First, **maintainer reach**: control is concentrated — half of maintainers can access only a single repository, but a few can reach tens or hundreds, meaning a single compromised account can have an outsized blast radius.
Second, **model discrepancies**: performance claims are largely unverifiable. Only a fraction of models included checkable claims (8 of 53 object detection models, 4 of 26 image classification models, though 136 of 160 sentiment analysis models), and among the ones that were checkable, some — including models from major technology companies — showed accuracy discrepancies exceeding 5%, discrepancies large enough to potentially mask evidence of attacks like BadNet or EvilModel.

Key Take-Aways
--------------

Existing software supply chain defenses do not transfer cleanly to the PTM ecosystem.
Concentrated maintainer access and unverifiable performance claims are both concrete, measurable risks today, not hypothetical ones.
The paper calls for expanded empirical study of PTM security characteristics and for automated tooling — model auditing and specialized scanning — purpose-built for this supply chain, rather than adapting tools designed for traditional software packages.

Citation
~~~~~~~~

DOI: https://doi.org/10.1145/3560835.3564547

Jiang, Wenxin, Nicholas Synovic, Rohan Sethi, Aryan Indarapu, Matt Hyatt, Taylor R. Schorlemmer, George K. Thiruvathukal, and James C. Davis. *An Empirical Study of Artifacts and Security Risks in the Pre-Trained Model Supply Chain*. Proceedings of the 2022 ACM Workshop on Software Supply Chain Offensive Research and Ecosystem Defenses (SCORED), 2022, pp. 105–114.

.. code-block:: bibtex

   @inproceedings{jiang_empirical_2022,
     author    = {Jiang, Wenxin and Synovic, Nicholas and Sethi, Rohan and Indarapu, Aryan and Hyatt, Matt and Schorlemmer, Taylor R. and Thiruvathukal, George K. and Davis, James C.},
     title     = {An Empirical Study of Artifacts and Security Risks in the Pre-Trained Model Supply Chain},
     booktitle = {Proceedings of the 2022 ACM Workshop on Software Supply Chain Offensive Research and Ecosystem Defenses},
     year      = {2022},
     pages     = {105--114},
     doi       = {10.1145/3560835.3564547},
     publisher = {Association for Computing Machinery},
     address   = {New York, NY, USA}
   }
