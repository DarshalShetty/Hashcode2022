from dataclasses import dataclass
from typing import List

from Role import Role


@dataclass
class Project:
    best_before: int
    time_taken: int
    name: str
    roles: List[Role]
    best_score: int
    roles: List

    def calculate_score(self, end_date):
        return self.best_score if end_date <= self.best_before else max(self.best_score-(end_date-self.best_before), 0)
