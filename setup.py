import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sshtools-nicolasawelsh",
    version="2020.6",
    author="Nicolas Welsh",
    author_email="nicolas.a.welsh@gmail.com",
    description="A package containing tools to deal with manipulations within ssh",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nicolasawelsh/sshtools.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
