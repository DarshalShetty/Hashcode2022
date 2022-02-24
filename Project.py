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
