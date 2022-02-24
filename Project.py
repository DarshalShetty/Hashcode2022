from dataclasses import dataclass
from typing import List, Dict

from Contributor import Contributor
from Skill import Skill


@dataclass
class Project:
    best_before: int
    time_taken: int
    name: str
    skills: List[Skill]
    roles: Dict[Skill, Contributor]
    best_score: int
    roles: List
