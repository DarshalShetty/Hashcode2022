from dataclasses import dataclass
from typing import Optional

from Contributor import Contributor
from Skill import Skill


@dataclass
class Role:
    skill: Skill
    contributor: Optional[Contributor] = None
