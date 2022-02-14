#!/usr/bin/env python3
from setuptools import setup

with open("README.md") as fp:
    long_description = fp.read()

setup(
    name="ipyvizzu",
    version="0.4.1",
    description="Jupyter notebook integration for vizzu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache 2",
    py_modules=["ipyvizzu"],
    python_requires='>=3.6',
    install_requires=["IPython"],
    url="https://github.com/vizzuhq/ipyvizzu",
    project_urls={
        "Documentation": "https://vizzuhq.github.io/ipyvizzu/index.html",
        "Source": "https://github.com/vizzuhq/ipyvizzu",
        "Tracker": "https://github.com/vizzuhq/ipyvizzu/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
)
