# Hello World

This is an example project demonstrating how to publish a python module to PyPI.

## Use Virtualenv to customize Python

[Use Virtualenv to customize Python](https://kb.iu.edu/d/aonm)
Example:
```bash
virtualenv genomicsPython
source genomicsPython/bin/activate
which python
deactivate
```


## Installation

Run the following to install:

```python
pip install helloworld
```

## Usage

```python
from helloworld import say_hello

# Generate "Hello, World!"
say_hello()

# Generate "Hello, Everybody!"
say_hello("Everybody")
```

# Developing Hello World

To install helloworld, along with the tools you need to develop an run tests, run the following in your virtualenv:

```bash
$ pip install -e.[dev]
```

