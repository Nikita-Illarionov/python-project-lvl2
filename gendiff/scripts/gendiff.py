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
    if arg1[0] != '/':
        arg1 = os.getcwd() + '/' + arg1
    arg2 = args.second_file
    if arg2[0] != '/':
        arg2 = os.getcwd() + '/' + arg2
    output_format = args.format
    if output_format == 'plain':
        output_function = generate_plain
    elif output_format == 'json':
        output_function = generate_json
    else:
        output_function = generate_string
    diff = output_function(generate_diff(arg1, arg2))
    print(diff)


if __name__ == '__main__':
    main()
