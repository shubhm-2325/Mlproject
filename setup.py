from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirement(file_path:str)->List[str]:
    '''
    This funcyion will return the list requirements
    '''
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace("\n","")for req in requirement]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)
    return requirement

setup(
name='mlproject',
version='0.0.1',
author='shubham',
author_email='shubhamsingh2325@gmail.com',
packages=find_packages(),
instll_requires=get_requirement('requirement.txt'),


)