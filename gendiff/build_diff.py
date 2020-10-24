from gendiff.loading_file import extract_data
from gendiff.formats import plain, json, stylish


def generate_diff(file_path1, file_path2, output_format):
    file_data1 = extract_data(file_path1)
    file_data2 = extract_data(file_path2)
    formats = {
               'plain': plain.format,
               'json': json.format,
               'stylish': stylish.format
              }
    generate_format = formats[output_format]
    return generate_format(make_diff(file_data1, file_data2))


def make_diff(data1, data2):
    data = {}
    for key in data1.keys() & data2.keys():
        if data1[key] == data2[key]:
            data[key] = 'unchanged', data1[key]
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            data[key] = 'nested', make_diff(data1[key], data2[key])
        else:
            data[key] = 'changed', (data1[key], data2[key])
    for key in data1.keys() - data2.keys():
        data[key] = 'deleted', data1[key]
    for key in data2.keys() - data1.keys():
        data[key] = 'added', data2[key]
    return data
