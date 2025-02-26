"""Pfizer testing.

Import the package::

   import tmp_testing_demo

This is the complete API reference:

.. autosummary::
   :toctree: .

   example_function
   ExampleClass
"""

__version__ = "0.0.1"  # denote a pre-release for 0.1.0 with 0.1rc1

from lamindb_setup import _check_instance_setup

if _check_instance_setup():
    from ._core import ExampleClass, save_dataframe
