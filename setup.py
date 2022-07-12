#!/usr/bin/env python3
from setuptools import setup

with open("requirements.txt") as fp:
    requirements = fp.read().splitlines()

with open("README.md") as fp:
    long_description = fp.read()

setup(
    name="ipyvizzu",
    version="0.11.1",
    description="ipyvizzu is the Jupyter Notebook integration of Vizzu.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache 2",
    packages=["ipyvizzu"],
    package_dir={"ipyvizzu": "src/ipyvizzu"},
    package_data={"ipyvizzu": ["py.typed", "templates/*.js"]},
    python_requires=">=3.6",
    install_requires=requirements,
    url="https://github.com/vizzuhq/ipyvizzu",
    project_urls={
        "Documentation": "https://ipyvizzu.vizzuhq.com/",
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
