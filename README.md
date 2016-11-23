Triangle Checker
================

Small app to check the type of triangle

Requirement
-----------

Python 3

Installation
------------

```bash
pip3 install -e git+https://github.com/butomo1989/triangle.git#egg=triangle
```

Help
----

```bash
triangle -h
```

Usage
-----

triangle check ***first_length*** ***second_length*** ***third_length***

Example:

```bash
triangle check 3 4 5
```

The output will be:

```bash
Scalene
```

Unit tests
----------

Run the unit tests with this command:

```bash
nosetests -v
```
