import pathlib
import argparse
import sys
from dataviz_gallery import crud

parser = argparse.ArgumentParser(
    prog='bulk_create',
    description='Load data from flat file into database table')

parser.add_argument(
    '-rp',
    '--relative_path',  # this get's added as Namespace (without --)
    metavar='Relative Path',
    type=str,
    required=True,
    help='the path to the flat file which should be used to populate the database table',
    action='store',  # stores value to Namespace object
    nargs=1  # expects n (here 1) value for the argument
)

# Execute the parse_args() method
args = parser.parse_args()

if isinstance(args.relative_path, list):
    relative_path = args.relative_path[0]
else:
    relative_path = args.relative_path

df = crud.xlsx_to_df(relative_path)
query_list = crud.df_to_query_list(df)
crud.bulk_create(query_list)
