#!/usr/bin/python3
"""
This module contains the solution of the log parsing problem.
"""
import sys
import signal
import re
import os


counter = 0
fileSize = 0
statusCodes = {}


def get_status(signum, frame):
    """ print the actual values of the fileSize and statusCodes"""
    global counter
    counter = 0
    print(f"File size: {fileSize}")
    for key, value in sorted(statusCodes.items()):
        print(f"{key}: {value}")


signal.signal(signal.SIGINT, get_status)


def main():
    """ the main function"""
    for line in sys.stdin:
        x = re.search(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$', line)

        if not x:
            continue

        data = re.findall(r'(\d{3}) (\d+)$', line)
        status = data[0][0]
        size = data[0][1]

        global counter
        global fileSize
        global statusCodes
        counter += 1
        if statusCodes.get(status):
            statusCodes[status] += 1
        else:
            statusCodes[status] = 1
        fileSize += int(size)

        if counter == 10:
            os.kill(os.getpid(), signal.SIGINT)


if __name__ == "__main__":
    main()
