#!/usr/bin/python3
def read_file(filename=""):
    """ Function that reads from a file

    Args:
        filename: func_filename

    Raises
        Exception: when the file can be opened

    """

    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
