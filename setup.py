import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
setup(
    name="credo-python",
    version="1.0.0",
    description="A Python Wrapper for the Credo API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/BdVade/credo-python",
    author="Aderibigbe Victor",
    author_email="victoraderibigbe03@gmail.com",
    keywords = ['credo', 'python', 'sdk'],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools'
    ],
    packages=["credo"],
    include_package_data=True,
    install_requires=['requests'],

)