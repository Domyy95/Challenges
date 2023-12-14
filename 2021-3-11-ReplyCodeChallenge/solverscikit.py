import numpy as np
import os
from sklearn.cluster import DBSCAN

DIRPATH = os.path.dirname(os.path.realpath(__file__))


class Cluster:
    def __init__(self, buildings):
        self.buildings = buildings
        self.centroid_x = sum([b.x for b in buildings]) // len(buildings)
        self.centroid_y = sum([b.y for b in buildings]) // len(buildings)

    def avg_connection(self, average):
        total = 0
        for b in self.buildings:
            distance = abs(b.x - self.centroid_x) + abs(b.y - self.centroid_y)
            total += b.connection_s * average - b.latency * distance
        return total


class Building:
    def __init__(self, x, y, latency, connection_s):
        self.x = x
        self.y = y
        self.latency = latency
        self.connection_s = connection_s


class Antenna:
    def __init__(self, id, r, connection_s):
        self.id = id
        self.range = r
        self.connection_s = connection_s


class SolverDBScan:
    def __init__(self, file_name):
        self.file_name = file_name
        self.buildings = {}
        self.antennas = []
        self.antennas_positions = {}

        with open(f"{DIRPATH}/data/{file_name}.in", "r") as f:
            file_content = f.read().split("\n")

            # First line
            self.width = int(file_content[0].split(" ")[0])
            self.height = int(file_content[0].split(" ")[1])

            # Second line
            self.number_building = int(file_content[1].split(" ")[0])
            self.number_antennas = int(file_content[1].split(" ")[1])
            self.reward = int(file_content[1].split(" ")[2])

            # Buildings
            for i in range(2, 2 + self.number_building):
                x, y, latency, connection = [int(x) for x in file_content[i].split(" ")]
                self.buildings[str(x) + " " + str(y)] = Building(
                    x, y, latency, connection
                )

            # Antennas
            id_antennas = 0
            for i in range(
                2 + self.number_building,
                2 + self.number_building + self.number_antennas,
            ):
                latency, connection = [int(x) for x in file_content[i].split(" ")]
                self.antennas.append(Antenna(id_antennas, latency, connection))
                id_antennas += 1

        print()

    def solve(self):
        self.antennas.sort(key=lambda x: x.connection_s, reverse=True)

        antennas_for_cluster = [a for a in self.antennas if a.range > 0]
        antennas_for_single_buildings = [a for a in self.antennas if a.range == 0]

        magic_value = 0
        if self.file_name == "b":
            magic_value = 50
        elif self.file_name == "c":
            magic_value = 2
        elif self.file_name == "d":
            magic_value = 60
        elif self.file_name == "e":
            magic_value = 45
        elif self.file_name == "f":
            magic_value = 80

        remaining_buildings = [
            b for b in self.buildings.values() if b.connection_s <= magic_value
        ]
        buildings_for_dbscan = [
            b for b in self.buildings.values() if b.connection_s > magic_value
        ]

        c = {}
        X = np.array([[b.x, b.y] for b in buildings_for_dbscan])
        # eps = 2 seems nice
        dbscan = DBSCAN(eps=2.3, min_samples=2, metric="manhattan").fit(X)

        core_samples_mask = np.zeros_like(dbscan.labels_, dtype=bool)
        core_samples_mask[dbscan.core_sample_indices_] = True
        labels = dbscan.labels_

        for index, label in enumerate(labels):
            if c.get(label) is None:
                c[label] = []
            c[label].append(self.buildings[str(X[index, 0]) + " " + str(X[index, 1])])

        label = 0
        clusters = []
        for _ in range(len(c) - 1):
            clusters.append(Cluster(c[label]))
            label += 1

        antenna_avg = sum([x.connection_s for x in self.antennas]) // len(self.antennas)
        clusters.sort(key=lambda x: x.avg_connection(antenna_avg), reverse=True)

        # Cluster assignment
        current_cluster = None
        for index, clu in enumerate(clusters):
            if index < len(antennas_for_cluster):
                self.antennas_positions[antennas_for_cluster[index].id] = (
                    clu.centroid_x,
                    clu.centroid_y,
                )
            else:
                current_cluster = index
                break

        # The noise is the remaining buildings not assigned
        if -1 in c:
            remaining_buildings.extend(c[-1])

        # Some clusters may have not been assigned
        if len(self.antennas_positions) == len(antennas_for_cluster):
            for i in range(current_cluster, len(clusters)):
                remaining_buildings.extend(clusters[i].buildings)
        # Some antennas may have not been assigned
        else:
            antennas_for_single_buildings.extend(antennas_for_cluster[current_cluster:])

        # Sort
        remaining_buildings.sort(key=lambda x: x.connection_s, reverse=True)
        antennas_for_single_buildings.sort(key=lambda x: x.connection_s, reverse=True)

        for index, a in enumerate(antennas_for_single_buildings):
            if index >= len(remaining_buildings):
                break
            b = remaining_buildings[index]
            self.antennas_positions[antennas_for_single_buildings[index].id] = (
                b.x,
                b.y,
            )

    def to_output(self):
        with open(f"./out/{self.file_name}_out.txt", "w") as file:
            file.write(f"{len(self.antennas_positions)}\n")

            for id, pos in self.antennas_positions.items():
                file.write(f"{id} {pos[0]} {pos[1]}\n")
