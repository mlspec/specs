# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='MLSpec',
    version='0.0.1',
    description='MLSpec helper library to making using metadata in ML workflows easier',
    long_description=readme,
    author='David Aronchick',
    author_email='aronchick@gmail.com',
    url='https://github.com/mlspec/mlspec-lib',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

