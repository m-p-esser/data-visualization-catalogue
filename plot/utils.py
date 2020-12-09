""" Collection of helper functions """

import pathlib


def create_output_dir(folder_name):
    """ Helper function to create output directory """
    output_dir = pathlib.Path.cwd() / "plot" / folder_name
    output_dir.mkdir(parents=True, exist_ok=True)

    return output_dir


def concat_strings(*strings):
    """ Helper function to concat strings which are not of type None"""
    concated_string = ""
    for s in strings:
        if s is not None:
            concated_string = concated_string + s + ", "
    # remove last two letters, because the comma is getting added after the last concatination
    concated_string = concated_string[:-2]
    return concated_string


def replace_str(string):
    """ Helper function to add quotation around strings which are not None """
    if string is None:
        return string
    else:
        string = string.replace("'", "")
        return string
