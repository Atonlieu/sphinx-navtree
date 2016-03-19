==========
Transforms
==========


Top-level section titles
========================

Description
-----------

The Read the Docs theme supports optional top-level headings that divide a documentation into its main sections (*Manual* and *Demo Section* in this documentation). They show up in the navigation pane and are rendered in all caps.

In reST markup, the headings are specified as ``caption`` options on the root ``toctree`` directives:

.. code-block:: rest
   :caption: toc.rst

    .. toctree::
       :caption: Part I

       chapter_1
       chapter_2
       chapter_3

    .. toctree::
       :caption: Part II

       chapter_4
       chapter_5
       chapter_6

This works fine for the navigation menu. The trouble is that the captioned toctrees only *appear* to divide the content into top-level parts. Structurally, the above layout simply translates to six consecutive chapters at the root level. This is because parallel toctrees don't establish separate branches in the Sphinx document tree. (The captions are really only annotations that have no bearing on the structure.)

Since *Part I* and *Part II* are not reflected in the actual document hierarchy, they won't appear anywhere outside of the navigation menu. Main sections defined in this way won't show up in PDF or EPUB outputs, the HTML breadcrumb navigation, or other representations of the full content layout.

**sphinx-navtree** solves the problem by letting us define the top-level structure as a proper hierarchy and converting that structure into captioned lists for nav tree rendering purposes only. This way, we can make full use of the theme while ensuring our documentation is well-structured and renders correctly in all output formats.

Restructuring the above example as a document hierarchy leads to the following layout:

.. table::
   :class: layout cell-top

   +-----------------------+---------------------------+---------------------------+
   | .. code-block:: rest  | .. code-block:: rest      | .. code-block:: rest      |
   |    :caption: toc.rst  |    :caption: part_one.rst |    :caption: part_two.rst |
   |                       |                           |                           |
   |     .. toctree::      |     .. toctree::          |     .. toctree::          |
   |                       |                           |                           |
   |        part_one       |        chapter_1          |        chapter_4          |
   |        part_two       |        chapter_2          |        chapter_5          |
   |                       |        chapter_3          |        chapter_6          |
   +-----------------------+---------------------------+---------------------------+

When a template requests the global navigation tree, **sphinx-navtree** transforms it into one with captioned lists before it's rendered into HTML.

Essentially, the entire hierarchy is shifted up one level, with the two topmost levels merged into one. The end result is as if the structure had been specified like in the initial example — but only HTML navigation is affected. In other contexts the structure will be represented in full.

Usage
-----

To enable this feature, set the Sphinx configuration option ``navtree_shift = True``. If you are converting from captioned toctrees, split the single-level root TOC into a two-level document structure.

Since the top-level sections now correspond to actual reST documents containing their respective sub-toctrees, the main titles in the navigation pane can be turned into links by setting ``navtree_root_links = True``.

Both options are enabled on this site to provide a live example with sources. The root TOC can be found at :doc:`toc.html <toc>`.

.. tip::
   For bigger projects, the Sphinx option latex_use_parts_ is a great companion to ``navtree_shift``.

.. _latex_use_parts: http://www.sphinx-doc.org/en/stable/config.html#confval-latex_use_parts


Maximum nesting depth
=====================

Description
-----------

In the Read the Docs theme, the maximum number of visible levels in the navigation pane is currently fixed to 4. Even if the theme had an option for this, the Sphinx API only supports specifying a single value for the entire tree.

**sphinx-navtree** makes it possible to customize the number of navigation levels displayed, both globally as well as for individual branches.

Usage
-----

To enable this feature, set the Sphinx configuration option ``navtree_maxdepth``.

The maximum depth is expressed as an integer. To specify a global value, simply set the option to that value. To specify different values by section, set the option to a dictionary that maps section titles to target values.

The pseudo-title ``'default'`` may be used to provide a default value for sections that are not in the dictionary. If there is no default, unspecified sections will use the value provided by the theme. If the theme doesn't provide a value, the extension will default to 3.

As an example, the *Demo Section* area of this site limits the navigation depth to two levels. The *Overview* page under *Manual* has a limit of one, preventing the menu item from expanding at all:

.. code-block:: python

    navtree_maxdepth = {'Overview': 1, 'Demo Section': 2}

