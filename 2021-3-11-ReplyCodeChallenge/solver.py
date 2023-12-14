import numpy
import os
from collections import Counter
from collections import deque
import random

DIRPATH = os.path.dirname(os.path.realpath(__file__))


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


class Solver:
    def __init__(self, file_name):
        self.file_name = file_name
        self.buildings = []
        self.antennas = []
        self.antennas_positions = {}

        with open(f"{DIRPATH}\\data\\{file_name}.in", "r") as f:
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
                self.buildings.append(Building(x, y, latency, connection))

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
        grid = []

        self.buildings.sort(key=lambda x: x.connection_s, reverse=True)
        self.antennas.sort(key=lambda x: x.connection_s, reverse=True)

        for index, b in enumerate(self.buildings):
            if index < len(self.antennas):
                self.antennas_positions[self.antennas[index].id] = (b.x, b.y)

    def to_output(self):
        with open(f".\\out\\{self.file_name}_out.txt", "w") as file:
            file.write(f"{len(self.antennas_positions)}\n")

            for id, pos in self.antennas_positions.items():
                file.write(f"{id} {pos[0]} {pos[1]}\n")
