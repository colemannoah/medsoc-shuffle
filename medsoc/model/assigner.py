import random

from constants import constants
from model.person import Person


class MedSocShuffle:
    def __init__(self, people_array: list[Person]) -> None:
        self._people_array = people_array
        self._seed = random.randint(0, 10000)
        random.seed(self._seed)

    def run(self) -> dict[str, list[dict]]:
        assignments: dict[str, list[dict]] = {
            loc: [] for loc in list(constants.LOCATION_LIMITS.keys())
        }
        _assigned_leaders = self._assign_group_leaders(assignments)
        _assigned_members = self._assign_group_members(_assigned_leaders)

        return _assigned_members

    def _assign_group_leaders(
        self, assignments: dict[str, list[Person]]
    ) -> dict[str, list[Person]]:
        limits = constants.LOCATION_LIMITS
        pool = [person for person in self._people_array if person.leader]
        random.shuffle(pool)

        for person in pool:
            for loc in person.preferences:
                n = len(limits[loc])

                if len(assignments[loc]) < n and person not in assignments[loc]:
                    assignments[loc].append(person)
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
                n = len(limits[loc])
                if len(assignments[loc]) < n and person not in assignments[loc]:
                    assignments[loc].append(person)
                    pool.remove(person)
                    break

        return assignments

    def _assign_group_members(
        self, assignments: dict[str, list[Person]]
    ) -> dict[str, list[dict]]:
        limits = constants.LOCATION_LIMITS
        runs = constants.MAX_RUNS
        flat_assignments = [
            person.email for loc in assignments for person in assignments[loc]
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
                un_leadered = Person(
                    person.email,
                    person.year,
                    person.preferences,
                    person.signup,
                    False,
                )

                for loc in person.preferences:
                    n = len(limits[loc])
                    if (
                        len(assignments[loc]) < (n * 5)
                        and un_leadered.email
                        not in [person.email for person in assignments[loc]]
                        and person in pool
                    ):
                        assignments[loc].append(un_leadered)
                        pool.remove(person)
                        break

        # Check for duplicates
        for loc in assignments:
            if len(assignments[loc]) != len(
                set([person.email for person in assignments[loc]])
            ):
                print(f"Duplicate in {loc}")

        # Check is someone has been assigned twice
        for person in self._people_array:
            count = 0
            for loc in assignments:
                if person.email in [p.email for p in assignments[loc]]:
                    count += 1
            if count > 1:
                print(f"Person {person.email} has been assigned {count} times")

        results = {
            loc: [person.to_dict() for person in assignments[loc]]
            for loc in assignments
        }

        return {"assignments": results, "leftovers": pool, "seed": self._seed}
