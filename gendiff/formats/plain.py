def generate_plain(input_data):
    def iter(data, way):
        change = ''
        keys = list(data.keys())
        keys.sort()
        way = correct_way(way)
        for item in keys:
            status = data[item][0]
            value = data[item][1]
            if status == 'not changed' and isinstance(value, dict):
                change += iter(value, way+str(item))
            elif status in ['deleted', 'added', 'changed']:
                change += gen_string(data, item, way, status)
        return change
    return iter(input_data, '')

def correct_way(way):
    if way:
        way += '.'
    return way


def gen_string(data, item, way, status):
    result = start_of_string(item, way, status)
    if status != 'deleted':
        result += generate_result(data[item][1])
        if status == 'changed':
            result += ' to ' + generate_result(data[item][2])
    return result + '\n'
    
def start_of_string(item, way, status):
    start = "Property '" + way + str(item) + "' "
    dict_of_statuses = {
                        'deleted': 'was removed',
                        'added': 'was added with value: ',
                        'changed': 'was updated. From '
                       }
    return start + dict_of_statuses[status]


def generate_result(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value)
    else:
        return "'" + str(value) + "'"
