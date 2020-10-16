from gendiff.build_diff import generate_diff
import sys
import pytest

way = sys.path[0] + '/fixtures/'

with open(way + 'answer1.txt', 'r') as file:
    answer1 = file.read()

with open(way + 'answer2.txt', 'r') as file:
    answer2 = file.read()

with open(way + 'answer3.txt', 'r') as file:
    answer3 = file.read()


data = [(way + 'file1.json', way + 'file2.json', 'string', answer1),
        (way + 'file1.yaml', way + 'file2.yaml', 'string', answer1),
        (way + 'new_file1.json', way + 'new_file2.json', 'string', answer2)]


@pytest.mark.parametrize('file_path1, file_path2, f, expected', data)
def test_string_format(file_path1, file_path2, f, expected):
    assert generate_diff(file_path1, file_path2, f) == expected


def test_plain_format():
    assert generate_diff(way + 'new_file1.json',
                         way + 'new_file2.json', 'plain') == answer3


def test_json_format():
    return isinstance(generate_diff(way + 'file1.json',
                      way + 'file2.json', 'json'), dict)
