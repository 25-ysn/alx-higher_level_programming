#!/usr/bin/python3
import sys


def safe_function(fn, *ag):
    try:
        result = fn(*ag)
        return result
    except (ValueError, ZeroDivisionError, TypeError, IndexError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
