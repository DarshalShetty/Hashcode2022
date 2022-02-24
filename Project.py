from dataclasses import dataclass
from typing import List, Dict

from Contributor import Contributor
from Role import Role
from Skill import Skill


@dataclass
class Project:
    best_before: int
    time_taken: int
    name: str
    roles: List[Role]
    best_score: int
    roles: List
