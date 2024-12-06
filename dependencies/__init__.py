# my_package/__init__.py

# Initializing package-level variables or settings
__version__ = '0.1.0'
__author__ = 'robert19066'

# Importing modules to make them accessible when the package is imported
from dependencies import dependencies

# Alternatively, you can define an __all__ list to specify what is exported
__all__ = ['dependencies']
