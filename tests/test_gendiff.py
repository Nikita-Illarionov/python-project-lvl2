from gendiff.build_diff import generate_diff
import sys
import pytest

way = sys.path[0] + '/fixtures/'


def open_file(name):
    with open(way + name, 'r') as file:
        return file.read()


data = [(way + 'file1.json', way + 'file2.json', 'string',
         open_file('answer1.txt')),
        (way + 'file1.yaml', way + 'file2.yaml', 'string',
         open_file('answer1.txt')),
        (way + 'new_file1.json', way + 'new_file2.json', 'string',
         open_file('answer2.txt'))]


@pytest.mark.parametrize('file_path1, file_path2, f, expected', data)
def test_string_format(file_path1, file_path2, f, expected):
    assert generate_diff(file_path1, file_path2, f) == expected


def test_plain_format():
    assert generate_diff(way + 'new_file1.json',
                         way + 'new_file2.json',
                         'plain') == open_file('answer3.txt')


def test_json_format():
    return isinstance(generate_diff(way + 'file1.json',
                      way + 'file2.json', 'json'), dict)
