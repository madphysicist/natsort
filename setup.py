#! /usr/bin/env python

from setuptools import find_packages, setup
setup(
    name='natsort',
    version='5.4.1',
    packages=find_packages(),
    install_requires=["argparse; python_version < '2.7'"],
    entry_points={'console_scripts': ['natsort = natsort.__main__:main']},
    extras_require={
        'fast': ["fastnumbers >= 2.0.0; python_version > '2.6'"],
        'icu': ["PyICU >= 1.0.0"]
    }
)
