# -*- coding: utf-8 -*-
"""Python client for the Diffbot API."""
from setuptools import setup


setup(
    name='diffbot',
    version='1.0.0',
    url='https://github.com/attilaolah/permutation.py',
    license='Public Domain',
    author='Attila Oláh',
    author_email='attilaolah@gmail.com',
    description="Python client for the Diffbot API.",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries",
    ],
    tests_require=[
        "nose",
    ],
    py_modules=['permutation'],
    include_package_data=False,
    test_suite='nose.collector',
    zip_safe=True,
)
