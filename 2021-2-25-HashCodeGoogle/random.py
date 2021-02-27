import os
import numpy as np
from numba import jit
import tqdm
import random
import sys
import shutil
import time

DIRPATH = os.path.dirname(os.path.realpath(__file__))


class Intersection:
    def __init__(self, id):
        self.id = id
        self.incoming = []
        self.outbound = []
        self.queues = {}   # 1 queue for each incoming

    def add_car(self, car):
        self.queues[car.actual_street].append(car)

    def someone_in_queue(self):
        for q in self.queues:
            if len(self.queues[q]) > 0:
                return True

        return False

    def find_who_shall_pass(self):
        max = 0
        street_inc = 0
        for i in self.incoming:
            points = sum([c.heuristic for c in self.queues[i]])
            if points > max:
                max = points
                street_inc = i

        if max == 0:
            return 0
        else:
            return street_inc

class Street:
    def __init__(self, s_i, e_i, s_n, t_t):
        self.start_intersection = s_i
        self.end_intersection = e_i
        self.street_name = s_n
        self.travel_time = t_t

class Car:
    def __init__(self, id, n_s, s, step, next_intersection):
        self.actual_street = s[0]
        self.number_streets = n_s - 1
        self.id = id
        self.streets = s[1:]
        self.heuristic = 0
        self.step = step
        self.last_step = step
        self.next_intersection = next_intersection

    def add_step(self):
        self.step += 1

    def change_street(self):
        return

    def traffic_light(self):
        return True if self.step == self.last_step else False

class Solution:
    def __init__(self):
        self.intersections = 0
        self.intersections_traffic_light_green = {}

    def add_on_time_trafficlight(self, id, street, time):
        if not id in self.intersections_traffic_light_green:
            self.intersections += 1
            self.intersections_traffic_light_green[id] = []

        self.intersections_traffic_light_green[id].append((street, time))

class Problem:
    def __init__(self, file_content):
        content = file_content.split("\n")

        first_line = content[0].split(" ")
        self.duration = int(first_line[0])
        self.number_intersections = int(first_line[1])
        self.number_streets = int(first_line[2])
        self.number_of_cars = int(first_line[3])
        self.bonus = int(first_line[4])

        self.streets = {}
        self.cars = {}
        self.intersections = {}


        self.solution = Solution()

        for i in range(self.number_intersections):
            self.intersections[i] = Intersection(i)

        for i in range(1, self.number_streets + 1):
            line = content[i].split(" ")
            start_intersection = int(line[0])
            end_intersection = int(line[1])
            street_name = line[2]
            travel_time = int(line[3])
            self.streets[street_name] = Street(start_intersection, end_intersection, street_name, travel_time)

            self.intersections[self.streets[street_name].start_intersection].outbound.append(street_name)
            self.intersections[self.streets[street_name].end_intersection].incoming.append(street_name)
            self.intersections[self.streets[street_name].end_intersection].queues[street_name] = []

        counter = 0
        for i in range(1 + self.number_streets, 1 + self.number_streets + self.number_of_cars):
            line = content[i].split(" ")
            number_streets = int(line[0])
            streets = content[i][1 + len(str(number_streets)):].split(" ")
            next_intersection = self.streets[streets[0]].end_intersection
            self.cars[counter] = Car(counter, number_streets, streets, self.streets[streets[0]].travel_time, next_intersection)
            self.intersections[self.streets[streets[0]].end_intersection].add_car(self.cars[counter])
            counter += 1

        return

    def one_step(self):
        return

    def solve(self):
        for t in self.intersections:
            for street in self.intersections[t].incoming:
                n = random.randint(0, 20)
                if n != 0:
                    self.solution.add_on_time_trafficlight(id = self.intersections[t].id, street = street, time = n)

        #for sol in self.solution.intersections_traffic_light_green:
        #    print(f'{sol} : {self.solution.intersections_traffic_light_green[sol]}')


    def write_solution(self, eccolo):
        S = ''
        S += f"{self.solution.intersections}\n"
        for sol in self.solution.intersections_traffic_light_green:
            S += f"{sol}\n"
            S += f"{len(self.solution.intersections_traffic_light_green[sol])}\n"
            for street in self.solution.intersections_traffic_light_green[sol]:
                S +=f"{street[0]} {street[1]}\n"

        soluzza = open(f'sol{eccolo}.txt',"w")
        soluzza.write(S)

    def to_output(self):
        problem_name = "a"
        shutil.make_archive(f"{problem_name}_{time.time()}", 'zip')
        return


def parse_input(file_name):
    with open(f"{DIRPATH}/data/{file_name}.txt", 'r') as f:
        return Problem(f.read())


if __name__ == '__main__':
    problem = parse_input(sys.argv[1])
    problem.solve()
    problem.write_solution(sys.argv[1])

    # problem.to_output()

