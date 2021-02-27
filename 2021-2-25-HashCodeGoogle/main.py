import os
import numpy as np
from numba import jit
import tqdm
import sys
import shutil
import time

DIRPATH = os.path.dirname(os.path.realpath(__file__))


class Intersection:
    def __init__(self, id):
        self.id = id
        self.incoming = {}
        self.outbound = {}
        self.incoming_streets = []
        self.green_light_street = []

    def car_to_move(self, street_name):
        return self.incoming[street_name]["queue"].pop(0)

    def best_path(self):
        # Heuristic
        max_val = 0
        street_name = ""
        for i in self.incoming.values():
            if len(i["queue"]) > max_val:
                max_val = len(i["queue"])
                street_name = i["street_name"]

        self.green_light_street.append(street_name)

        return self.car_to_move(street_name) if max_val > 0 else None


class Street:
    def __init__(self, s_i, e_i, s_n, t_t):
        self.start_intersection = s_i
        self.end_intersection = e_i
        self.street_name = s_n
        self.travel_time = t_t


class Car:
    def __init__(self, id, n_s, s):
        self.next_street = 1
        self.id = id
        self.number_streets = n_s
        self.streets = s

    def is_finished(self):
        return self.next_street > len(self.streets)

    def get_current_street(self):
        return self.streets[self.next_street - 1]

    def get_arriving_intersection(self):
        return self.streets[self.next_street - 1].end_intersection


class Problem:
    def __init__(self, file_content):
        content = file_content.split("\n")

        first_line = content[0].split(" ")
        self.duration = int(first_line[0])
        self.number_intersections = int(first_line[1])
        self.number_streets = int(first_line[2])
        self.number_of_cars = int(first_line[3])
        self.bonus = int(first_line[4])

        self.intersections = {}
        self.streets = {}
        self.car_paths = []

        for i in range(1, self.number_streets + 1):
            line = content[i].split(" ")
            start_intersection = int(line[0])
            end_intersection = int(line[1])
            street_name = line[2]
            travel_time = int(line[3])
            self.streets[street_name] = Street(start_intersection, end_intersection, street_name, travel_time)

        counter = 0
        for i in range(1 + self.number_streets, 1 + self.number_streets + self.number_of_cars):
            line = content[i].split(" ")
            number_streets = int(line[0])
            streets = content[i][1 + len(str(number_streets)):].split(" ")
            new_streets = []
            for s in streets:
                new_streets.append(self.streets[s])

            self.car_paths.append(Car(counter, number_streets, new_streets))
            counter += 1
        return

    def create_data_structure(self):

        for i in range(self.number_intersections):
            self.intersections[i] = Intersection(i)

        for s in self.streets.values():
            self.intersections[s.start_intersection].outbound[s.end_intersection] = {
                "street_name": s.street_name,
                "travel_time": s.travel_time
            }

            self.intersections[s.end_intersection].incoming_streets.append(s.street_name)

            self.intersections[s.end_intersection].incoming[s.street_name] = {
                "queue": [],
                "street_name": s.street_name,
                "intersection": s.start_intersection
            }

        for i in self.intersections.values():
            for c in self.car_paths:
                if c.streets[0].street_name in i.incoming_streets:
                    i.incoming[c.streets[0].street_name]["queue"].append(c)

    def sgabole(self):
        streets_overall_count = {}

        for i in self.intersections.values():
            streets_overall_count[str(i.id)] = {}
            for s_name in i.incoming.keys():
                streets_overall_count[str(i.id)][s_name] = 0

        for c in self.car_paths:
            for s in c.streets:
                streets_overall_count[str(s.end_intersection)][s.street_name] += 1

        for i in self.intersections.values():
            counts = streets_overall_count[str(i.id)]

            for name, val in counts.items():
                i.green_light_street.extend([name] * val)

    def emulate(self):
        transferring_cars = {}

        for t in range(self.duration):

            if transferring_cars.get(t) is not None:
                for c in transferring_cars[t]:
                    self.intersections[c.get_arriving_intersection()] \
                        .incoming[c.get_current_street().street_name]["queue"] \
                        .append(c)

            for i in self.intersections.values():
                car = i.best_path()
                if car is not None:
                    car.next_street += 1
                    if car.is_finished():
                        del car
                    else:
                        if transferring_cars.get(t + car.get_current_street().travel_time) is None:
                            transferring_cars[t + car.get_current_street().travel_time] = []
                        transferring_cars[t + car.get_current_street().travel_time].append(car)

        print()

    def to_output(self):
        mega_counterone = 0
        with open(f".\\out\\temp.txt", "w") as file:
            for i in self.intersections.values():
                mega_counterone += 1

                from collections import Counter

                if len(i.green_light_street) == 0:
                    file.write(f"{i.id}\n")
                    file.write(f"1\n")
                    file.write(f"{i.incoming_streets[0]} 1\n")
                    continue

                file.write(f"{i.id}\n")
                file.write(f"{len(Counter(i.green_light_street).keys())}\n")
                val = i.green_light_street[0]

                counter = 0
                total = 0
                for g in i.green_light_street:
                    if g != val:
                        file.write(f"{val} {counter}\n")
                        total += counter
                        counter = 1
                        val = g
                    else:
                        counter += 1

                if len(i.green_light_street) == 1:
                    file.write(f"{i.green_light_street[0]} 1\n")
                elif total != len(i.green_light_street):
                    file.write(f"{val} {counter}\n")

        with open(f".\\out\\{sys.argv[1]}_out.txt", "w") as file:
            with open(f".\\out\\temp.txt", "r") as temp:
                file.write(f"{mega_counterone}\n")
                file.write(temp.read()[:-1])


def parse_input(file_name):
    with open(f"{DIRPATH}\\data\\{file_name}.txt", 'r') as f:
        return Problem(f.read())


if __name__ == '__main__':
    problem = parse_input(sys.argv[1])
    problem.create_data_structure()
    # problem.emulate()
    problem.sgabole()
    problem.to_output()
