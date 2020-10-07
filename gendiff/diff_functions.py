from gendiff.loading_file import extract_data


def generate_diff(file_path1, file_path2):
    file_data1 = extract_data(file_path1)
    file_data2 = extract_data(file_path2)

    def iter(data1, data2):
        data = {}
        list_of_keys = get_keys(data1, data2)
        for item in list_of_keys:
            value1 = data1.get(item)
            value2 = data2.get(item)
            place = data, item
            if item in data1 and item in data2:
                if isinstance(value1, dict) and isinstance(value2, dict):
                    add_dictionary(*place, iter(value1, value2))
                elif value1 == value2:
                    add_value(*place, value1, 'not changed')
                else:
                    add_value(*place, [value1, value2], 'changed')
            elif item in data1:
                add_value(*place, value1, 'deleted')
            else:
                add_value(*place, value2, 'added')
        return data
    return iter(file_data1, file_data2)


def add_dictionary(place, item, value):
    add_value(place, item, value, 'not changed')


def add_value(data, item, value, status):
    data[item] = [status]
    if status == 'not changed':
        data[item].append(value)
    elif status == 'changed':
        data[item].append(value[0])
        data[item].append(value[1])
    elif status == 'deleted':
        data[item].append(value)
    elif status == 'added':
        data[item].append(value)
    else:
        print('Incorrect status.\n')


def get_keys(data1, data2):
    list_of_keys = list(set(data1.keys()) | set(data2.keys()))
    list_of_keys.sort()
    return list_of_keys
