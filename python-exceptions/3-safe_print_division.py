#!/usr/bin/python3


def safe_print_division(a, b):
    result = None
    try:
        result = a/b
        print(a/b)
    except (TypeError, ValueError, ZeroDivisionError):
        pass
    finally:
        print("Result: {}".format(result))
    return result    
