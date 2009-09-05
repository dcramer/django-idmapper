#!/usr/bin/env python

from setuptools import setup, find_packages

import idmapper

setup(
    name='django-idmapper',
    version=".".join(map(str, idmapper.__version__)),
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='http://github.com/dcramer/django-idmapper',
    install_requires=[
        'django>=1'
    ],
    description = 'An identify mapper for the Django ORM',
    packages=find_packages(),
    include_package_data=True,
)
