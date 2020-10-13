def generate_plain(input_data):
    return generate_main(input_data, '')


def generate_main(data, way):
    plain_format = ''
    keys = list(data.keys())
    keys.sort()
    if way:  # Если у нас не начало пути,то уровни вложенности отделяем точками
        way += '.'
    for item in keys:
        status = data[item][0]
        value = data[item][1]
        if status == 'nested':
            plain_format += generate_main(value, way+str(item))
        elif status != 'not changed':
            plain_format += add_string(data, item, way)
    return plain_format


def add_string(data, item, way):
    status = data[item][0]
    statuses = {
                'deleted': 'was removed',
                'added': 'was added with value: ',
                'changed': 'was updated. From '
               }
    string = "Property '" + way + str(item) + "' " + statuses[status]
    if status == 'deleted':
        return string + '\n'
    string += form_value(data[item][1])
    if status == 'added':
        return string + '\n'
    string += ' to ' + form_value(data[item][2]) + '\n'
    return string


def form_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value)
    return "'" + str(value) + "'"
