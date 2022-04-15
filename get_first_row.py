def get_first_row(data):
    """
    Get the first row from a CSV file.
     Args:
         data(str): csv file.
     Return:
         list: First row.
    """

    return data.split("\n")[1].split(',')

# Read the csv file
