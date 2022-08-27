#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
see https://medium.com/swlh/decoding-noaa-satellite-images-using-50-lines-of-code-3c5d1d0a08da

Noaa-decoding - 2022 - por jero98772
Noaa-decoding - 2022 - by jero98772
"""
from setuptools import setup, find_packages
setup(
	name='jerotools',
	version='1.0.1',
	license='GPLv3',
	author_email='jero98772@protonmail.com',
	author='jero98772',
	description='web page for decoding image from noaa satelites',
	url='https://jero98772.pythonanywhere.com/proyects/noaa.html',
	packages=find_packages(),
    install_requires=['numpy', 'matplotlib','Flask','scipy','pillow'],
    include_package_data=True,
)