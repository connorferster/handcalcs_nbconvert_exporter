from setuptools import setup, find_packages
from codecs import open
from os import path

from jupyter_packaging import get_data_files, get_version

pjoin = path.join

name = 'handcalcs_nbconvert_exporter'
here = path.abspath(path.dirname(__file__))
version = get_version(pjoin(here, name, '_version.py'))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requires = [
    'jupyterlab>=1.0.0',
    'nbconvert>=6.0.0',
]

dev_requires = requires + [
    'pytest',
    'pytest-cov',
    'flake8',
    'bump2version',
    'mock',
    'autopep8'
]

setup(
    name=name,
    version=version,
    description='A simple helper library with two nbonvert exporters for PDF/HTML export with no code cells',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/connorferster/handcalcs_nbconvert_exporter',
    author='Tim Paine, Connor Ferster',
    author_email='connorferster@gmail.com',
    license='Apache 2.0',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Jupyter',
    ],
    keywords='jupyter jupyterlab',
    packages=find_packages(exclude=['tests', ]),
    python_requries='>=3.6',
    include_package_data=True,
    data_files=get_data_files([
        ("share", str(pjoin(here, "share")), "**"),
    ]),
    zip_safe=False,
    entry_points={
        'nbconvert.exporters': [
            'pdf_nocode = handcalcs_nbconvert_exporter.nbconvert_functions.hideinput.exporters:PDFHideCodeExporter',
            'html_nocode = handcalcs_nbconvert_exporter.nbconvert_functions.hideinput.exporters:HTMLHideCodeExporter',
        ],
    },
    extras_require={
        'dev': dev_requires,
    },
)
