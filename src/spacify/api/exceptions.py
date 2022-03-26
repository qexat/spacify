#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Callable


@dataclass
class ErrorType:
    name: str
    reason: Callable[[str], str]


MissingRequiredArgs = ErrorType(
    "MissingRequiredArgs", lambda expected, received: f"expected {expected} args, got {received}")


def error(__type: ErrorType, /, *args) -> None:
    print("\x1b[1;37;41m", __type.name, "\x1b[22;39;49m", __type.reason(*args))
    exit(1)
