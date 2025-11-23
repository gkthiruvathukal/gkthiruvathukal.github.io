###################################
 George K. Thiruvathukal, PhD
###################################

.. warning::

   This website is currently **under construction**. I am currently migrating away from a proprietary platform
   and returning to Sphinx and GitHub Pages.
   Thank you for your patience.


Welcome to my web site.
I'm George K. Thiruvathukal and am Professor and Chairperson for the Computer Science department at Loyola University Chicago.
I also hold a visiting computer scientist appointment at Argonne National Laboratory as part of the Guest Faculty Research Participation program.
For more information about me, see :doc:`pages/about`.

.. grid:: 2

   .. grid-item-card:: 🖊️ Blog Posts
      :text-align: center

      .. button-link:: posts/index.html
         :click-parent:
         :color: primary
         :expand:

         View Blogs

   .. grid-item-card:: 📖 Papers
      :text-align: center

      .. button-link:: papers/index.html
         :click-parent:
         :color: primary
         :expand:

         View Papers

   .. grid-item-card:: 📃 CV
      :margin: 3 0 0 0
      :text-align: center

      .. button-link:: https://github.com/gkthiruvathukal/cv/releases/latest
         :click-parent:
         :color: primary
         :expand:

         Download via GitHub


*******************
 Latest Blog Posts
*******************

.. postlist:: 5
   :category: Blog Post
   :date: %A, %B %d, %Y
   :format: {date}: {title}
   :excerpts:
   :expand: Read more ...

*****************************
 Pre-print Paper Manuscripts
*****************************

..
   TODO: Use ABlog to organize this

***********************
 Latest Other Writings
***********************

Book Summaries
===============

.. postlist:: 5
   :category: Book Summary
   :date: %A, %B %d, %Y
   :format: {date}: {title}
   :excerpts:
   :expand: Read more ...

..
   Toctrees for the side bars

.. toctree::
   :glob:
   :hidden:
   :maxdepth: 2
   :caption: Pages

   Pages <pages/index>
   pages/*

.. toctree::
   :glob:
   :hidden:
   :maxdepth: 2
   :caption: Blog Posts

   All Blog Posts <posts/index>
   posts/*

.. toctree::
   :glob:
   :hidden:
   :maxdepth: 2
   :caption: Papers

   All Papers <papers/index>
   papers/*

