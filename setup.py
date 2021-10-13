import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

from docopt import __version__


class PyTestCommand(TestCommand):
    """ Command to run unit py.test unit tests
    """

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run(self):
        import pytest

        rcode = pytest.main(self.test_args)
        sys.exit(rcode)


setup(
    name="docopt-ng",
    version=__version__,
    maintainer="itdaniher",
    maintainer_email="itdaniher@gmail.com",
    description="Humane command line arguments parser. Now with maintenance, typehints, and complete test coverage.",
    license="MIT",
    keywords="option arguments parsing optparse argparse getopt docopt docopt-ng",
    url="https://github.com/jazzband/docopt-ng",
    py_modules=["docopt"],
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
    tests_require=["pytest"],
    cmdclass={"test": PyTestCommand},
)
