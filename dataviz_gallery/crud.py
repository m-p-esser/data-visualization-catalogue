import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()

import pathlib
import pandas as pd
from dataviz_gallery import models


def csv_to_df(file_name: str):
    data_dir = pathlib.Path.cwd() / 'data'
    file_path = data_dir / file_name
    df = pd.read_csv(file_path, delimiter=';')
    return df


def df_to_query_list(df: pd.DataFrame):
    query_list = df.to_dict('records')
    return query_list


def bulk_create(query_list):
    instances = [
        models.Plot(
            name=entry['Name'],
            image='img/' + str(entry['Name']).lower().replace(' ', '_') +
            ".png",
        ) for entry in query_list
    ]
    models.Plot.objects.bulk_create(instances, ignore_conflicts=True)


if __name__ == "__main__":
    df = csv_to_df('plot_taxanomy.csv')
    query_list = df_to_query_list(df)
    bulk_create(query_list)
