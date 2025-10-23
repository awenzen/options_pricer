from setuptools import setup, Extension
import pybind11
import os

# Set C++ standard and optimization flags
# This is a robust way to pass flags
os.environ["CXXFLAGS"] = "-std=c++17 -O3"

ext_modules = [
    Extension(
        'pricer_cpp',  # Module name in Python
        [
            'cpp_src/BlackScholes.cpp',
            'cpp_src/wrapper.cpp'
        ],
        include_dirs=[
            pybind11.get_include(),
            'cpp_src'  # So it can find BlackScholes.h
        ],
        language='c++',
    ),
]

setup(
    name='pricer_cpp',
    version='1.0',
    description='C++ options pricer extension',
    ext_modules=ext_modules, # This tells setup what to build
)