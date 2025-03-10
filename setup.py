#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 'chibi_api>=0.1.0' ]

setup(
    author="dem4ply",
    author_email='dem4ply@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="libreria para usar github",
    entry_points={
        'console_scripts': [
            'chibi_github=chibi_github.cli:main',
        ],
    },
    install_requires=requirements,
    license="WTFPL",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='chibi_github',
    name='chibi_github',
    packages=find_packages(include=['chibi_github', 'chibi_github.*']),
    url='https://github.com/dem4ply/chibi_github',
    version='0.1.2',
    zip_safe=False,
)
