from typing import List

from Project import Project
from Role import Role
from Skill import Skill


class Contributor:

    def __init__(self, skills: List[Skill]):
        self.available_from = 0
        # self.skills = skills
        self.skill_index = {it.name: it.level for it in skills}

    def assign_project(self, project: Project, role: Role):
        """ Returns successful_assignment and mentor_needed """
        name = role.skill.name
        level = role.skill.level
        if name in self.skill_index:
            role.contributor = self
            self.available_from += project.time_taken
            if level - 1 == self.skill_index[name]:
                self.skill_index[name] += 1
                return True, True
            else:
                return True, False
        else:
            return False, None

