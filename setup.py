#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='pyduinolcdclock',
    description="LCD shield library for the Synapse Pyduino development board",
    maintainer='Tyler Crumpton',
    maintainer_email='tyler.crumpton@synapse-wireless.com',
    url='https://github.com/synapse-wireless/pyduino-lcd-clock',
    packages=['pyduinolcdclock'],
    install_requires=[
        'vcversioner',
        'pyduinolcd==1.0.0',
        'snappyatmega==1.0.1'
    ],
    dependency_links=[
        "git+https://github.com/synapse-wireless/pyduino-lcd.git@v1.0.0#egg=pyduinolcd-1.0.0",
        "git+https://github.com/synapse-wireless/snappy-atmega.git@v1.0.1#egg=snappyatmega-1.0.1"
    ],
    vcversioner={
        'version_module_paths': ['pyduinolcdclock/_version.py'],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
    ],
)
