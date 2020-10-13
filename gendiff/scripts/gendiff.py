import argparse
from gendiff.build_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output',
                        default='string')
    args = parser.parse_args()
    arg1 = args.first_file
    arg2 = args.second_file
    diff = generate_diff(arg1, arg2, args.format)
    print(diff)


if __name__ == '__main__':
    main()
