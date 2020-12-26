import pathlib
import argparse
import sys
from dataviz_gallery import crud

parser = argparse.ArgumentParser(
    prog='str_to_json_entry',
    description='Convert string entry in pandas series in json entry and output to new flat file')

parser.add_argument(
    '-rpi',
    '--relative_path_in',  # this get's added as Namespace (without --)
    metavar='Relative Path In',
    type=str,
    required=True,
    help='Relative Path which leads to input file',
    action='store',  # stores value to Namespace object
    nargs=1  # expects n (here 1) value for the argument
)

parser.add_argument(
    '-rpo',
    '--relative_path_out',  # this get's added as Namespace (without --)
    metavar='Relative Path Out',
    type=str,
    required=True,
    help='Relative Path which leads to output file',
    action='store',  # stores value to Namespace object
    nargs=1  # expects n (here 1) value for the argument
)

parser.add_argument(
    '-c',
    '--cols',  # this get's added as Namespace (without --)
    metavar='Relevant Columns',
    type=str,
    required=True,
    help='The columns which contain strings which need to be converted',
    action='store',  # stores value to Namespace object
    nargs='+'  # expects 1 or more
)

# Execute the parse_args() method
args = parser.parse_args()

print(args.relative_path_in)
print(args.relative_path_out)
print(args.cols)

if isinstance(args.relative_path_in, list):
    rel_path_in = args.relative_path_in[0]
else:
    rel_path_in = args.relative_path_in

if isinstance(args.relative_path_in, list):
    rel_path_out = args.relative_path_out[0]
else:
    rel_path_out = args.relative_path_out

crud.str_to_json_entry(
        rel_path_in=rel_path_in,
        rel_path_out=rel_path_out,
        cols=args.cols,
    )
