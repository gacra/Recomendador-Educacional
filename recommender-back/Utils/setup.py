#  -*- coding: utf-8 -*-
from setuptools import setup, find_packages

__version__ = "0.1.0"

setup(
    name='rec_edu_utils',
    version=__version__,
    author='Guilherme',
    # packages=['rec_edu_utils'],
    packages=find_packages(),
    install_requires=['neo4j-driver'],
    zip_safe=False
)
