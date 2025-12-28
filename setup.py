# find_packages: automatically finds out the packages that are available in the application in the directory.
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str)-> List[str]:
    """
    This function gets the requirements for the package
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements] 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


setup(
    name = 'mlproject',
    version = '0.0.1',
    author = "Jathu",
    author_email = "s.jathurshan03@gmail.com",
    #packages = find_packages(),
    packages = find_packages("src"),
    package_dir = {"": "src"},
    install_requires = get_requirements('requirements.txt')
)
