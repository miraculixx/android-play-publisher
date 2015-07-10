import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='android-play-publisher',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='apache',  
    description='android playstore publisher',
    long_description=README,
    author='Patrick Senti',
    author_email='miraculixx@gmx.ch',
    classifiers=[
        'Environment :: Desktop',
        'Intended Audience :: Developers',
        'License :: Apache', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # replace these appropriately if you are using Python 3 
        'Programming Language :: Python :: 2', 
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'google-api-python-client',
    ], 
    dependency_links=[
    ]
)
