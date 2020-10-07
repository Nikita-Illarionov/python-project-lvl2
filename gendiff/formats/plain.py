
def generate_plain(input_data):
    def iter(data, way):
        change = ''
        keys = list(data.keys())
        keys.sort()
        if way:
            way += '.'
        for item in keys:
            status = data[item][0]
            start_of_string = "Property '" + way + str(item) + "'"
            if status == 'not changed' and type(data[item][1]) == dict:
                change += iter(data[item][1], way+str(item))
            if status == 'deleted':
                change += start_of_string + ' was removed\n'
            if status == 'added':
                change += start_of_string + ' was added with value: ' + \
                         generate_result(data[item][1]) + "\n"
            if status == 'changed':
                change += start_of_string + ' was updated. From ' + \
                       generate_result(data[item][1]) + \
                       ' to ' + generate_result(data[item][2]) + "\n"
        return change
    return iter(input_data, '')


def generate_result(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value)
    else:
        return "'" + str(value) + "'"
