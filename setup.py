import os
import sys
from setuptools import setup, find_packages

tests_require = [ ]
if sys.version_info < (3, 3):
    tests_require.append('mock') # mock became available as unittest.mock from Python 3.3.

setup(
    name = 'vexf_ioctl',
    packages = find_packages(),
    use_scm_version = True,
    description = 'ioctl helper functions for vexf (vision exchange format)',
    license = 'MIT',
    maintainer = 'Aswin Vijayakumar',
    maintainer_email = 'aswinvk28@gmail.com',
    url = 'https://github.com/olavmrk/python-ioctl',
    download_url = 'https://github.com/aswinvk28/python-ioctl/releases',
    setup_requires = [ 'setuptools_scm' ],
    tests_require = tests_require,
    test_suite = 'tests',
)
