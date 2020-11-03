start_indent = 2
indent_step = 4


def render(input_data):
    return '{\n' + to_stylish(input_data, start_indent) + '}\n'


def to_stylish(data, indent):
    result = ''
    keys = list(data.keys())
    keys.sort()
    for key in keys:
        state, value = data[key]
        if state == 'nested':
            result += make_property(data, key, indent) + '{\n'
            result += to_stylish(value, indent+indent_step)
            result += indent*' ' + '  }\n'
        else:
            result += make_property(data, key, indent)
    return result


def make_property(data, key, indent):
    state, value = data[key]
    if state == 'changed':
        value, new_value = value
    operator = {
                'nested': '  ',
                'unchanged': '  ',
                'deleted': '- ',
                'added': '+ ',
                'changed': '- '
               }
    result = indent*' ' + operator[state] + str(key) + ': '
    if state == 'nested':
        return result
    result += to_str(value, indent+indent_step) + '\n'
    if state != 'changed':
        return result
    result += indent*' ' + '+ ' + str(key) + ': ' + \
        to_str(new_value, indent+indent_step) + '\n'
    return result


def to_str(value, indent):
    if value == 'None':
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if not isinstance(value, dict):
        return str(value)
    else:
        result = '{'
        keys = list(value.keys())
        for key in keys:
            result += '\n' + indent*' ' + '  ' + str(key) + ': ' + \
                   to_str(value[key], indent+4)
        return result + '\n' + (indent-2)*' ' + '}'
