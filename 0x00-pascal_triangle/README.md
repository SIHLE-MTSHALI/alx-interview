# Pascal's Triangle

## Overview
This project implements a function to generate Pascal's Triangle in Python. Pascal's Triangle is a triangular array of the binomial coefficients that arises in probability theory, combinatorics, and algebra.

## Project Structure
- `0-pascal_triangle.py`: Contains the main function `pascal_triangle(n)` that generates Pascal's Triangle.
- `0-main.py`: A script to test the `pascal_triangle` function.

## Function Description
### `pascal_triangle(n)`
This function generates Pascal's Triangle up to n rows.

#### Parameters:
- `n` (int): The number of rows to generate in Pascal's Triangle.

#### Returns:
- List of lists: Each inner list represents a row in Pascal's Triangle.
- Returns an empty list if n <= 0.

#### Algorithm:
1. If n <= 0, return an empty list.
2. Initialize the triangle with the first row [1].
3. For each subsequent row:
   - Start and end the row with 1.
   - Calculate the middle elements by summing the two elements above it from the previous row.
4. Return the complete triangle.
