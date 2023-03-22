from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str) -> List[str]:
    '''
    This is function for requirement
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]
        if HYPEN_E_DOT:
            requirements.remove(HYPEN_E_DOT)
    return requirements    
    
    
setup(
name = "mlproject",
version = "0.0.1",
author = "madhav",
author_email = "madhavkumarsingh@gmail.com",
packages = find_packages(),
install_requires = get_requirements("requirement.txt")
)