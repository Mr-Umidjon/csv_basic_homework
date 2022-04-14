import csv


def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    f = open(data)
    data = list(csv.reader(f))

    return len(data[0])


# # Read the csv file
# f = open('data.csv')
# data = csv.reader(f)
# print(find_number_of_columns(list(data)))

print(find_number_of_columns('data.csv'))
