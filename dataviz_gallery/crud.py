import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()

import pathlib
import pandas as pd
from dataviz_gallery import models


def csv_to_df(relative_path: str):
    file_path = pathlib.Path.cwd() / relative_path
    df = pd.read_csv(file_path, delimiter=';')

    return df


def df_to_query_list(df: pd.DataFrame):
    query_list = df.to_dict('records')

    return query_list


def bulk_create(query_list):
    instances = [
        models.Plot(
            parent_name=entry['parent_name'],
            variation_name=entry['variation_name'],
            synonyms=entry['synonyms'],
            goals=entry['goals'],
            dimensionality=entry['dimensionality'],
            numerical=entry['numerical'],
            categorical=entry['categorical'],
            visual_cues=entry['visual_cues'],
            coordinate_system=entry['coordinate_system'],
            shapes=entry['shapes'],
            anatomy=entry['anatomy'],
            caveats=entry['caveats'],
            facetted=entry['facetted'],
            single_facetted=entry['single_facetted'],
            dual_facetted=entry['dual_facetted'],
            grouped=entry['grouped'],
            plot_package=entry['plot_package'],
            related=entry['related'],
            implemented=entry['implemented'],
            icon='img/icon/' + str(entry['parent_name']).lower().replace(' ', '_') +
            ".png",
            seaborn='img/seaborn/' + str(entry['variation_name']).lower().replace(' ', '_') +
            ".png",
        ) for entry in query_list
    ]
    models.Plot.objects.bulk_create(instances, ignore_conflicts=True)

    print("Added entries to database table")