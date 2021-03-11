import sys

from solver import Solver
from solverscikit import SolverDBScan

if __name__ == '__main__':
    file_names = sys.argv[1].split("-")
    for file_name in file_names:
        print(f"Solving file {file_name}...")
        problem = SolverDBScan(file_name)
        problem.solve()
        problem.to_output()
