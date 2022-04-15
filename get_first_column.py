def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    data = data.split('\n')
    res = []
    for i in data[1:]:
        res.append(i.split('\n')[0])
    return res

# Read the csv file
