"""
ipyvizzu
Build animated charts in Jupyter Notebook and
in many other environments with a simple Python syntax.
"""

from setuptools import setup  # type: ignore


with open("requirements.txt", encoding="utf8") as fp:
    requirements = fp.read().splitlines()

with open("README.md", encoding="utf8") as fp:
    long_description = fp.read()

setup(
    name="ipyvizzu",
    version="0.13.0",
    description="Build animated charts in many environments with a simple Python syntax.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache 2",
    packages=["ipyvizzu", "ipyvizzu.integrations"],
    package_dir={"ipyvizzu": "src/ipyvizzu"},
    package_data={"ipyvizzu": ["py.typed", "templates/*.js"]},
    python_requires=">=3.6",
    install_requires=requirements,
    extras_require={
        "fugue": ["fugue>=0.8.1"],
    },
    url="https://github.com/vizzuhq/ipyvizzu",
    project_urls={
        "Documentation": "https://ipyvizzu.vizzuhq.com",
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
