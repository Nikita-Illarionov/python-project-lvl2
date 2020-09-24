import argparse
import json
from gendiff.comparisons import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    arg1 = args.first_file
    arg2 = args.second_file
    diff = generate_diff(arg1, arg2)
    print(diff)
    



if __name__ == '__main__':
    main()
