#!/usr/bin/env python3

from setuptools import setup, find_packages

exec(open('forrest/__init__.py').read())

setup(
    name='forrest',
    version=__version__,
    description='A database of GAMS runs.',
    maintainer='Tim Tröndle',
    maintainer_email='tim.troendle@online.de',
    url='https://www.github.com/philipphanemann/forrestgums',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=['sumatra>0.7.4', 'GitPython'],
    entry_points={
        'console_scripts': [
            'forrest=forrest.main:start_web_server',
        ],
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering'
    ]
)
