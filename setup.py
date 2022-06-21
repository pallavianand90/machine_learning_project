from setuptools import setup
from typing import List


#declearing all the variables
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR =  "pallavi anand"
DESCRIPTION = "This is my first end-to-end machine learning project"
REQUIREMENT_FILE_NAME = "requirements.txt" 


def get_requirements_list()->List[str]:
   '''
    Description: This function is going to return list of requirement which is mention
    in requirement.txt file.

    return This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file

   '''
   with open(REQUIREMENT_FILE_NAME) as requirement_file:
       return requirement_file.readlines().remove("-e .")
def find_packages():
    pass

setup(
name = PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description = DESCRIPTION,
package = find_packages(),
install_require = get_requirements_list()

)