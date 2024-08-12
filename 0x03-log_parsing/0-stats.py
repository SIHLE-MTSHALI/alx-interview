#!/usr/bin/python3
"""Log parsing script."""

import sys
import signal


def print_stats(total_size, status_codes):
    """Print the statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line, total_size, status_codes):
    """Parse a single line of log."""
    try:
        parts = line.split()
        size = int(parts[-1])
        status = int(parts[-2])
        if status in status_codes:
            status_codes[status] += 1
        return total_size + size
    except (ValueError, IndexError):
        return total_size


def main():
    """Main function to process the logs."""
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    def signal_handler(sig, frame):
        """Handle CTRL+C interrupt."""
        print_stats(total_size, status_codes)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            total_size = parse_line(line.strip(), total_size, status_codes)
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
