from setuptools import setup
from typing import List


def get_requirements_list()->List:
    pass
#Declaring variables for setup functions 
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Panakj Raj"
DESRCIPTION="This is a first FSDS Nov batch Machine Learning Project"
PACKAGES=["housing"]

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()


)
