from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    email: str
    year: str
    preferences: list[str]
    signup: str
    leader: bool
