#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='nblox-contact',
    # Please read the following for setting the version number:
    #    - https://pythonhosted.org/setuptools/setuptools.html#specifying-your-project-s-version  # noqa
    version='0.0.0',

    author='Pedro H <pedro@digitalrounin.com>',
    author_email='pedro@digitalrounin.com',

    # description='',
    # long_description=,

    # TODO - Add GitHub link
    # url='https://github.com/',

    license='MIT',

    # TODO - Add more classifiers.
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],

    # TODO - Add keywords.
    keywords='aws lambda',

    packages=find_packages(exclude=['tests']),
    install_requires=[
        'boto3>=1.4.4',
        'Flask>=0.12.1'
    ]
)
