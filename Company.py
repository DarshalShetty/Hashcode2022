from typing import List

from Contributor import Contributor
from Project import Project


class Company:
    def __init__(self, contributors: List[Contributor], projects: List[Project]):
        self.projects = {it.name: it for it in projects}
        self.current_score = 0

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
        for role, contributor in zip(project.roles, contributors):
            if not contributor.can_assign_project(project, role):
                for prev_contributor in contributors:
                    prev_contributor.rollback()
                return False
        for role, contributor in zip(project.roles, contributors):
            contributor.commit_assignment()
            role.contributor = contributor
        return True

    def assign_projects(self):
        pass
