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
            result.append(f"Property '{way}{key}' was removed")
        if state == 'added':
            result.append("Property '{}{}' was added with value: {}".format(
                                                    way, key, to_str(value)))
        if state == 'changed':
            value, new_value = value
            result.append("Property '{}{}' was updated. From {} to {}".format(
                                  way, key, to_str(value), to_str(new_value)))
    return result


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
