import pathlib

from setuptools import find_namespace_packages, setup

here = pathlib.Path(__file__).parent.resolve()


# setup arguments
name = "aoc2020"
description = "https://adventofcode.com/2020"
version = "0.1.0"
author = "Simon Keith"
author_email = "simonkth@gmail.com"
url = "https://github.com/simonkth/aoc2020"
long_description = (here / "README.md").read_text(encoding="utf-8")
long_description_content_type = "text/markdown"

# Package requirements
install_requires = []

setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    url=url,
    author=author,
    author_email=author_email,
    packages=find_namespace_packages(include=("{name}*".format(name=name),)),
    package_data={"aoc2020.input": ["*.txt"]},
    python_requires=">=3.7, <4",
    install_requires=install_requires,
)
