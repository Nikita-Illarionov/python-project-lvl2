import argparse
import json
from gendiff.comparisons import generate_diff
import os


def main():
    print('Hello')
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
    diff = generate_diff(arg1, arg2)
    print(diff)
    



if __name__ == '__main__':
    main()
