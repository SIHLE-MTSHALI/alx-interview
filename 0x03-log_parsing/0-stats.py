#!/usr/bin/python3
"""Log parsing script that reads from stdin and computes metrics."""

import sys
import signal


def print_stats(file_size, status_codes):
    """Print the current statistics."""
    print("File size: {}".format(file_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    """Parse a single line of log."""
    try:
        parts = line.split()
        if len(parts) < 7:
            return None, None

        file_size = int(parts[-1])
        status_code = int(parts[-2])

        return file_size, status_code
    except (ValueError, IndexError):
        return None, None


def main():
    """Main function to process the log."""
    file_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    def signal_handler(sig, frame):
        """Handle the keyboard interruption signal."""
        print_stats(file_size, status_codes)
        sys.exit(0)

    # Register the signal handler
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            file_size_part, status_code_part = parse_line(line)
            if file_size_part is not None:
                file_size += file_size_part
                if status_code_part in status_codes:
                    status_codes[status_code_part] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(file_size, status_codes)

    except Exception:
        pass
    finally:
        print_stats(file_size, status_codes)


if __name__ == "__main__":
    main()
