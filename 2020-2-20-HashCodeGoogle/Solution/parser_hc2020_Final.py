import os
import numpy as np
from numba import jit
import tqdm
import sys

DIRPATH = os.path.dirname(os.path.realpath(__file__))


class Problem:
    def __init__(self, libraries, days, number_books, books_to_library):
        self.libraries = libraries
        self.days = days
        self.books_to_library = books_to_library

        self.selected_libraries = []

    def add_library(self, id):
        self.selected_libraries.append(SelectedLibrary(id))

    def get_output_file(self):
        output = ""
        output += "{}\n".format(len(self.selected_libraries))
        for selected_library in self.selected_libraries:
            output += "{} {}\n".format(
                selected_library.id, len(selected_library.selected_books)
            )
            for id in selected_library.selected_books:
                output += "{} ".format(id)
            output += "\n"

        with open("outF.txt", "w") as f:
            f.write("{}".format(output))


class SelectedLibrary:
    def __init__(self, id, books):
        self.id = id
        self.selected_books = books


class Book:
    def __init__(self, id, value):
        self.value = value
        self.id = id


class Library:
    def __init__(self, id, books, signup_days, books_per_day):
        self.id = id
        self.books = books
        self.signup_days = signup_days
        self.books_per_day = books_per_day
        self.books_id = set()
        for book in books:
            self.books_id.add(book.id)

        self.sorted_books = sorted(self.books, key=lambda b: b.value, reverse=True)


def parse_input(file):
    books_value = {}
    libraries = []
    books_to_library = {}
    id_library = 0

    with open(file, "r") as f:
        for i, line in enumerate(f):
            if i == 0:
                values = line.split(" ")
                number_books = int(values[0])
                number_libraries = values[1]
                number_days = int(values[2])
            elif i == 1:
                values = line.split(" ")
                book_id = 0
                for v in values:
                    books_value[book_id] = int(v)
                    books_to_library[book_id] = set()
                    book_id += 1

            else:
                if line == "\n":
                    print("bois", i)

                elif i % 2 == 0:
                    values = line.split(" ")
                    number_books_library = values[0]
                    sign_up_library = int(values[1])
                    books_per_day = int(values[2])
                else:
                    values = line.split(" ")
                    books_in_library = []
                    for v in values:
                        books_in_library.append(Book(int(v), books_value[int(v)]))
                        books_to_library[int(v)].add(id_library)

                    libraries.append(
                        Library(
                            id_library, books_in_library, sign_up_library, books_per_day
                        )
                    )
                    id_library += 1

    return Problem(libraries, number_days, number_books, books_to_library)


if __name__ == "__main__":
    data = parse_input(sys.argv[1])
    data.libraries.sort(
        key=lambda l: sum(list(map(lambda b: b.value, l.books))) / l.signup_days,
        reverse=True,
    )
    selected_books_set = set()
    i = 0

    while i < data.days and len(data.libraries) != 0:
        data.libraries.sort(
            key=lambda l: sum(
                list(
                    map(
                        lambda b: b.value,
                        l.books[0 : (data.days - i) * l.books_per_day],
                    )
                )
            ),
            reverse=True,
        )

        library = data.libraries.pop(0)
        books_to_add = library.books[0 : (data.days - i) * library.books_per_day]
        books_to_add = list(map(lambda b: b.id, books_to_add))

        for id in books_to_add:
            selected_books_set.add(id)

        for t in range(len(data.libraries)):
            data.libraries[t].books = list(
                filter(
                    lambda b: b.id not in selected_books_set, data.libraries[t].books
                )
            )
            data.libraries[t].books = sorted(
                data.libraries[t].books, key=lambda b: b.value, reverse=True
            )
        data.selected_libraries.append(SelectedLibrary(library.id, books_to_add))
        i += library.signup_days

    data.get_output_file()
