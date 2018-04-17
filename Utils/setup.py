#  -*- coding: utf-8 -*-
from setuptools import setup, find_packages

__version__ = "0.1.0"

setup(
    name='rec_edu_utils',
    version=__version__,
    author='Guilherme',
    description='Possui as classes Item e Perguntas usadas na Pre-Recomendacao e na Recomendacao',
    packages=['rec_edu_utils'],
    install_requires=['neo4j-driver'],
    zip_safe=False
)
