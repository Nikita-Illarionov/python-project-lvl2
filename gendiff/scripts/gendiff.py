from gendiff.build_diff import generate_diff
from gendiff.cli import parser


def main():
    parser = parser()
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
