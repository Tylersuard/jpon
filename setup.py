from setuptools import setup, find_packages

setup(
    name="jpon",
    version="0.1.0",
    author="Tyler Suard",
    author_email="tylersuard@gmail.com",
    description="A simple alternative to JSON using Python syntax.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tylersuard/jpon",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
