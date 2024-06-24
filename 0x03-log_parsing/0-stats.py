#!/usr/bin/python3
"""
This module contains the solution of the log parsing problem.
"""

import sys
import signal
import re
import os

counter = 0
file_size = 0
status_codes = {}

def get_result(singrun=None, frame=None):
    """Handle SIGINT signal by printing current stats."""
    global counter
    counter = 0

    print(f"File size: {file_size}")
    for key, value in sorted(status_codes.items()):
        print(f"{key}: {value}")

signal.signal(signal.SIGINT, get_result)

def main():
    """Main function to process log lines from stdin."""
    global counter, file_size, status_codes

    for line in sys.stdin:
        match = re.match(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) *- *\[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$', line)
        if not match:
            continue

        status, size = match.group(3), int(match.group(4))

        counter += 1
        status_codes[status] = status_codes.get(status, 0) + 1
        file_size += size

        if counter == 10:
            get_result()
    get_result()

if __name__ == "__main__":
    main()
