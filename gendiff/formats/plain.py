states = {
          'deleted': 'was removed',
          'added': 'was added with value: ',
          'changed': 'was updated. From '
         }


def render(input_data):
    return make_format(input_data, '')


def make_format(data, way):
    result = ''
    if way:  # Если у нас не начало пути,то уровни вложенности отделяем точками
        way += '.'
    for key in sorted(list(data.keys())):
        state, value = data[key]
        if state == 'nested':
            result += make_format(value, way+str(key))
        if state == 'deleted':
            result += make_property(state, key, way) + '\n'
        if state == 'added':
            result += make_property(state, key, way) + to_str(value) + '\n'
        if state == 'changed':
            value, new_value = value
            result += (make_property(state, key, way) + to_str(value) + ' to '
                       + to_str(new_value) + '\n')
    return result


# Выделил эту функцию, тк иначе CodeClimate ругается и ставит рейтинг D
# (повторяются строки)
def make_property(state, key, way):
    return "Property '" + way + str(key) + "' " + states[state]


def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool) or value is None:
        return str(value)
    return "'" + str(value) + "'"
