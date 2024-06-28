#!/usr/bin/python3
""" This module contains the solution of the utf8 validation problem"""

def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    i = 0
    while i < len(data):
        if data[i] >> 7 == 0:  # 1-byte character (ASCII)
            i += 1
        elif data[i] >> 5 == 0b110:  # 2-byte character
            if i + 1 >= len(data) or data[i + 1] >> 6 != 0b10:
                return False
            i += 2
        elif data[i] >> 4 == 0b1110:  # 3-byte character
            if i + 2 >= len(data) or data[i + 1] >> 6 != 0b10 or data[i + 2] >> 6 != 0b10:
                return False
            i += 3
        elif data[i] >> 3 == 0b11110:  # 4-byte character
            if i + 3 >= len(data) or data[i + 1] >> 6 != 0b10 or data[i + 2] >> 6 != 0b10 or data[i + 3] >> 6 != 0b10:
                return False
            i += 4
        else:
            return False
    return True
