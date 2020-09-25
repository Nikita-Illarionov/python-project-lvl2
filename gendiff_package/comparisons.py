import json


def generate_string(sign, key, value):
    return '  ' + sign + ' ' + key + ': ' + value + '\n'


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json. load(open(file_path2))
    main_list_of_keys = set(data1.keys()) | set(data2.keys())
    result = '{\n'
    for item in main_list_of_keys:
        if item in data1 and item in data2:
            if data1[item] == data2[item]:
                result += generate_string(' ', str(item), str(data1[item]))
            else:
                result += generate_string('-', str(item), str(data1[item]))
                result += generate_string('+', str(item), str(data2[item]))
        elif item in data1:
            result += generate_string('-', str(item), str(data1[item]))
        else:
            result += generate_string('+', str(item), str(data2[item]))
    result += '}\n'
    return result
