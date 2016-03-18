==============
sphinx-navtree
==============

**sphinx-navtree** is a small `Sphinx <sphinx_>`_ extension that lets you modify the documentation's HTML navigation tree while keeping the underlying TOC structure intact.

It is mainly designed to address some issues with the `Read the Docs theme <rtd_theme_>`_ but can be used with other themes too.

There are a couple of things the extension can do:

* Optimize the presentation of top-level sections across output formats.
* Specify a maximum nesting depth for different parts of the nav tree.

The features are explained in detail on the :doc:`transforms` page.

.. _sphinx: http://www.sphinx-doc.org/en/stable/index.html
.. _rtd_theme: https://read-the-docs.readthedocs.org/en/latest/theme.html


General usage
=============

Install it like any other extension::

    pip install sphinx-navtree

.. code-block:: python
   :caption: conf.py

    extensions = [..., 'sphinx_navtree']

The package provides a drop-in replacement for the `toctree <template_toctree_>`_ callable that Sphinx templates use to build navigation trees. The provided function applies the configured transforms to the resolved node tree before rendering it into HTML.

The following **conf.py** options are available:

* ``navtree_shift``
* ``navtree_root_links``
* ``navtree_maxdepth``
* ``navtree_template_var``

The first three deal with individual features and are covered in :doc:`transforms`. No transforms are enabled by default.

``navtree_template_var`` is a string designating the Sphinx template variable through which the modified nav tree is made available to templates. The default value is ``'toctree'``, meaning that it will replace the standard variable. This works out of the box with the Read the Docs theme.

If you have templates using the `toctree <template_toctree_>`_ callable for something where the nav tree transforms are not wanted, you can set ``navtree_template_var`` to a custom value such as ``'navtree'``.

.. _template_toctree: http://www.sphinx-doc.org/en/stable/templating.html#toctree


Links
=====

* `Project repository at GitHub <https://github.com/bintoro/sphinx-navtree>`_
* `PyPI entry <https://pypi.python.org/pypi/sphinx-navtree>`_

