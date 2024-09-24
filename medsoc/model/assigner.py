import random

from typing import cast, Any
from constants import constants
from model.person import Person


class MedSocShuffle:
    def __init__(self, people_array: list[Person]) -> None:
        self._people_array = people_array
        self._seed = random.randint(0, 10000)
        random.seed(self._seed)

    def run(self) -> dict[str, Any]:
        assignments: dict[str, list[str]] = {loc: [] for loc in constants.LOCATION_COLS}
        _assigned_leaders = self._assign_group_leaders(assignments)
        _assigned_members = self._assign_group_members(_assigned_leaders)

        return _assigned_members

    def _assign_group_leaders(
        self, assignments: dict[str, list[str]]
    ) -> dict[str, list[str]]:
        limits = constants.LOCATION_LIMITS
        pool = [person for person in self._people_array if person.leader]
        random.shuffle(pool)

        for person in pool:
            for loc in person.preferences:
                if (
                    len(assignments[loc]) < cast(int, limits[loc]["leaders"])
                    and person.email not in assignments[loc]
                ):
                    assignments[loc].append(person.email)
                    pool.remove(person)
                    break

        pool = [
            person
            for person in self._people_array
            if person.year in ["GEM2", "UEM3 (2nd med)"]
        ]
        random.shuffle(pool)

        for person in pool:
            for loc in person.preferences:
                if (
                    len(assignments[loc]) < cast(int, limits[loc]["leaders"])
                    and person.email not in assignments[loc]
                ):
                    assignments[loc].append(person.email)
                    pool.remove(person)
                    break

        return assignments

    def _assign_group_members(
        self, assignments: dict[str, list[str]]
    ) -> dict[str, Any]:
        limits = constants.LOCATION_LIMITS
        runs = constants.MAX_RUNS
        flat_assignments = [
            email for sublist in assignments.values() for email in sublist
        ]
        pool = [
            person
            for person in self._people_array
            if person.email not in flat_assignments
        ]

        while runs >= 0 and pool:
            random.shuffle(pool)
            runs -= 1

            for person in pool:
                for loc in person.preferences:
                    if (
                        len(assignments[loc]) < cast(int, limits[loc]["people"])
                        and person.email not in assignments[loc]
                    ):
                        assignments[loc].append(person.email)
                        pool.remove(person)
                        break

        # Check for duplicates
        for loc in assignments:
            if len(assignments[loc]) != len(set(assignments[loc])):
                print(f"Duplicate in {loc}")

        return {"assignments": assignments, "leftovers": pool, "seed": self._seed}
