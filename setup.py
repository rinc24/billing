from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='billing',
    version='0.0.1',
    description='Billing app for Django',
    long_description=long_description,
    url='https://github.com/rinc24/billing.git',

    author='Vadim Romanov',
    author_email='vadim@rinc.site',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['safe-delete @ git+ssh://git@github.com/rinc24/safe_delete.git@0.0.3'],
)
