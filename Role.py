from dataclasses import dataclass

from Contributor import Contributor
from Skill import Skill
from typing import Optional


@dataclass
class Role:
    skill: Skill
    contributor: Optional[Contributor] = None
