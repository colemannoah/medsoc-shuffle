import random

from constants import constants
from model.person import Person


class MedSocShuffle:
    def __init__(self, people_array: list[Person]) -> None:
        self._people_array = people_array
        self._seed = random.randint(0, 1000)
        random.seed(self._seed)

    def run(self) -> dict[str, list[str]]:
        assignments = {loc: [] for loc in constants.LOCATION_COLS}
        _assigned_leaders = self._assign_group_leaders(assignments)
        _assigned_members = self._assign_group_members(_assigned_leaders)

        return _assigned_members

    def _assign_group_leaders(self, assignments: dict[str, list[str]]) -> Person:
        pool = [
            person
            for person in self._people_array
            if person.leader or person.year in ["GEM2", "UEM3 (2nd med)"]
        ]
        random.shuffle(pool)

        for person in pool:
            for loc in person.preferences:
                if len(assignments[loc]) < constants.LOCATION_LIMITS[loc]["leaders"]:
                    assignments[loc].append(person.email)
                    break

        return assignments

    def _assign_group_members(
        self, assignments: dict[str, list[str]]
    ) -> dict[str, list[str]]:
        limits = constants.LOCATION_LIMITS
        flat_assignments = [
            email for sublist in assignments.values() for email in sublist
        ]
        pool = [
            person for person in self._people_array if person not in flat_assignments
        ]
        random.shuffle(pool)

        for person in pool:
            for loc in person.preferences:
                if (
                    len(assignments[loc]) < limits[loc]["people"]
                    and person.email not in assignments[loc]
                ):
                    assignments[loc].append(person.email)
                    break

        return assignments
