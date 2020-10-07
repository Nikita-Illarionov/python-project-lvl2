from gendiff.diff_functions import generate_diff
from gendiff.formats.string import generate_string
from gendiff.formats.plain import generate_plain
from gendiff.formats.json import generate_json
import sys

way = sys.path[0]
file_path1_json = way + '/fixtures/file1.json'
file_path2_json = way + '/fixtures/file2.json'
file_path1_yaml = way + '/fixtures/file1.yaml'
file_path2_yaml = way + '/fixtures/file2.yaml'

new_file_path1_json = way + '/fixtures/new_file1.json'
new_file_path2_json = way + '/fixtures/new_file2.json'


with open(way + '/fixtures/answer1.txt', 'r') as file:
    answer1 = file.read()

with open(way + '/fixtures/answer2.txt', 'r') as file:
    answer2 = file.read()

with open(way + '/fixtures/answer3.txt', 'r') as file:
    answer3 = file.read()


def test_string_format_json():
    assert generate_string(generate_diff(file_path1_json,
                                         file_path2_json)) == answer1


def test_string_format_yaml():
    assert generate_string(generate_diff(file_path1_yaml,
                                         file_path2_yaml)) == answer1


def test_string_format_json2():
    assert generate_string(generate_diff(new_file_path1_json,
                                         new_file_path2_json)) == answer2


def test_plain_format():
    assert generate_plain(generate_diff(new_file_path1_json,
                                        new_file_path2_json)) == answer3


def test_json_format():
    return isinstance(generate_json(generate_diff(file_path1_json,
                                                  file_path2_json)), dict)
