from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='helloworld',
    version='0.0.1',
    description='Say hello!',
    py_modules=["helloworld"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLV2+)",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    extras_require = {
        "dev": [
            "pytest>=3.7",
        ],
    },
    url="https://github.com/brykim/demo-pypi-package",
    author="Bryant J Kim",
    author_email="brykim@iu.edu",
)