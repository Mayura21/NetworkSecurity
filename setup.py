'''
Used setup tools to define the configurations of project, such as metadata, dependencies and more
'''

from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """
    This function returns the list of requirements
    """
    requirement_list: List[str] = list()
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()
                # Ignore -e. and empty lines
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_list


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Mayura S M",
    author_email='mayurasm2000@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)