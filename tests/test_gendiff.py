from gendiff.build_diff import generate_diff
import sys
import pytest

way = sys.path[0] + '/fixtures/'
file_path1_json = way + 'file1.json'
file_path2_json = way + 'file2.json'
file_path1_yaml = way + 'file1.yaml'
file_path2_yaml = way + 'file2.yaml'

new_file_path1_json = way + 'new_file1.json'
new_file_path2_json = way + 'new_file2.json'


with open(way + 'answer1.txt', 'r') as file:
    answer1 = file.read()

with open(way + 'answer2.txt', 'r') as file:
    answer2 = file.read()

with open(way + 'answer3.txt', 'r') as file:
    answer3 = file.read()


data = [(file_path1_json, file_path2_json, 'string', answer1),
        (file_path1_yaml, file_path2_yaml, 'string', answer1),
        (new_file_path1_json, new_file_path2_json, 'string', answer2)]


@pytest.mark.parametrize('file_path1, file_path2, f, expected', data)
def test_string_format(file_path1, file_path2, f, expected):
    assert generate_diff(file_path1, file_path2, f) == expected


def test_plain_format():
    assert generate_diff(new_file_path1_json,
                         new_file_path2_json, 'plain') == answer3


def test_json_format():
    return isinstance(generate_diff(file_path1_json,
                      file_path2_json, 'json'), dict)
