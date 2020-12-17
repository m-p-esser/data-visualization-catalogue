""" Controller to run all the plotting functions """

import json
import seaborn as sns
import matplotlib.pyplot as plt
import utils
from plot import plot, plot_utils

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
    "cat_vars": ["race", "gender", "relationship", "income"],
    "num_vars": ["age", "hours-per-week", "capital-gain", "capital-loss"],
    "time_vars": [],
}

cues = ["x", "y", "hue", "size", "row", "col"]

# Settings
plot.seaborn_settings()

# Load data into memory
example_df = plot.load_data("6_adult.csv", sep=",")
example_df = plot.filter_data(example_df, vars_selection)
plot_taxanomy = plot.load_data("plot_taxanomy.csv")

# Create output dir
output_dir = utils.create_output_dir("dataviz_gallery/static/img/seaborn")

# Clean up folder
utils.remove_files_in_dir("dataviz_gallery/static/img/seaborn")

# Iterate over different plots and save them as png
for idx, row in plot_taxanomy.iterrows():
    try:
        print(f"Iteration number: {idx+1}")

        # Load data from plot taxanomy
        visual_cue_params = json.loads(row["visual_cue_params"])
        plot_name = row["parent_name"]
        variation_name = row["variation_name"]
        plot_package = row["plot_package"]
        facetted = row["facetted"]
        single_facetted = row["single_facetted"]
        dual_facetted = row["dual_facetted"]
        grouped = row["grouped"]
        add_plot_args = json.loads(row["add_plot_args"])
        print(add_plot_args)
        add_gmap_args = json.loads(row["add_gmap_args"])
        print(add_gmap_args)

        # Dictionary manipulation
        vars_picked = plot.pick_vars(visual_cue_params, vars_selection, cues, plot_name)
        print(vars_picked)
        visual_cue_col_mapping = plot.map_cols_for_visual_cues(cues, vars_picked)
        unique_values = plot.calc_unique_values(example_df, vars_picked)
        basic_plot_func = plot_func_mapping.get(plot_name)

        # Filepath management
        file_name = str(idx + 1) + "_" + variation_name
        file_path = output_dir / file_name

        # Create plot commands
        plot_commands = plot.construct_plot_command(
            data=example_df,
            plot_name=plot_name,
            variation_name=variation_name,
            basic_plot_func=basic_plot_func,
            plot_package=plot_package,
            file_path=file_path,
            unique_values=unique_values,
            plots_per_row=3,
            x=visual_cue_col_mapping["x"],
            y=visual_cue_col_mapping["y"],
            hue=visual_cue_col_mapping["hue"],
            size=visual_cue_col_mapping["size"],
            row=visual_cue_col_mapping["row"],
            col=visual_cue_col_mapping["col"],
            facetted=facetted,
            single_facetted=single_facetted,
            dual_facetted=dual_facetted,
            grouped=grouped,
            add_plot_args=add_plot_args,
            add_gmap_args=add_gmap_args
        )

        print(plot_commands)

        df = example_df.copy()  # df as param referenced in plot commands
        for command in plot_commands:
            try:
                exec(command)
            except Exception as e:
                print("Exception occured")
                print(e)

    except Exception as e:
        print(f"An exception occured | {e}")

    finally:
        print()
