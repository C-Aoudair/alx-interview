#!/usr/bin/python3
""" This module contains the solution of the utf8 validation problem"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    for char in data:
        if char <= 127:
            continue
        else:
            return False
    return True
