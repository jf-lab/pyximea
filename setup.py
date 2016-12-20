from setuptools import setup

import os, platform
import numpy

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize


lib_dirs=[]
if platform.system() == 'Darwin':
    includes = [numpy.get_include()]
    f = '-framework'
    link_args = [f, 'm3api']
    libs = []
elif platform.system() == 'Windows':
    includes = [numpy.get_include(), r"C:\XIMEA\API"]
    libs = ['m3apiX64', 'xiapi64']
    lib_dirs=[r"C:\XIMEA\API\x64"]
    link_args = []
else:
    includes = [numpy.get_include()]
    link_args = ['m3api']
    libs = []



# extra_objects=["../build/libnanovg.a"]

extensions = [
    Extension(  name="ximea",
                sources=['ximea.pyx'],
                include_dirs = includes,
                libraries = libs,
                library_dirs=lib_dirs,
                extra_link_args=link_args,
                extra_compile_args=['-std=c99']
            ),
]

setup(  name="pyximea",
        version="0.0.2",
        description="Ximea XiAPI Python Bindings",
        ext_modules=cythonize(extensions),
        url="https://github.com/cyanut/pyximea",
        license="GPL"
)
