from collections import defaultdict
from typing import List

# from Project import Project
# from Role import Role
from Skill import Skill


class Contributor:

    def __init__(self, name, skills: List[Skill]):
        self.name = name
        self.available_from = 0
        self._possible_available_from = 0
        self.skill_index = defaultdict(int, {it.name: it.level for it in skills})
        self._level = None
        self._skill_name = None

    def can_assign_project(self, project, role):
        """ Returns successful_assignment"""
        self._skill_name = role.skill.name
        self._level = role.skill.level
        if self._skill_name in self.skill_index:
            role.contributor = self
            self._possible_available_from = project.time_taken + self.available_from
            return self._possible_available_from
        else:
            return False

    def commit_assignment(self):
        if self._level - 1 == self.skill_index.get(self._skill_name):
            self.skill_index[self._skill_name] += 1
        self.available_from = self._possible_available_from
        self._skill_name = None
        self._level = None

    def rollback(self):
        self._possible_available_from = self.available_from
        self._skill_name = None
        self._level = None

    def can_mentor(self, skill: Skill):
        return self.skill_index.get(skill.name) >= skill.level
