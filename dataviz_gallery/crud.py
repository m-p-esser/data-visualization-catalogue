import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django

django.setup()

import pathlib
import json
import pandas as pd
import numpy as np
from dataviz_gallery import models


def csv_to_df(relative_path: str):
    file_path = pathlib.Path.cwd() / relative_path
    df = pd.read_csv(file_path, delimiter=";")

    return df


def xlsx_to_df(relative_path: str):
    file_path = pathlib.Path.cwd() / relative_path
    df = pd.read_excel(file_path)

    return df


def str_entry_to_json_entry(relative_path_in: str, relative_path_out: str, cols: list):
    """ Convert string entry in pandas series in json entry and output to new flat file"""
    df = xlsx_to_df(relative_path=relative_path_in)

    # Iterate over different columns
    for col in cols:

        # Unique values for each column
        series = df[col]
        unique_strings = series.unique().tolist()
        unique_split = [
            string.split(",") for string in unique_strings if isinstance(string, str)
        ]
        unique_flatten = [
            list_elem.strip() for sublist in unique_split for list_elem in sublist
        ]
        unique = np.unique(unique_flatten).tolist()

        for index, entry in series.items():

            # Populate dict
            dict_entry = {}

            if isinstance(entry, str):
                list_entry = entry.split(",")
                list_entry = [elem.strip() for elem in list_entry]
                for list_elem in unique:
                    key = list_elem.strip()  #.replace("'", '"')
                    if list_elem in list_entry:
                        dict_entry[key] = True
                    else:
                        dict_entry[key] = False
                dict_entry = json.dumps(dict_entry)

            else:
                print(f"Entry {entry} is no string and can't be processed")

            df.loc[:, col].at[index] = dict_entry

    file_path_out = pathlib.Path.cwd() / relative_path_out
    df.to_excel(file_path_out)


def df_to_query_list(df: pd.DataFrame):
    query_list = df.to_dict("records")

    return query_list


def bulk_create(query_list):
    instances = [
        models.Plot(
            parent_name=entry["parent_name"],
            variation_name=entry["variation_name"],
            synonyms=entry["synonyms"],
            goals=json.loads(entry["goals"]),
            dimensionality=entry["dimensionality"],
            numerical=entry["numerical"],
            categorical=entry["categorical"],
            visual_cues=json.loads(entry["visual_cues"]),
            coordinate_system=json.loads(entry["coordinate_system"]),
            shapes=json.loads(entry["shapes"]),
            description=entry["description"],
            anatomy=entry["anatomy"],
            caveats=entry["caveats"],
            facetted=entry["facetted"],
            single_facetted=entry["single_facetted"],
            dual_facetted=entry["dual_facetted"],
            grouped=entry["grouped"],
            plot_package=entry["plot_package"],
            related=json.loads(entry["related"]),
            implemented=entry["implemented"],
            icon="img/icon/"
            + str(entry["parent_name"]).lower().replace(" ", "_")
            + ".png",
            seaborn="img/seaborn/"
            + str(entry["variation_name"]).lower().replace(" ", "_")
            + ".png",
            code=entry["variation_name"].lower().replace(" ", "_") + ".md",
        )
        for entry in query_list
    ]
    models.Plot.objects.bulk_create(instances, ignore_conflicts=True)

    print("Added entries to database table")


if __name__ == "__main__":
    str_entry_to_json_entry(
        relative_path_in="data/plot_taxanomy/plot_taxanomy.xlsx",
        relative_path_out="data/plot_taxanomy/plot_taxanomy_out.xlsx",
        cols=["goals", "visual_cues", "coordinate_system", "shapes", "related"],
    )
