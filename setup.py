from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()


setup(
    name="FindMyRoomie",
    version="3.0",
    description="Django app to find roommates built for NCSU students",
    long_description=long_description,
    author="Rohit Geddam, Shandler Mason, Arun kumar, Kiron Jayesh, Teja Varma",
    license="MIT",
    keywords="FindMyRoomie roommate finder",
    packages=find_packages(),
    install_requires=[],
)
