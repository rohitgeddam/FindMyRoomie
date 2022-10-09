.. FindMyPack documentation master file, created by
   sphinx-quickstart on Wed Oct  5 23:40:44 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



========================================
Welcome to FindMyRoomie's documentation!
========================================

'FindMyRoomie' is a Web Application that provides a platform for lonely wolves (NC State students) to find roommates of their preference. 
The stakes are high when it comes to finding your best roommate because this relationship starts with a living relationship 😅.
We understand how stressful this can be, especially if you are moving to a new city or country. 
FindMyRoomie is a one-stop solution to your roommate finding needs. Our software has functionalities that allow you to filter and choose your ideal roommate. 
But if that is too much work for you, we also provide roommate suggestions based on your preferences! 
Any NC State student could sign up with their NC State Email address from any corner of the world on our website and begin searching for roommates.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   requirements/main.rst
   quickstart/main.rst
   techused/main.rst
   contributing/main.rst
   github/main.rst
   trackissue/main.rst
   troubleshooting/main.rst
   license/main.rst
   releases/main.rst

Seed users
==========

.. automodule:: base.management.commands.seed_users
   :members:

Matching Algorithm
==================

.. automodule:: base.matching
   :members:

Profile filter
==============

.. automodule:: base.filters
   :members:

Forms
=====

.. automodule:: base.forms
   :members:

User Manager model
==================

.. automodule:: base.managers
   :members:

Profile model
=============

.. automodule:: base.models
   :members:

Utility Functions
=================
.. automodule:: base.utils
   :members:

Configuration
=============

.. automodule:: config.asgi
   :members:

.. automodule:: config.settings
   :members:

.. automodule:: config.urls
   :members:

.. automodule:: config.wsgi
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
