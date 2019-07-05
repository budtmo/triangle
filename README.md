Triangle Checker
================

[![Build Status](https://travis-ci.org/budtmo/triangle.svg?branch=master)](https://travis-ci.org/budtmo/triangle)
[![codecov](https://codecov.io/gh/budtmo/triangle/branch/master/graph/badge.svg)](https://codecov.io/gh/budtmo/triangle)
[![Build Status](https://dev.azure.com/budtmoos/budtmoos/_apis/build/status/budtmo.triangle?branchName=master)](https://dev.azure.com/budtmoos/budtmoos/_build/latest?definitionId=1&branchName=master)

Small app to check the type of triangle

Requirement
-----------

Python 3

Installation
------------

```bash
pip3 install -e git+https://github.com/budtmo/adefa /triangle.git#egg=triangle
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
