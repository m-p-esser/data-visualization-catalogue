""" Functions to create plots as png files """

import pathlib
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from plot import utils


def load_data(file_name, sep=";"):
    """ Load data from file to dataframe """
    if pathlib.Path.cwd().parts[-1] == "jupyter_notebooks":
        file_path = [fp for fp in pathlib.Path.cwd().parent.rglob(f'*{file_name}')][0]
    else:
        file_path = [fp for fp in pathlib.Path.cwd().rglob(f'*{file_name}')][0]
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


def pick_vars(visual_cue_params, vars_selection, cues, plot_name):
    """ Pick necessary variables which are required to create the plot """

    vars_picked = {}

    cat_vars = vars_selection["cat_vars"]
    num_vars = vars_selection["num_vars"]
    time_vars = vars_selection["time_vars"]

    cat_pos_counter = 0
    num_pos_counter = 0
    time_pos_counter = 0

    for cue in cues:

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


def seaborn_settings(style="darkgrid", context="talk", font_scale=0.65):
    """ Activate global seaborn settings """
    sns.set_theme(style=style)
    sns.set_context(context=context, font_scale=font_scale)


def map_cols_for_visual_cues(cues, vars_picked):
    """ Takes a list of visual cues (e.g. x, y, hue) and map each cue to a
    specific column (from the dataframe used to plot the data) """

    visual_cue_col_mapping = {}

    for cue in cues:
        value = vars_picked.get(cue)
        if value is not None:
            value = f'"{value}"'
        visual_cue_col_mapping[cue] = value

    return visual_cue_col_mapping


def calc_unique_values(df, vars_picked):
    """ Calculate unique values for each column and store in dictionary with visual cue as key"""

    unique_values = {}

    for k, v in vars_picked.items():
        nunique = df[v].nunique()
        unique_values[k] = nunique

    return unique_values


def dict_to_args_string(add_args):
    """ Flatten dictionary to string, so it can be accepted as optional argument for plot """

    args_string = ", "

    for k, v in add_args.items():
        args_string = args_string + str(k) + "=" + str(v) + ", "
    args_string = args_string[:-2]

    return args_string


def construct_plot_command(
    data,
    plot_name,
    variation_name,
    basic_plot_func,
    plot_package,
    file_path,
    unique_values,
    plots_per_row=3,
    fig_size=(10, 10),
    x=None,
    y=None,
    hue=None,
    size=None,
    row=None,
    col=None,
    facetted=False,
    single_facetted=False,
    dual_facetted=False,
    grouped=False,
    add_plot_args={},
    add_gmap_args={}
):
    """ Create executable plot command which allows to create a plot as png file"""

    plot_args_string = ""
    if len(add_plot_args) > 0:
        plot_args_string = dict_to_args_string(add_plot_args)

    gmap_args_string = ""
    if len(add_gmap_args) > 0:
        gmap_args_string = dict_to_args_string(add_plot_args)

    if x is None and y is None:
        raise ValueError("Either x or y need to have a value")

    if plot_package not in ["Seaborn", "Matplotlib"]:
        raise ValueError(f"Plot package '{plot_package}' not compatible")

    plot_commands = []

    # Facets
    if facetted is True:
        if plot_package == "Seaborn":
            if single_facetted is True:
                c1 = f"g = sns.FacetGrid(data=df, row={row}, col={col}, col_wrap={plots_per_row}, height=4, aspect=1)"
            else:
                c1 = (
                    f"g = sns.FacetGrid(data=df, row={row}, col={col}, margin_titles=True, height=4, aspect=1)"
                )
            c2 = f"g.map_dataframe({basic_plot_func}, x={x}, y={y}, hue={hue}{gmap_args_string})"
            c3 = f"g.set_axis_labels({x}, {y})"
            c4 = "g.add_legend()"
            plot_commands.extend([c1, c2, c3, c4])

        else:
            c1 = "{}(x=df[{}], y=df[{}])".format(
                basic_plot_func, utils.replace_str(x), utils.replace_str(y)
            )
            plot_commands.extend([c1])

    # Non Facets
    if facetted is False:
        if plot_package == "Seaborn":
            c1 = (
                f"{basic_plot_func}(data=df, x={x}, y={y}, hue={hue}{plot_args_string})"
            )
            plot_commands.extend([c1])

        else:
            c1 = "{}(x=df[{}], y=df[{}])".format(
                basic_plot_func, utils.replace_str(x), utils.replace_str(y)
            )
            plot_commands.extend([c1])

    plot_commands.append("plt.tight_layout()")
    plot_commands.append(f'plt.savefig(r"{file_path}.png", dpi=300)')
    plot_commands.append("plt.close('all')")

    return plot_commands


def plot_commands_to_markdown():
    """ Plot Commands need to be transformed to a format which can be implemented in Website, e.g. Markdown """
    pass

