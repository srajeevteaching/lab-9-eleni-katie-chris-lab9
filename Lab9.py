# Programmers: Chris, Eleni, Katie
# Course: CS151, Dr. Rajeev
# Date: 11/18/21
# Lab Number: 9
# Program Inputs: [What information do you request from the user?]
# Program Outputs: [What information do you display for the user?]

import sys

DATE = 0
TITLE = 1
BUDGET = 2
GROSS = 3
PROFIT = 4

# A function load_movie_data which, given the name of a file respecting the csv format outlined above,
# loads the data into a list of lists. Declare column index constants at the top of your program for
# each of the movie fields (release date, title, etc.) Cast each field to the appropriate type.
# Use try/except so that your program exits normally if the file does not exist or if a numerical value
# in the input file fails to cast.
def load_movie_data(filename):
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print("Exception: File", filename, "not found.")
        return []

    data = []
    line_count = 0
    for line in f:
        line_count += 1
        line_entries = line.split(",")

        try:
            line_entries[DATE] = line_entries[DATE].strip()
            line_entries[TITLE] = line_entries[TITLE].strip()
            line_entries[BUDGET] = float(line_entries[BUDGET])
            line_entries[GROSS] = float(line_entries[GROSS])
            data.append(line_entries)
        except ValueError:
            print("Error: skipping line", line_count, "because of invalid value.")

    f.close()
    return data

# A function add_profit_column which, given a movie dataset as a list of lists, appends a profit
# column to the data computed as the difference between each movie's gross and its budget.
def add_profit_column(data):
    for row in data:
        row.append(row[GROSS] - row[BUDGET])

# A function print_min_and_max_profit which, given a movie dataset as a list of lists, searches the dataset and
# prints all available info on the movies with the highest and lowest profits.
def print_min_and_max_profit(data):
    lowest_profit = sys.maxsize
    highest_profit = 0

    lowest_row = []
    highest_row = []

    for row in data:
        if row[PROFIT] > highest_profit:
            highest_row = row
        if row[PROFIT] < lowest_profit:
            lowest_row = row

    print("lowest profit: ", lowest_row)
    print("highest profit: ", highest_row)

# A function save_movie_data which, given a movie dataset as a list of lists and a filename,
# saves the dataset to a comma-separated values file of the given name.
def save_movie_data(data, filename):
    try:
        f = open(filename, "w")
    except IOError:
        print("Exception: File", filename, "could not be opened for writing.")
        return

    for row in data:
        f.write(str(row[DATE]) + ",")
        f.write(str(row[TITLE]) + ",")
        f.write("{:.2f}".format(row[BUDGET]) + ",")
        f.write("{:.2f}".format(row[GROSS]) + ",")
        f.write("{:.2f}".format(row[PROFIT]) + "\n")

    f.close()
    return

def main():
    data = load_movie_data("movies.csv")
    add_profit_column(data)
    print_min_and_max_profit(data)
    save_movie_data(data, "movies_out.csv")

main()