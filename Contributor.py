from typing import List

from Project import Project
from Role import Role
from Skill import Skill

from collections import defaultdict


class Contributor:

    def __init__(self, skills: List[Skill]):
        self.available_from = 0
        self.possible_available_from = 0
        self.skill_index = defaultdict(0, {it.name: it.level for it in skills})
        self.level = None
        self.skill_name = None

    def can_assign_project(self, project: Project, role: Role):
        """ Returns successful_assignment"""
        self.skill_name = role.skill.name
        self.level = role.skill.level
        if self.skill_name in self.skill_index:
            role.contributor = self
            self.possible_available_from = project.time_taken+self.available_from
            return True
        else:
            return False

    def commit_assignment(self):
        if self.level - 1 == self.skill_index.get(self.skill_name):
            self.skill_index[self.skill_name] += 1
        self.available_from = self.possible_available_from
        self.skill_name = None
        self.level = None

    def rollback(self):
        self.possible_available_from = self.available_from
        self.skill_name = None
        self.level = None

    def can_mentor(self, skill:Skill):
        return self.skill_index.get(skill.name)>=skill.level
