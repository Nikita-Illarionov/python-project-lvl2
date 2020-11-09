from gendiff.build_diff import generate_diff
import sys
import pytest
import json

way = sys.path[0] + '/fixtures/'
cases = [
         (
             "{path1}".format(path1=way + 'file1.json'),
             "{path2}".format(path2=way + 'file2.json'),
             "{f}".format(f='stylish'),
             "{expected}".format(expected='answer_stylish1.txt')
         ),
         (
             "{path1}".format(path1=way + 'file1.yaml'),
             "{path2}".format(path2=way + 'file2.yaml'),
             "{f}".format(f='stylish'),
             "{expected}".format(expected='answer_stylish1.txt')
         ),
         (
             "{path1}".format(path1=way + 'big_file1.json'),
             "{path2}".format(path2=way + 'big_file2.json'),
             "{f}".format(f='stylish'),
             "{expected}".format(expected='answer_stylish2.txt')
         ),
         (
             "{path1}".format(path1=way + 'big_file1.json'),
             "{path2}".format(path2=way + 'big_file2.json'),
             "{f}".format(f='plain'),
             "{expected}".format(expected='answer_plain.txt')
         ),
         (
             "{path1}".format(path1=way + 'big_file1.yaml'),
             "{path2}".format(path2=way + 'big_file2.yaml'),
             "{f}".format(f='plain'),
             "{expected}".format(expected='answer_plain.txt')
         ),
         (
             "{path1}".format(path1=way + 'file1.yaml'),
             "{path2}".format(path2=way + 'file2.yaml'),
             "{f}".format(f='json'),
             "{expected}".format(expected='answer.json')
         )]


@pytest.mark.parametrize('way1, way2, f, expected', cases)
def test_format(way1, way2, f, expected):
    with open(way + expected, 'r') as file:
        if f == 'json':
            assert json.loads(generate_diff(way1, way2, f)) ==\
                                                   json.load(file)
        else:
            assert generate_diff(way1, way2, f) == file.read()
