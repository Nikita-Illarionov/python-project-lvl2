from gendiff.build_diff import generate_diff
import sys
import pytest

way = sys.path[0] + '/fixtures/'


def read_file(name):
    with open(way + name, 'r') as file:
        return file.read()


cases = [(way + 'empty_file1.json', way + 'empty_file2.json', 'plain', ''),
         (way + 'file1.json', way + 'file2.json', 'stylish',
         read_file('answer_stylish1.txt')),
         (way + 'file1.yaml', way + 'file2.yaml', 'stylish',
         read_file('answer_stylish1.txt')),
         (way + 'big_file1.json', way + 'big_file2.json', 'stylish',
         read_file('answer_stylish2.txt')),
         (way + 'big_file1.json', way + 'big_file2.json', 'plain',
         read_file('answer_plain.txt')),
         (way + 'file1.yaml', way + 'file2.yaml', 'json',
         read_file('answer_json.txt'))]


@pytest.mark.parametrize('file_path1, file_path2, f, expected', cases)
def test_format(file_path1, file_path2, f, expected):
    assert generate_diff(file_path1, file_path2, f) == expected
