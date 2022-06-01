#!/usr/bin/env python3

from setuptools import setup
import sys


with open("README.md") as fp:
    long_description = fp.read()


version = "1.0.0"


select = "pyvizzu"
if "--ipyvizzu" in sys.argv:
    select = "ipyvizzu"
    sys.argv.remove("--ipyvizzu")
elif "--stpyvizzu" in sys.argv:
    select = "stpyvizzu"
    sys.argv.remove("--stpyvizzu")


if select == "pyvizzu":
    setup(
        name="pyvizzu",
        version=version,
        description="pyvizzu is the Python integration of Vizzu.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license="Apache 2",
        packages=["pyvizzu"],
        package_dir={"pyvizzu": "src/pyvizzu"},
        package_data={"pyvizzu": ["templates/*.js"]},
        python_requires=">=3.6",
        install_requires=["pandas"],
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
elif select == "ipyvizzu":
    setup(
        name="ipyvizzu",
        version=version,
        description="ipyvizzu is the Jupyter Notebook integration of Vizzu.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license="Apache 2",
        packages=["ipyvizzu"],
        package_dir={"ipyvizzu": "src/ipyvizzu"},
        python_requires=">=3.6",
        install_requires=["IPython", f"pyvizzu=={version}"],
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
elif select == "stpyvizzu":
    setup(
        name="streamlit-pyvizzu",
        version=version,
        description="streamlit-pyvizzu is the Streamlit integration of Vizzu.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license="Apache 2",
        packages=["stpyvizzu"],
        package_dir={"stpyvizzu": "src/stpyvizzu"},
        python_requires=">=3.6",
        install_requires=["streamlit", f"pyvizzu=={version}"],
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