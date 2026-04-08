#!/usr/bin/env python3
"""
Setup script for brother_ql_web
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="brother_ql_web",
    version="1.0.0",
    author="DL6ER",
    description="A dockerized Python3 web service to print labels on Brother QL label printers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DL6ER/brother_ql_web",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "Topic :: Printing",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "brother-ql-web=run:main",
        ],
    },
    include_package_data=True,
    package_data={
        "app": [
            "static/css/*",
            "static/fontawesome/css/*",
            "static/fontawesome/webfonts/*",
            "static/images/favicon/*",
            "static/js/*",
            "static/webfonts/*",
            "templates/*",
            "errors/templates/*",
            "labeldesigner/templates/*",
            "main/templates/*",
        ],
    },
    zip_safe=False,
)
