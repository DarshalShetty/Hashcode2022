from Company import Company
from Contributor import Contributor
from Project import Project
from Role import Role
from Skill import Skill


def parse_input(file):
    cont_num_str, proj_num_str = file.readline().split()
    cont_num = int(cont_num_str)
    proj_num = int(proj_num_str)

    contributors = []
    projects = []

    for _ in range(cont_num):
        cotrib_name, skill_num_str = file.readline().split()
        skill_num = int(skill_num_str)
        skills = []
        for _ in range(skill_num):
            name, level_str = file.readline().split()
            level = int(level_str)
            skills.append(Skill(name, level))
        contributors.append(Contributor(cotrib_name, skills))

    for _ in range(proj_num):
        name, days_taken_str, best_score_str, best_before_str, num_roles_str = file.readline().split()
        days_taken = int(days_taken_str)
        best_score = int(best_score_str)
        best_before = int(best_before_str)
        num_roles = int(num_roles_str)

        roles = []
        for _ in range(num_roles):
            skill_name, level_str = file.readline().split()
            level = int(level_str)
            roles.append(Role(Skill(skill_name, level)))

        projects.append(Project(best_before, days_taken, name, roles, best_score))

    return projects, contributors


in_file_name = "data/a_an_example.in.txt"

if __name__ == '__main__':
    with open(in_file_name, 'r') as in_file:
        projects, contributors = parse_input(in_file)
        c = Company(contributors, projects)
        c.assign_projects()
