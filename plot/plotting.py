""" Functions to create plots as png files """

import pathlib
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from plot import utils


def load_data(file_name, folder_name, sep=";"):
    """ Load data from file to dataframe """
    root_dir = pathlib.Path.cwd()
    data_dir = root_dir / "data" / folder_name
    file_path = data_dir / file_name
    df = pd.read_csv(file_path, sep=sep)

    return df


def filter_data(df, vars_selection):
    """ Filter down to only relevant columns """
    cat_vars = vars_selection["cat_vars"]
    num_vars = vars_selection["num_vars"]
    time_vars = vars_selection["time_vars"]
    rel_vars = cat_vars + num_vars + time_vars
    filtered_df = df[rel_vars]

    return filtered_df


def pick_vars(visual_cue_params, vars_selection):
    """ Pick necessary variables from list of availabe ones """

    vars_picked = {}

    cat_vars = vars_selection["cat_vars"]
    num_vars = vars_selection["num_vars"]
    time_vars = vars_selection["time_vars"]

    cat_pos_counter = 0
    num_pos_counter = 0
    time_pos_counter = 0

    for cue in ["x", "y", "hue", "size", "col", "row"]:

        var_type = visual_cue_params.get(cue)

        if var_type == "cat":
            var = cat_vars[cat_pos_counter]
            vars_picked[cue] = var
            cat_pos_counter += 1

        elif var_type == "num":
            var = num_vars[num_pos_counter]
            vars_picked[cue] = var
            num_pos_counter += 1

        if var_type == "time":
            var = time_vars[time_pos_counter]
            vars_picked[cue] = var
            time_pos_counter += 1

    return vars_picked


def seaborn_settings():
    sns.set_theme(style="whitegrid")


def construct_plot_command(
    data,
    plot_name,
    variation_name,
    plot_func_mapping,
    plot_package,
    vars_picked,
    file_path,
    facetted=False,
    grouped=False,
):
    """ Create executable plot command which allows to create a plot as png file"""

    basic_plot_func = plot_func_mapping.get(plot_name)
    print(basic_plot_func)

    visual_cue_cols = {}

    for cue in ["x", "y", "hue", "size", "row", "col"]:
        value = vars_picked.get(cue)
        if value is not None:
            value = f'"{value}"'
        visual_cue_cols[cue] = value

    x = visual_cue_cols["x"]
    y = visual_cue_cols["y"]
    hue = visual_cue_cols["hue"]
    # size = visual_cue_cols["size"]
    row = visual_cue_cols["row"]
    col = visual_cue_cols["col"]

    if x is None or y is None:
        raise ValueError("Either x or y need to have a value")

    if plot_package not in ["Seaborn", "Matplotlib"]:
        raise ValueError(f"Plot package '{plot_package}' not compatible")

    plot_commands = []

    if facetted is True:
        if plot_package == "Seaborn":
            command_1 = f"g = sns.FacetGrid(data=df, row={row}, col={col}, hue={hue})"
            concated_string = utils.concat_strings(basic_plot_func, x, y)
            command_2 = f"g.map({concated_string})"
            command_3 = f'g.savefig(r"{file_path}.png")'
            plot_commands.extend([command_1, command_2, command_3])

        else:
            command_1 = "{}(x=df[{}], y=df[{}])".format(
                basic_plot_func, utils.replace_str(x), utils.replace_str(y)
            )
            command_2 = f'plt.savefig(r"{file_path}.png")'
            plot_commands.extend([command_1, command_2])

    if facetted is False:
        if plot_package == "Seaborn":
            command_1 = f"{basic_plot_func}(data=df, x={x}, y={y}, hue={hue})"
            command_2 = f'plt.savefig(r"{file_path}.png")'
            plot_commands.extend([command_1, command_2])
        else:
            command_1 = "{}(x=df[{}], y=df[{}])".format(
                basic_plot_func, utils.replace_str(x), utils.replace_str(y)
            )
            plot_commands.extend([command_1])

    return plot_commands

