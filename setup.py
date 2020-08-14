import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="strmanip", # Replace with your own username
    version="0.0.1",
    author="Sanmitha Sadhishkumar",
    author_email="sanmithasadhishkumar@gmail.com",
    description="This module gives additional string functions to make python programming easier than before",
    long_description=long_description,
    long_description_content_type="""long_description_content_type="This file adds more **string functions** to python.
    These functionalities are commonly used by the people very often.
    In all those cases, these functions will be very useful
    . Some of the functions mentioned here have a long code.
    Hence, they are helpful in compressing the code.
    The available functions and their description are :
    i) word count() - to count the occurrence of each word in the given string
	ii) addpref() - to add a prefix to each sentence of the given string
	iii) chrrem() - to remove the mentioned character in the given string
	iv) strrep() - to replace the occurrence of a string in the given string with a new string
	v) cwlcount() - to count the occurrence of each character, word and line in the given string
	vi) slicesub() - gives the step by step slice of the given string
	vii) ismem() - returns whether the second string is found in the first string or not
	viii) ispalindrome() - returns whether the given string is a palindrome or not
	ix) vowcons() - returns the number of vowels and consonants in the given string
	x) abece() - returns an abecedarian series
	xi) vowrem() - returns a string from the given string with all the vowels removed
	xii) chrcount() - returns the occurrence of the given character in the given string
	xiii) pyramid() - returns a pattern of specified condition
	xvii) iscapitalised() - used to check whether the given string is in capitalised form or not
	xiv) istitled() - checks whether the given string is in titled form
	xv) splitchr() - used to split all the characters in the given string/markdown""",
    url="https://github.com/Sanmitha-Sadhishkumar/strmanip/tree/master/strmanip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: PSFL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
