#!/usr/bin/env python

import setuptools
import numpy
from Cython.Build import cythonize
from Cython.Compiler import Options

Options.docstrings = False

_include = [
    "src/**"
]
_excludes = []

setuptools.setup(name='project_name',
                 version='0.1.0',
                 description='UnitX SoftWare',
                 author='UnitX Team',
                 author_email='info@unitxlabs.com',
                 packages=setuptools.find_packages(),
                 python_requires='>=3.11',
                 ext_modules=cythonize(
                     include=_include,
                     exclude=_excludes,
                     language_level="3",
                     build_dir="build/c_src",
                     compiler_directives={
                         'emit_code_comments': False,
                         'always_allow_keywords': True,
                         'annotation_typing': False,
                     },
                 ),
                 include_dirs=[numpy.get_include()]
                 )
