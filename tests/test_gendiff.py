from gendiff.build_diff import generate_diff, make_diff
import sys
import pytest
import json

way = sys.path[0] + '/fixtures/'


def read_file(name, f='txt'):
    with open(way + name, 'r') as file:
        if f == 'json':
            return json.load(file)
        return file.read()


diff1 = {
              'timeout': ('changed', (50, 20)),
              'host': ('unchanged', 'hexlet.io'),
              'proxy': ('deleted', '123.234.53.22'),
              'verbose': ('added', True),
              'follow': ('deleted', False)
        }
diff2 = {
              'common': ('nested', {
                  'setting3': ('changed', (True, {'key': 'value'})),
                  'setting6': ('nested', {
                      'doge': ('nested', {
                          'wow': ('changed', ('too much', 'so much'))
                      }),
                      'key': ('unchanged', 'value'),
                      'ops': ('added', 'vops')
                  }),
                  'setting1': ('unchanged', 'Value 1'),
                  'setting2': ('deleted', 200),
                  'setting5': ('added', {'key5': 'value5'}),
                  'setting4': ('added', 'blah blah'),
                  'follow': ('added', False)
              }),
              'group1': ('nested', {
                  'baz': ('changed', ('bas', 'bars')),
                  'nest': ('changed', ({'key': 'value'}, 'str')),
                  'foo': ('unchanged', 'bar')
              }),
              'group2': ('deleted', {'abc': 12345, 'deep': {'id': 45}}),
              'group3': ('added', {
                              'fee': 100500,
                              'deep': {'id': {'number': 45}}
                         })
        }


cases_for_diff = [(read_file('file1.json', f='json'),
                   read_file('file2.json', f='json'),
                   diff1),
                  (read_file('big_file1.json', f='json'),
                   read_file('big_file2.json', f='json'),
                   diff2)]


cases_for_render = [
         (way + 'small_file1.json', way + 'small_file2.json', 'plain',
          read_file('answer_small_plain.txt')),
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


@pytest.mark.parametrize('data1, data2, expected', cases_for_diff)
def test_diff(data1, data2, expected):
    assert make_diff(data1, data2) == expected


@pytest.mark.parametrize('path1, path2, f, expected', cases_for_render)
def test_format(path1, path2, f, expected):
    assert generate_diff(path1, path2, f) == expected
