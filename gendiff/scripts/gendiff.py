import argparse
from gendiff.diff_functions import generate_diff
from gendiff.formats.string import generate_string
from gendiff.formats.plain import generate_plain
from gendiff.formats.json import generate_json
import os


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    arg1 = args.first_file
    arg2 = args.second_file
    for arg in (arg1, arg2):
        if arg[0] != '/':
            arg = os.getcwd() + '/' + arg
    output_format = args.format
    dict_of_formats = {
                       'plain': generate_plain,
                       'json': generate_json
                      }
    if output_format in list(dict_of_formats.keys()):
        output_function = dict_of_formats[output_format]
    else:
        output_function = generate_string
    diff = output_function(generate_diff(arg1, arg2))
    print(diff)


if __name__ == '__main__':
    main()
