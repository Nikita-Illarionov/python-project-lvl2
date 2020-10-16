def generate_plain(input_data):
    return generate_main(input_data, '')


def generate_main(data, way):
    plain_format = ''
    keys = list(data.keys())
    keys.sort()
    if way:  # Если у нас не начало пути,то уровни вложенности отделяем точками
        way += '.'
    for key in keys:
        status, value = data[key]
        if status == 'nested':
            plain_format += generate_main(value, way+str(key))
        elif status != 'not changed':
            plain_format += add_string(data, key, way)
    return plain_format


def add_string(data, key, way):
    status, value = data[key]
    if status == 'changed':
        value, new_value = value
    statuses = {
                'deleted': 'was removed',
                'added': 'was added with value: ',
                'changed': 'was updated. From '
               }
    string = "Property '" + way + str(key) + "' " + statuses[status]
    if status == 'deleted':
        return string + '\n'
    string += form_value(value)
    if status == 'added':
        return string + '\n'
    string += ' to ' + form_value(new_value) + '\n'
    return string


def form_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value)
    return "'" + str(value) + "'"
