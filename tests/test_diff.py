from gendiff.build_diff import make_diff
from gendiff.loading_file import extract_data
from fixtures import diff1, diff2
import sys
import pytest

way = sys.path[0] + '/fixtures/'

cases = [(extract_data(way + 'file1.json'),
          extract_data(way + 'file2.json'), diff1),
         (extract_data(way + 'big_file1.json'),
          extract_data(way + 'big_file2.json'), diff2)]


@pytest.mark.parametrize('data1, data2, expected', cases)
def test_diff(data1, data2, expected):
    assert make_diff(data1, data2) == expected
