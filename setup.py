import os
from setuptools import find_packages, setup
  
setup(
    name= 'pivottraffic',
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license="Private",
    description= "This is the description",
    author= "Mark Lovretovich",
    author_email= "mlovretovich@gmail.com",
  
    install_requires=["pandas >= 2.2.0"],
  
    entry_points={
        'console_scripts': ['pivottraffic = pivottraffic.pipeline:main']
    }
)