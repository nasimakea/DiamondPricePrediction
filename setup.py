from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:  # Use the variable `file_path`
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        # Optional: To ignore '-e .' if present in requirements
        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements

setup(
    name="DiamondPricePrediction",
    version="0.0.1",
    author="Nasim",
    author_email="nasimakram6200@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()
)
