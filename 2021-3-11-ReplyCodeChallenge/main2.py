# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import numpy as np
import sys
import shutil
import time

import pandas as pd

from copy import deepcopy

import matplotlib
import matplotlib.pyplot as plt

import sklearn

from sklearn.cluster import MiniBatchKMeans

DIRPATH = os.path.dirname(os.path.realpath(__file__))

class Position:
    def __init__(self, x, y):
        self.x, self.y = x, y

class Building:
    def __init__(self, x, y, latency, connection):
        self.x, self.y, self.latency, self.connection = x, y, latency, connection

class Antenna:
    def __init__(self, id, range, connection_speed):
        self.id, self.range, self.connection_speed = id, range, connection_speed
        self.x, self.y = None, None

class Assignment:
    def __init__(self, id_a, x, y):
        self.id_a, self.x, self.y = id_a, x, y

class Solution:
    def __init__(self, assignments, file_name):
        self.assignments = assignments
        self.file_name = file_name

    def to_output(self):
        with open(f"./out/{self.file_name}_out.txt", "w") as file:
            file.write(f"{len(self.assignments)}\n")

            for a in self.assignments:
                file.write(f"{a.id_a} {int(a.x)} {int(a.y)}\n")

class Problem:
    def __init__(self, file_content):
        global range
        content = file_content.split("\n")

        first_line = content[0].split(" ")
        self.width, self.height = int(first_line[0]), int(first_line[1])
        second_line = content[1].split(" ")

        self.num_buildings, self.num_antennas, self.reward = int(second_line[0]), int(second_line[1]), int(second_line[2])

        buildings = []
        vals_df = []  # pd.DataFrame()
        for n_b in range(self.num_buildings):
            vals_line_n = content[n_b + 2].split(" ")
            current_building = [int(val) for val in vals_line_n]
            x, y, latency, connection = current_building
            buildings.append(Building(x, y, latency, connection))
            vals_df.append({"x": x, "y": y, "lat": latency, "connection": connection})
            # buildings_matrix = np.vstack((buildings_matrix, np.array(current_building)))

        self.buildings = buildings
        self.buildings_df = pd.DataFrame(vals_df)

        antennas = []
        vals_df = []
        for n_a in range(self.num_antennas):
            vals_line_n = content[self.num_buildings + 2 + n_a].split(" ")
            current_antenna = [int(val) for val in vals_line_n]
            range, connection_speed = current_antenna
            antennas.append(Antenna(n_a, range, connection_speed))
            vals_df.append({"range": range, "connection_speed": connection_speed})
            # antennas_matrix = np.vstack((antennas_matrix, np.array(current_antenna)))

        self.antennas = antennas
        self.antennas_df = pd.DataFrame(vals_df)

        return

    def solve(self, problem):

        # TODO kmeans: k = #antennas, buildings = ... e dammi in centroidi

        model = MiniBatchKMeans(n_clusters=self.num_antennas)

        predictions = model.fit_predict(self.buildings_df[['x', 'y']])
        centroids = [Position(int(c[0]), int(c[1])) for c in model.cluster_centers_]
        assignments = []
        for idx_building, p in enumerate(predictions):
            # TODO prova assignments.append({"a": p, "b": idx_building})
            building = self.buildings[idx_building]
            assignments.append({'id_a': p, 'id_b': idx_building, "b_x": building.x, "b_y": building.y, \
                                "b_latency": building.latency, \
                                "b_connection": building.connection, \
                                "x_a": centroids[p].x, "y_a": centroids[p].y})

        # TODO raggruppo per id antenna, e prendo i building; per ogni building, prendo distanza da centroide
        df_pair = pd.DataFrame(assignments)
        antennas_sorted_per_building = df_pair.groupby(by='id_a').mean().sort_values(by='b_connection')
        antennas_sorted_per_antenna = sorted(self.antennas, key=lambda x: x.connection_speed)
        antennas_solutions = {}
        for id_a in antennas_sorted_per_building.index:
            x_a, y_a = antennas_sorted_per_building.loc[id_a]['x_a'], antennas_sorted_per_building.loc[id_a]['y_a']
            buildings = df_pair.loc[df_pair['id_a'] == id_a].index
            id_antenna_real = antennas_sorted_per_antenna[id_a].id
            antennas_solutions[id_antenna_real] = (x_a, y_a)#(buildings, centroids[id_a])

        solutions = []
        for id_a in antennas_solutions.keys():
            position = antennas_solutions[id_a]
            solutions.append(Assignment(id_a, position[0], position[1]))

        self.solution = Solution(solutions, problem)



    def to_output(self, problem):
        self.solve(problem)
        self.solution.to_output()
        #shutil.make_archive(f"{problem_name}_{time.time()}", 'zip')
        return


def parse_input(file_name):
    with open(f"{DIRPATH}/data/{file_name}.in", 'r') as f:
        return Problem(f.read())


if __name__ == '__main__':
    filename = sys.argv[1]
    problem = parse_input(filename)

    problem.to_output(filename)
