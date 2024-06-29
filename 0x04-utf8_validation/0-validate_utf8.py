#!/usr/bin/python3
""" This module contains the solution of the utf8 validation problem"""


def validUTF8(data: list) -> bool:
    """Determines if a given data set represents a valid UTF-8 encoding"""

    def is_continuation_byte(byte):
        return (byte >> 6) == 0b10

    numOfBytes = 0  # The number of bytes that the each utf8 character will be

    for byte in data:
        byte = byte & 0xFF  # Ensure that the byte is less than 255

        if numOfBytes == 0:  # Recognize the utf-8 bytes pattern

            if (byte >> 5) == 0b110:  # For two bytes
                numOfBytes = 1
            elif (byte >> 4) == 0b1110:  # For three bytes
                numOfBytes = 2
            elif (byte >> 3) == 0b11110:  # For four bytes
                numOfBytes = 3
            elif byte >> 7:
                return False

        else:
            if not is_continuation_byte(byte):
                return False
            numOfBytes -= 1

    return numOfBytes == 0  # Ensure that all continuation bytes was checked
