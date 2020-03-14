import os
import numpy as np
import tqdm
import sys

DIRPATH = os.path.dirname(os.path.realpath(__file__))

class Problem:
    def __init__(self, width, height, map_office, developers, project_managers):
        self.width = width
        self.height = height
        self.mapOffice = map_office
        self.developers = developers
        self.project_managers = project_managers
        self.number_dev = len(developers)
        self.number_pm = len(project_managers)

        self.selected_developers = {}
        self.selected_project_managers = {}

    def highest_compatibility_dev(self, boi):
        # If same company, boi.bonus * anon.bonus
        # len(Int skill) * len(skill not in common)
        return sorted(self.developers,
                      key=lambda x: len(boi.skills.intersection(x.skills)) *
                                    len(boi.skills.union(x.skills) - boi.skills.intersection(x.skills)) +
                                    (boi.bonus * x.bonus if boi.company == x.company else 0),
                      reverse=True)[0:4]

    def highest_compatibility_pm(self, boi):
        # If same company, boi.bonus * anon.bonus
        return sorted(self.project_managers,
                      key=lambda x: (boi.bonus * x.bonus if boi.company == x.company else 0),
                      reverse=True)[0:4]

    def get_output_file(self):
        output = ""
        for index_sdev in range(0, self.number_dev):
            if index_sdev in list(self.selected_developers):
                output += "{} {}\n".format(self.selected_developers[index_sdev][0], self.selected_developers[index_sdev][1])
            else:
                output += "X\n"
        for index_spm in range(0, self.number_pm):
            if index_spm in list(self.selected_project_managers):
                output += "{} {}\n".format(self.selected_project_managers[index_spm][0], self.selected_project_managers[index_spm][1])
            else:
                output += "X\n"

        with open("OUT" + sys.argv[1], 'w') as f:
            f.write('{}'.format(output))


class Node:
    def __init__(self, x, y, position):
        self.x = x
        self.y = y
        self.position = position  # "_" or "M"
        self.id_selected = -1
        self.siblings = []


class Developer:
    def __init__(self, id, company, bonus, skills):
        self.id = id
        self.company = company
        self.bonus = bonus
        self.skills = skills


class ProjectManager:
    def __init__(self, id, company, bonus):
        self.id = id
        self.company = company
        self.bonus = bonus
        self.skills = set([])


def parse_input(file):
    map_office = []
    developers = {}
    project_managers = {}
    height = 0
    developer_id = 0
    project_manager_id = 0
    number_developers = 100001
    number_project_managers = 0

    with open(file, 'r') as f:
        for i, line in enumerate(f):
            if i == 0:
                values = line.split(' ')
                width = int(values[0])
                height = int(values[1])
            elif 1 <= i < height + 1: #MAP
                values = line.rstrip()
                for x in range(0, len(values)):
                    if values[x] != "#":
                        new_node = Node(x, i-1, values[x])

                        for n in map_office:
                            if (n.x == x ) and (n.y - 1 == i-1):
                                new_node.siblings.append(n)
                                n.siblings.append(new_node)

                            if(n.x == x ) and (n.y + 1 == i-1):
                                new_node.siblings.append(n)
                                n.siblings.append(new_node)

                            if(n.y == i-1 ) and (n.x - 1 == x):
                                new_node.siblings.append(n)
                                n.siblings.append(new_node)

                            if (n.y == i - 1) and (n.x + 1 == x):
                                new_node.siblings.append(n)
                                n.siblings.append(new_node)

                        map_office.append(new_node)

            elif height + 1 <= i < height + 2 + number_developers: #DEV
                if number_developers == 100001:
                    number_developers = int(line)
                else:
                    values = line.rstrip().split(' ')

                    developers[developer_id] = \
                        Developer(developer_id, values[0], int(values[1]), skills=set(values[3: len(values)]))
                    developer_id += 1
            else:
                if number_project_managers == 0:
                    number_project_managers = int(line)
                else:
                    values = line.split(' ')
                    project_managers[project_manager_id] = ProjectManager(project_manager_id, values[0], int(values[1]))
                    project_manager_id += 1

    return Problem(width, height, map_office, developers, project_managers)



if __name__ == '__main__':
    data = parse_input(sys.argv[1])

    data.mapOffice = sorted(data.mapOffice, key=lambda x: len(x.siblings), reverse=True)

    data.developers = [v for k, v in sorted(data.developers.items(), key=lambda item: len(item[1].skills), reverse=True)]
    data.project_managers = [v for k, v in sorted(data.project_managers.items(), key=lambda item: item[1].bonus, reverse=True)]

    score = 1

    while score != 0 and len(data.mapOffice) != 0:
        data.mapOffice = sorted(data.mapOffice, key=lambda x: len(x.siblings), reverse=True)

        selected_node = data.mapOffice.pop()

        if selected_node.id_selected != -1:
            continue

        if selected_node.position == "_":
            if len(data.developers) == 0:
                continue
            boi = data.developers.pop()
            data.selected_developers[boi.id] = [selected_node.x, selected_node.y]
        else:
            if len(data.project_managers) == 0:
                continue
            boi = data.project_managers.pop()
            data.selected_project_managers[boi.id] = [selected_node.x, selected_node.y]

        selected_node.id_selected = boi.id

        besties_devs = data.highest_compatibility_dev(boi)
        besties_pm = data.highest_compatibility_pm(boi)

        # check score
        if len(besties_devs) > 0:
            score_dev = (len(boi.skills.intersection(besties_devs[0].skills)) *
                len(boi.skills.union(besties_devs[0].skills) - boi.skills.intersection(besties_devs[0].skills)) +
                 (boi.bonus * besties_devs[0].bonus if boi.company == besties_devs[0].company else 0))
        else:
            score_dev = 0

        if len(besties_pm) > 0:
            score_pm = (boi.bonus * besties_pm[0].bonus if boi.company == besties_pm[0].company else 0)
        else:
            score_pm = 0

        score = max(score_dev, score_pm)

        if score == 0:
            break

        for s in selected_node.siblings:
            if s.id_selected == -1:
                if s.position == "_":
                    if len(besties_devs) > 0:
                        best_dev = besties_devs.pop()
                        s.id_selected = best_dev.id
                        data.selected_developers[best_dev.id] = [s.x, s.y]
                        data.developers.remove(best_dev)
                    else:
                        continue
                else:
                    if len(besties_pm) > 0:
                        best_pm = besties_pm.pop()
                        s.id_selected = best_pm.id
                        data.selected_project_managers[best_pm.id] = [s.x, s.y]
                        data.project_managers.remove(best_pm)
                    else:
                        continue
                data.mapOffice.remove(s)

            if len(data.mapOffice) == 0:
                break


    data.get_output_file()
