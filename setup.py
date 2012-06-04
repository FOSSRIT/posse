"""Setuptools setup file"""

import sys, os
import multiprocessing, logging

from setuptools import setup

setup(
    name='posse',
    version='0.1',
    description="Materials for teaching POSSE at RIT",
    install_requires=[
        'Sphinx',
        'cloud_sptheme',
        'pyyaml',
        'feedparser',
        'six',  # For python3 support.
    ],
    url = "http://teachingopensource.org/index.php/RIT",
    download_url="https://github.com/Qalthos/posse",
    author='Nathaniel Case',
    author_email='Qalthos@gmail.com',
    license='GPLv3+',
    packages = [],
    namespace_packages = [],
    include_package_data=True,
    zip_safe=False,
    classifiers = [],
)
