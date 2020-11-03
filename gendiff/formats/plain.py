def render(input_data):
    return '\n'.join(flatten(make_properties(input_data, ''))) + '\n'


def make_properties(data, way):
    result = []
    if way:  # Если у нас не начало пути,то уровни вложенности отделяем точками
        way += '.'
    for key in sorted(list(data.keys())):
        state, value = data[key]
        if state == 'nested':
            result.append(make_properties(value, way+str(key)))
        if state == 'deleted':
            result.append(make_property(state, key, way))
        if state == 'added':
            result.append(make_property(state, key, way) + to_str(value))
        if state == 'changed':
            value, new_value = value
            result.append(make_property(state, key, way) + to_str(value)
                          + ' to ' + to_str(new_value))
    return result


# Выделил эту функцию, тк иначе CodeClimate ругается и ставит рейтинг D
# (повторяются строки)
def make_property(state, key, way):
    property_ = "Property '" + way + str(key) + "' "
    if state == 'deleted':
        return property_ + 'was removed'
    if state == 'added':
        return property_ + 'was added with value: '
    return property_ + 'was updated. From '


def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    return "'" + str(value) + "'"


def flatten(tree):
    result = []

    def inner(subtree):
        list(map(lambda x: inner(x) if isinstance(x, list) else
                 result.append(x), subtree))
    inner(tree)
    return result
