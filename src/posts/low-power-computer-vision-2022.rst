:orphan:
:blogpost: true
:date: February 23, 2022
:category: Blog Post, Artificial Intelligence, Books
:tags: Low-Power Computing, Computer Vision, Edge Computing, Model Efficiency, CRC Press
:nocomments:

Low-Power Computer Vision: Improve the Efficiency of Artificial Intelligence
==============================================================================

I'm glad to share **Low-Power Computer Vision: Improve the Efficiency of Artificial Intelligence**, an edited volume I co-edited with **Yung-Hsiang Lu**, **Jaeyoun Kim**, **Yiran Chen**, and **Bo Chen**, published by **Chapman & Hall/CRC** (Routledge/CRC Press).
This post also covers the companion survey that laid the groundwork for the book, **"A Survey of Methods for Low-Power Deep Learning and Computer Vision"**, led by **Abhinav Goel** and **Caleb Tung** (Purdue University), with **Yung-Hsiang Lu** and myself, presented at WF-IoT 2020.

What the Book Is About
----------------------

Energy efficiency is critical for running computer vision on battery-powered systems — mobile phones, drones, embedded cameras, and other devices that can't rely on a wall outlet or a data-center GPU.
Since 2015, the annual **IEEE Low-Power Computer Vision Challenge** has pushed researchers to build vision systems that are both accurate and efficient.
This book collects the methods that have won those challenges, with the winning teams sharing their own solutions and the reasoning behind them.

What's Inside
-------------

The book brings together contributions spanning the history of the challenge itself through to the specific engineering techniques that won it:

* History of the Low-Power Computer Vision Challenge
* A survey on energy-efficient deep neural networks for computer vision
* Hardware design and software practices for efficient neural network inference
* Progressive automatic design of search space for one-shot neural architecture search
* Fast adjustable threshold for uniform neural network quantization
* Power-efficient neural network scheduling on heterogeneous SoCs
* Efficient neural network architectures
* Design methodology for low-power image recognition systems
* Guided design for efficient on-device object detection models

The Research Behind It
-----------------------

Before the book, the 2020 WF-IoT survey (*"A Survey of Methods for Low-Power Deep Learning and Computer Vision"*) set out the landscape the book's later chapters build on.
Deep neural networks need millions of parameters and operations to run, which makes them energy-, computation-, and memory-intensive — a poor fit for resource-constrained devices.
The survey organizes the ways researchers address this into four categories of methods: parameter quantization and pruning, compressed filters and matrix factorization, network architecture search, and knowledge distillation.
It weighs the accuracy trade-offs of each and proposes evaluation metrics meant to guide future work on making deep networks practical for low-power IoT and edge deployment.

That survey, in turn, grew out of an even larger community effort: the 2019 report *"Low-Power Computer Vision: Status, Challenges, and Opportunities,"* co-authored with the broader Low-Power Computer Vision Challenge community (dozens of contributors across the field), which took stock of where the challenge and the field stood at the time.

Why It Matters
---------------

The survey, the community report, and the book all make the same point: computer vision's usefulness is capped by where it can actually run.
A model that only works on a data-center GPU can't go in a drone, a wearable, or a sensor node.
Collecting the challenge-winning solutions in one place, alongside the surveys that map the design space, is meant to give practitioners a concrete starting point rather than a scattered literature to piece together themselves.

Citations
~~~~~~~~~

**Book**

Link: https://www.routledge.com/Low-Power-Computer-Vision-Improve-the-Efficiency-of-Artificial-Intelligence/Thiruvathukal-Lu-Kim-Chen-Chen/p/book/9780367755287

Thiruvathukal, George K., Yung-Hsiang Lu, Jaeyoun Kim, Yiran Chen, and Bo Chen, editors. *Low-Power Computer Vision: Improve the Efficiency of Artificial Intelligence*. Chapman & Hall/CRC, 2022.

.. code-block:: bibtex

   @book{thiruvathukal_lowpower_2022,
     editor    = {Thiruvathukal, George K. and Lu, Yung-Hsiang and Kim, Jaeyoun and Chen, Yiran and Chen, Bo},
     title     = {Low-Power Computer Vision: Improve the Efficiency of Artificial Intelligence},
     publisher = {Chapman and Hall/CRC},
     year      = {2022},
     isbn      = {9780367755287}
   }

**Survey (WF-IoT 2020)**

Link: https://arxiv.org/abs/2003.11066

Goel, Abhinav, Caleb Tung, Yung-Hsiang Lu, and George K. Thiruvathukal. *A Survey of Methods for Low-Power Deep Learning and Computer Vision*. 2020 IEEE 6th World Forum on Internet of Things (WF-IoT), 2020.

.. code-block:: bibtex

   @inproceedings{goel_survey_2020,
     author    = {Goel, Abhinav and Tung, Caleb and Lu, Yung-Hsiang and Thiruvathukal, George K.},
     title     = {A Survey of Methods for Low-Power Deep Learning and Computer Vision},
     booktitle = {2020 IEEE 6th World Forum on Internet of Things (WF-IoT)},
     year      = {2020},
     doi       = {10.1109/WF-IoT48130.2020.9221198},
     url       = {https://arxiv.org/abs/2003.11066}
   }
