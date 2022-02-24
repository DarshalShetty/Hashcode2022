from dataclasses import dataclass

from Contributor import Contributor
from Skill import Skill


@dataclass
class Role:
    name: str
    skill: Skill
    contributor: Contributor
