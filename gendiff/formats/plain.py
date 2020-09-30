
def generate_plain(input_data):
    def iter(data, way):
        change = ''
        keys = list(data.keys())
        keys.sort()
        if way:
            way += '.'
        for item in keys:
            if data[item][0] == 'deleted':
                change += 'Property ' + "'" + way + str(item) + \
                         "'" + ' was removed\n'
            if data[item][0] == 'added':
                change += 'Property ' + "'" + way + str(item) + \
                         "'" + ' was added with value: ' + \
                         generate_result(data[item][1]) + "\n"
            if data[item][0] == 'changed':
                change += 'Property ' + "'" + way + str(item) + \
                       "'" + ' was updated. From ' + \
                       generate_result(data[item][1]) + \
                       ' to ' + generate_result(data[item][2]) + "\n"
            if data[item][0] == 'not changed' and type(data[item][1]) == dict:
                change += iter(data[item][1], way+str(item))
        return change
    return iter(input_data, '')


def generate_result(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value)
    else:
        return "'" + str(value) + "'"
