#!/usr/bin/env python3

SPACE: str = " "


def argify(argv: list[str]) -> tuple[int, list[str]]:
    """
    Takes as argument `sys.argv` and returns a tuple of its length and itself both without the script argument.

    Parameters:
        `argv: list[str]` -> the argument passed to your script

    Example:
        >>> argify(["my_script.py", "hello", "world", "3"])
        (3, ["hello", "world", 3]) 
    """
    return len(argv[1:]), argv[1:]


def concatenate(array: list[str]) -> str:
    if not isinstance(array, list):
        raise TypeError(
            "array must be of type list, not {}".format(type(array).__name__))

    for element in array:
        if not isinstance(element, str):
            raise TypeError(
                "found an element of type {} in an array of 'str'".format(type(element).__name__))
    
    return SPACE.join(array)


def spacify(message: str) -> str:
    return SPACE.join(list(message))
