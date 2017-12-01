#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'pushtx',
    version = '1.0.0',
    keywords = ('pushtx', 'pushtx-sdk', 'python'),
    description = 'btc.com pushtx python sdk',
    license = 'MIT License',

    url = 'https://pushtx.btc.com',
    author = 'dubuqingfeng',
    author_email = 'app@btc.com',

    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = [],
)