"""Python setup.py for ubiquitous_octo_bassoon package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("ubiquitous_octo_bassoon", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="ubiquitous_octo_bassoon",
    version=read("ubiquitous_octo_bassoon", "VERSION"),
    description="Awesome ubiquitous_octo_bassoon created by JDSanti",
    url="https://github.com/JDSanti/ubiquitous-octo-bassoon/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="JDSanti",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["ubiquitous_octo_bassoon = ubiquitous_octo_bassoon.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
