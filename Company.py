from typing import List

from Contributor import Contributor
from Project import Project


class Company:
    def __init__(self, contributors: List[Contributor], projects: List[Project]):
        self.projects = {it.name: it for it in projects}
        self.contributors = {it.name: it for it in contributors}
        self.current_score = 0
        self.skill_lookup = self._index_skills()

    @staticmethod
    def _index_skills():

        return {}

    def assign_project(self, project_name: str, contributors: List[Contributor]):
        project: Project = self.projects.get(project_name, None)
        if project is None:
            return False
        elif len(project.roles) != len(contributors):
            return False
        for role in project.roles:
            for contributor in contributors:
                if contributor.can_mentor(role.skill):
                    break
            else:
                return False
        tot_end = 0
        for role, contributor in zip(project.roles, contributors):
            curr_end = contributor.can_assign_project(project, role)
            if curr_end:
                tot_end = max(tot_end, curr_end)
            else:
                for prev_contributor in contributors:
                    prev_contributor.rollback()
                return False
        for role, contributor in zip(project.roles, contributors):
            contributor.commit_assignment()
            role.contributor = contributor
        return project.calculate_score(tot_end)

    def assign_projects(self):
        for p in self.projects:
            best_contribs = self.best_match(p)
            self.assign_project(p, best_contribs)

    def best_match(self, project: Project):
        return []
