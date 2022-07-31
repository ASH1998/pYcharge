import os
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join("pycharge", "version.txt")) as file_handler:
    __version__ = file_handler.read().strip()

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

DESCRIPTION = 'ML Library'

# Setting up
setup(
    name="python-charge",
    version=__version__,
    author="Ashutosh Mishra",
    url="https://github.com/ASH1998/pYcharge",
    author_email="pythonicdevil@gmail.com",
    description=DESCRIPTION,
    license="MIT",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=[package for package in find_packages() if package.startswith("pycharge")],
    install_requires=[],
    python_requires=">=3.8",
    keywords=['python', 'machine learning'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
)