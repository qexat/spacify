#!/usr/bin/env python3

from sys import argv

from api import argify, concatenate, spacify, exceptions


def main(argc: int, argv: list[str]) -> None:
    """
    Main program.

    Parameters:
        argc: int -> number of script arguments
        argv: list[str] -> list of script arguments

    Example:
        >>> python spacify Hello World!
        H e l l o   W o r l d !
    """

    if argc == 0:
        exceptions.error(exceptions.MissingRequiredArgs, 1, argc)
    
    processed: str = concatenate(argv)
    spacified: str = spacify(processed)

    print(spacified)

if __name__ == "__main__":
    main(*argify(argv))
