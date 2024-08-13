#!/usr/bin/python3
"""Log parsing script that reads from stdin and computes metrics."""

import sys


def print_stats(file_size, status_codes):
    """Print the current statistics."""
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """Main function to process the log."""
    file_size = 0
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) > 6:
                size = parts[-1]
                code = parts[-2]
                if code in status_codes:
                    status_codes[code] += 1
                try:
                    file_size += int(size)
                except ValueError:
                    pass
            line_count += 1
            if line_count % 10 == 0:
                print_stats(file_size, status_codes)

    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise

    print_stats(file_size, status_codes)


if __name__ == "__main__":
    main()
