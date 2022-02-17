.. ipyvizzu documentation master file, created by
   sphinx-quickstart on Thu Feb 17 22:55:18 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ipyvizzu
========

`Vizzu <https://lib.vizzuhq.com/>`_ is a free, open-source Javascript/C++ library
utilizing a generic dataviz engine that generates many types of charts and
seamlessly animates between them. It can be used to create static charts but
more importantly it is designed for building animated data stories and
interactive explorers as Vizzu enables showing different perspectives of the
data that the viewers can easily follow due to the animationr.

**Note:** ``Chart.show(...)`` only generates a javascript code. The vizzu calls
are evaulated by the browser. Therefore if the vizzu figure is blank you should
check the console of your browser where the javascript reports its errors.

The examples bellow are copied from the `vizzu tutorial <https://lib.vizzuhq.com/0.4/>`_. 
You can read more information from there.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   examples/data
   examples/axes
   examples/geometry
   examples/channels
   examples/group
   examples/sorting
   examples/align
   examples/aggregate
   examples/orientation
   examples/without_coordinates
   examples/palette_font
   examples/layout
