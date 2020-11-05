from gendiff.build_diff import generate_diff
import sys
import pytest
import json

way = sys.path[0] + '/fixtures/'
cases = [
         (way + 'small_file1.json', way + 'small_file2.json', 'plain',
          'answer_small_plain.txt'),
         (way + 'file1.json', way + 'file2.json', 'stylish',
          'answer_stylish1.txt'),
         (way + 'file1.yaml', way + 'file2.yaml', 'stylish',
          'answer_stylish1.txt'),
         (way + 'big_file1.json', way + 'big_file2.json', 'stylish',
          'answer_stylish2.txt'),
         (way + 'big_file1.json', way + 'big_file2.json', 'plain',
          'answer_plain.txt'),
         (way + 'file1.yaml', way + 'file2.yaml', 'json',
          'answer.json')]


@pytest.mark.parametrize('way1, way2, f, expected', cases)
def test_format(way1, way2, f, expected):
    with open(way + expected, 'r') as file:
        if f == 'json':
            assert json.loads(generate_diff(way1, way2, f)) == json.load(file)
        else:
            assert generate_diff(way1, way2, f) == file.read()
