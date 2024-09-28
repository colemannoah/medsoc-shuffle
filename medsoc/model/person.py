from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Person:
    email: str
    year: str
    preferences: list[str]
    signup: str
    leader: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "email": self.email,
            "year": self.year,
            "preferences": self.preferences,
            "signup": self.signup,
            "leader": self.leader,
        }
