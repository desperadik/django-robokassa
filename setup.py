#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from distutils.core import setup

for cmd in ('egg_info', 'develop'):
    import sys
    if cmd in sys.argv:
        from setuptools import setup

import sys

if sys.version_info[0] == 2:
    long_description = open('README.rst').read().decode('utf-8') + u"\n\n" + open('CHANGES.rst').read().decode('utf-8')
elif sys.version_info[0] == 3:
    long_description = open('README.rst', encoding='utf-8').read() + u"\n\n" + open('CHANGES.rst', encoding='utf-8').read()
else:
    long_description = ''

setup(
    name='django-robokassa',
    version='1.2',
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',

    packages=['django_robokassa', 'django_robokassa.migrations'],

    url='https://bitbucket.org/kmike/django-robokassa/',
    license = 'MIT license',
    description = 'Приложение для интеграции платежной системы ROBOKASSA в проекты на Django.',
    long_description = long_description,

    requires=['django (>= 1.8)'],

    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
)
