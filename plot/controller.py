""" Controller to run all the plotting functions """

import pathlib
import pandas as pd
from plot import plot_utils
import os

# Load taxanomy
file_path = pathlib.Path.cwd() / "data" / "plot_taxanomy" / "plot_taxanomy.xlsx"
df = pd.read_excel(file_path)

# Create output dir
script_dir = pathlib.Path.cwd() / "plot" / "scripts"
output_dir = plot_utils.create_output_dir("dataviz_gallery/static/img/seaborn")
global output_dir

# Clean folder
plot_utils.remove_files_in_dir("dataviz_gallery/static/img/seaborn")

scripts_not_found = []

# Create plots based on .py scripts
for index, row in df["variation_name"].items():
    script_name = row.lower().replace(" ", "_") + ".py"
    script_path = script_dir / script_name
    try:
        exec(open(script_path).read())
        print(f"Executing '{script_name}'")
    except FileNotFoundError:
        print(f"file '{script_path}' couldn't be found")
        scripts_not_found.append(script_name)
    except Exception as e:
        print(f"An exception occured when running '{script_name}'")
        print(e)

print(f"{len(scripts_not_found)} scripts couldn't be found")