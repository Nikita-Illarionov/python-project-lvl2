def generate_plain(input_data):
    def iter(data, way):
        plain_format = ''
        keys = get_keys(data)
        way = get_way(way)
        for item in keys:
            status = data[item][0]
            value = data[item][1]
            place = data, item
            if status == 'not changed' and isinstance(value, dict):
                plain_format += iter(value, way+str(item))
            elif status in ['deleted', 'added', 'changed']:
                plain_format += add_string(*place, way, status)
        return plain_format
    return iter(input_data, '')

def get_way(way):
    if way:
        way += '.'
    return way


def add_string(data, item, way, status):
    string = get_description(item, way, status)
    if status != 'deleted':
        string += get_value(data[item][1])
        if status == 'changed':
            string += ' to ' + get_value(data[item][2])
    return string + '\n'
    
def get_description(item, way, status):
    first_part_of_string = "Property '" + way + str(item) + "' "
    dict_of_statuses = {
                        'deleted': 'was removed',
                        'added': 'was added with value: ',
                        'changed': 'was updated. From '
                       }
    return first_part_of_string + dict_of_statuses[status]


def get_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value)
    else:
        return "'" + str(value) + "'"


def get_keys(data):
    keys = list(data.keys())
    keys.sort()
    return keys
