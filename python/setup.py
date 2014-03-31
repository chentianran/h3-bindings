#!/usr/bin/env python

from distutils.core import setup, Extension

wrapper = Extension(
	    '_hom4ps', 
	    ['hom4psPYTHON_wrap.cxx'], 
	    libraries=['hom4ps']
	)
setup (
    name='Hom4PSpy',
    version='@CPACK_PACKAGE_VERSION_MAJOR@.@CPACK_PACKAGE_VERSION_MINOR@.@CPACK_PACKAGE_VERSION_PATCH@',
    description='Python binding for Hom4PS-3, a numerical nonlinear system solver',
    author='Tianran Chen',
    author_email='@CPACK_PACKAGE_CONTACT@',
    url='http://www.hom4ps3.org',
    py_modules=['hom4ps', 'hom4pspy'],
    ext_modules=[wrapper],
)
