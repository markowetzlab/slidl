#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages


REQUIREMENTS_FILE = "requirements.txt"
README_FILE = "README.md"

# Requirements
with open(REQUIREMENTS_FILE) as handle:
    requirements = handle.read().strip().split("\n")

with open(README_FILE) as readme_file:
    readme = readme_file.read()

def local_scheme(version):
    return ""

setup(
    name="slidl",
    package="slidl",
    packages=find_packages(),
    use_scm_version={
        "local_scheme": local_scheme,
        "write_to": "slidl/_version.py",
        "write_to_template": '__version__ = "{version}"\n',
    },
    author="A.G. Berman, William R. Orchard, Marcel Gehrung",
    author_email="florian.markowetz@cruk.cam.ac.uk",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="SliDL: a Python library of pre- and post-processing tools for applying deep learning to whole-slide images",
    long_description_content_type="text/markdown",
    long_description=readme,
    license="GNU General Public License v3",
    include_package_data=True,
    keywords=["ai", "deep learning", "pathology"],
    setup_requires=["setuptools_scm"],
    install_requires=requirements,
    tests_require=requirements,
    url="https://github.com/markowetzlab/slidl",
    project_urls={
        "Bug Tracker": "https://github.com/markowetzlab/slidl/issues",
        "Documentation": "https://slidl.readthedocs.io",
        "Source Code": "https://github.com/markowetzlab/slidl",
    },
    zip_safe=False,
)
