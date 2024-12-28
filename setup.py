from setuptools import find_packages,setup
from typing import List
edot='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the requirements in the form of list
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements ]
        if edot in requirements:
            requirements.remove(edot)

setup(
    name="NewEra",
    version="0.0.1",
    author="NIKHIL",
    author_email="gptnikhil1977@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')   #['pandas','numpy','seaborn']
)