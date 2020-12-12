""" Collection of helper functions """

import pathlib


def create_output_dir(relative_folder_path):
    """ Helper function to create output directory """
    output_dir = pathlib.Path.cwd() / relative_folder_path
    output_dir.mkdir(parents=True, exist_ok=True)

    return output_dir


def remove_files_in_dir(relative_folder_path):
    """ Helper to remove all files from folder (recursively) """
    input_dir = pathlib.Path.cwd() / relative_folder_path
    assert input_dir.is_dir()  # make sure it`s a folder
    for p in reversed(list(input_dir.glob('**/*'))):  # iterate contents from leaves to root
        if p.is_file():
            p.unlink()


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
    """ Helper function to add quotation around strings which are not of type None """
    if string is None:
        return string
    else:
        string = string.replace("'", "")
        return string
