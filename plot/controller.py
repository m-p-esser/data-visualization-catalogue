""" Controller to run all the plotting functions """

import json
import seaborn as sns
import matplotlib.pyplot as plt
from plot import plotting, utils

plot_func_mapping = {
    # "Area Chart": "plt.stackplot",
    "Bar Plot": "sns.countplot",
    "Box Plot": "sns.boxplot",
    "Density Plot": "sns.kdeplot",
    # "Donut Chart": "",
    # "Gauge Chart": "",
    "Histogram": "sns.histplot",
    "Line Chart": "sns.lineplot",
    # "Pie Chart": "",
    "Scatter Plot": "sns.scatterplot",
    # "Steam Graph": "",
    "Violin Plot": "sns.violinplot",
}

vars_selection = {
    "cat_vars": ["body-style", "make", "drive-wheels", "fuel-type"],
    "num_vars": ["length", "width", "height"],
    "time_vars": [],
}

# Load data into memory
example_df = plotting.load_data("4_automobile.csv", "example_datasets", sep=",")
example_df = plotting.filter_data(example_df, vars_selection)
plot_taxanomy = plotting.load_data("plot_taxanomy.csv", "plot_taxanomy")

# Iterate over different plots and save them as png
for idx, row in plot_taxanomy[0:10].iterrows():
    # try:
    print(f"Iteration number: {idx+1}")

    # Load data from plot taxanomy
    visual_cue_params = row["visual_cue_params"]
    variation_name = row["variation_name"]
    plot_name = (
        variation_name.replace("Simple ", "")
        .replace("Grouped ", "")
        .replace("Single Facetted ", "")
        .replace("Dual Facetted ", "")
    )  # to-do: fix this line
    plot_package = row["plot_package"]
    facetted = row["facetted"]
    grouped = row["grouped"]

    visual_cue_params = json.loads(visual_cue_params)
    vars_picked = plotting.pick_vars(
        visual_cue_params=visual_cue_params, vars_selection=vars_selection
    )
    output_dir = utils.create_output_dir("output")
    file_path = output_dir / variation_name

    # Create plot commands
    plot_commands = plotting.construct_plot_command(
        data=example_df,
        plot_name=plot_name,
        variation_name=variation_name,
        plot_func_mapping=plot_func_mapping,
        plot_package=plot_package,
        vars_picked=vars_picked,
        file_path=file_path,
        facetted=facetted,
        grouped=grouped,
    )

    df = example_df.copy()  # df as param referenced in plot commands
    for command in plot_commands:
        try:
            exec(command)
        except Exception as e:
            print("Exception occured")
            print(e)
        finally:
            print(command)
    print()

    # except Exception as e:
    #     print(f"An exception occured | {e}")
