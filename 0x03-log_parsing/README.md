# 0x03. Log Parsing

## Description
This project involves creating a script that reads log data from standard input (stdin), processes it, and computes metrics. The script parses input lines in a specific format, calculates the total file size, and counts occurrences of different HTTP status codes. It then prints these statistics every 10 lines and when interrupted by CTRL+C.

## File Structure
- `0-stats.py`: The main script that parses logs and computes metrics

## Usage
./0-generator.py | ./0-stats.py

## Functionality
- Reads input line by line from stdin
- Computes the total file size
- Counts occurrences of status codes (200, 301, 400, 401, 403, 404, 405, 500)
- Prints statistics every 10 lines and when interrupted by CTRL+C
- Handles keyboard interruption (CTRL+C) gracefully
