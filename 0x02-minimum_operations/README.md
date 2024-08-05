# 0x02. Minimum Operations

This project contains a Python implementation of an algorithm to calculate the minimum number of operations needed to achieve a given number of characters in a text file, using only "Copy All" and "Paste" operations.

## Files

- `0-minoperations.py`: Contains the implementation of the `minOperations` function.

## Requirements

- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 style (version 1.7.x)

## Usage

```python
minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
