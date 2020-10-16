from gendiff.loading_file import extract_data
from gendiff.formats.string import generate_string
from gendiff.formats.plain import generate_plain
from gendiff.formats.json import generate_json


def generate_diff(file_path1, file_path2, output_format):
    file_data1 = extract_data(file_path1)
    file_data2 = extract_data(file_path2)
    formats = {
               'plain': generate_plain,
               'json': generate_json,
               'string': generate_string
              }
    output_function = formats[output_format]
    return output_function(generate_main(file_data1, file_data2))


def generate_main(data1, data2):
    data = {}
    set1 = set(data1.keys())
    set2 = set(data2.keys())
    for key in set1 & set2:
        value1 = data1[key]
        value2 = data2[key]
        if value1 == value2:
            data[key] = 'not changed', value1
        elif isinstance(value1, dict) and isinstance(value2, dict):
            data[key] = 'nested', generate_main(value1, value2)
        else:
            data[key] = 'changed', (value1, value2)
    for key in set1 - set2:
        data[key] = 'deleted', data1[key]
    for key in set2 - set1:
        data[key] = 'added', data2[key]
    return data
