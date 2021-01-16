""" Collection of helper functions related to plot module"""

import pathlib
import plotly
import plotly.figure_factory as ff
import pandas as pd


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


def is_running_from_ipython():
    """ Check if code is run inside Jupyter Notebook """
    from IPython import get_ipython
    return get_ipython() is not None


def create_output_dir(relative_folder_path):
    """ Helper function to create output directory (if it doesn't exist yet) """
    if is_running_from_ipython():
        output_dir = pathlib.Path.cwd().parent.parent.parent / relative_folder_path
    else:
        output_dir = pathlib.Path.cwd() / relative_folder_path
    output_dir.mkdir(parents=True, exist_ok=True)

    return output_dir


def remove_files_in_dir(relative_folder_path):
    """ Helper to remove all files from folder (recursively) """
    if is_running_from_ipython():
        input_dir = pathlib.Path.cwd().parent.parent.parent / relative_folder_path
    else:
        input_dir = pathlib.Path.cwd() / relative_folder_path
    assert input_dir.is_dir()  # make sure it`s a folder
    for p in reversed(list(input_dir.glob('**/*'))):  # iterate contents from leaves to root
        if p.is_file():
            p.unlink()


def remove_prefix_from_file_name(prefix, relative_folder_path, file_types=['.png']):
    """ Plot icons are created by external program which adds prefixes to file names. Remove prefix from file name """
    input_dir = pathlib.Path.cwd() / relative_folder_path
    assert input_dir.is_dir()  # make sure it`s a folder
    for p in input_dir.iterdir():
        try:
            if p.is_file() and p.suffix in file_types:
                parent_dir = p.parent
                file_extension = p.suffix
                old_file_name = p.stem
                new_file_name = old_file_name.replace(prefix, "") + file_extension
                p.rename(pathlib.Path(parent_dir, new_file_name))
            else:
                print(f"Path {p} doesn't lead to a file or file type {p.suffix} is not in list of allowed file types {file_types}")
        except Exception as e:
            print("Exception occured")
            print(e)


def save_plot_as_div(figure, plot_name):
    """ Write div containing plot to file """
    # if is_running_from_ipython():
    #     input_dir = pathlib.Path.cwd().parent.parent.parent / relative_folder_path
    # else:
    #     input_dir = pathlib.Path.cwd() / relative_folder_path
    output_dir = pathlib.Path.cwd().parent.parent.parent / "dataviz_gallery/templates/plotly"
    file_path = output_dir / f"{plot_name}.html"
    div = plotly.offline.plot(figure_or_data=figure, include_plotlyjs=False, output_type='div')
    with open(file_path, "w") as f:
        f.write(div)


def create_table(data_frame, cols, order_cols, sample_size=12):
    """ Create plotly table which can be embedded on website """
    data_frame = data_frame[cols]
    df_sample = data_frame.sample(n=sample_size, random_state=42)
    if order_cols is not None:
        df_sample = df_sample.sort_values(by=order_cols)
    colorscale = [[0, "#292b2c"],[0.5, '#f7f7f7'],[1, '#ffffff']]
    fig = ff.create_table(df_sample, colorscale=colorscale)
    fig.show()
    return fig