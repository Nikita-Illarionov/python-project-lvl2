states = {
          'deleted': 'was removed',
          'added': 'was added with value: ',
          'changed': 'was updated. From '
         }

def format(input_data):
    return make_format(input_data, '')


def make_format(data, way):
    result = ''
    keys = list(data.keys())
    keys.sort()
    if way:  # Если у нас не начало пути,то уровни вложенности отделяем точками
        way += '.'
    for key in keys:
        state, value = data[key]
        if state == 'changed':
            value, new_value = value
        if state == 'nested':
            result += make_format(value, way+str(key))
        if state == 'deleted':
            result += "Property '" + way + str(key) + "' " + states[state] + '\n'
        if state == 'added':
            result += "Property '" + way + str(key) + "' " + states[state] +\
            to_str(value) + '\n'
        if state == 'changed':
            result += "Property '" + way + str(key) + "' " + states[state] +\
            to_str(value) + ' to ' + to_str(new_value) + '\n'
    return result


def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value)
    return "'" + str(value) + "'"
