import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="strmanip", 
    version="0.0.1",
    author="Sanmitha Sadhishkumar",
    author_email="sanmithasadhishkumar@gmail.com",
    description="This module gives additional string functions to make python programming easier than before",
    long_description=long_description,
    long_description_content_type="text/markdown"
    url="https://github.com/Sanmitha-Sadhishkumar/strmanip/tree/master/strmanip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
