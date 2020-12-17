import pathlib
import argparse
import sys
from dataviz_gallery import crud

parser = argparse.ArgumentParser(
    prog='bulk_create',
    description='Load data from csv into database table')

parser.add_argument(
    '-p',
    '--path',  # this get's added as Namespace (without --)
    metavar='Relative Path',
    type=str,
    required=True,
    help='the path to the csv which should be used to populate the database table',
    action='store',  # stores value to Namespace object
    nargs=1  # expects n (here 1) value for the argument
)

# Execute the parse_args() method
args = parser.parse_args()

if isinstance(args.path, list):
    path = args.path[0]
else:
    path = args.path

df = crud.csv_to_df(path)
query_list = crud.df_to_query_list(df)
crud.bulk_create(query_list)
