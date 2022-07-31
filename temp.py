import os
from setuptools import find_packages, setup
import codecs

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join("pycharge", "version.txt")) as file_handler:
    __version__ = file_handler.read().strip()

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

print(long_description)