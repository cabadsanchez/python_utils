import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cabadutils",
    version="0.0.1",
    author="Carlos Abad Sánchez",
    author_email="c.abad.sanchez@gmail.com",
    description="Package with useful all-day modules and functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cabadsanchez/python_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)