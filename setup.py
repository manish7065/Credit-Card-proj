from setuptools import setup, find_packages
from typing import List

# Declaring variables for setup functions
PROJECT_NAME = "Credit Card Default Checker"
VERSION = "0.0.1"
AUTHOR = "Manish Kumar"
DESRCIPTION = """This is a credit card deault checking project,
which will predict that the car holder will pay or not next installment."""


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    packages=find_packages(),
)
