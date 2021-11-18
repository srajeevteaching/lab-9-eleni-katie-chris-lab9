#Chris, Eleni, Kaite
#CS151
#11/18/21
#Lab9

DATE = 0
TITLE = 1
BUDGET = 2
GROSS = 3

def load_movie_data(filename):
    data= []
    try:
        f = open(filename, "r")
        line_count = 0
        for line in f:
            try:
                line_count += 1

                line_entries = line.split(",")

                line_entries[DATE] = int(line_entries[DATE])
                line_entries[TITLE] = line_entries[TITLE].strip()
                line_entries[BUDGET] = float(line_entries[BUDGET])
                line_entries[GROSS] = float(line_entries[GROSS])

                data.append(line_entries)

            except ValueError:
                print("Error: skipping line", line_count, "because of invalid value.")

        f.close()

    except FileNotFoundError:
        print("Error: File", filename, "not found.")

    return data


def add_profit_column(data,line_entries):
    for i in range(len(data)):
        data.append(line_entries[GROSS] - line_entries[BUDGET])
    return data

