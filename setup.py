# Copyright 2018 The Cornac Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

import glob
import os
import sys

from setuptools import Extension, find_packages, setup

"""
Release instruction:
    - Check that tests run correctly with all CI tools.
    - Change __version__ in setup.py, cornac/__init__.py, docs/source/conf.py.
    - Commit and release a version on GitHub, Actions will be triggered to build and upload to PyPI.
    - Update conda-forge feedstock with new version and SHA256 hash of the new .tar.gz archive on PyPI (optional), the conda-forge bot will detect a new version and create PR after a while.
    - Check on https://anaconda.org/conda-forge/cornac that new version is available for all platforms.
"""


with open("README.md", "r") as fh:
    long_description = fh.read()


cmdclass = {}


setup(
    name="cornac",
    version="1.14.2.1",
    description="A Comparative Framework for Multimodal Recommender Systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://cornac.preferred.ai",
    keywords=[
        "recommender system",
        "collaborative filtering",
        "multimodal",
        "preference learning",
        "recommendation",
    ],
    install_requires=["numpy", "scipy", "tqdm>=4.19", "powerlaw"],
    extras_require={"tests": ["pytest", "pytest-pep8", "pytest-xdist", "pytest-cov"]},
    cmdclass=cmdclass,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
    ],
)
