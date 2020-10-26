indent = 2
indent_step = 4


def render(input_data):
    return '{\n' + make_format(input_data, indent) + '}\n'


def make_format(data, n):
    result = ''
    keys = list(data.keys())
    keys.sort()
    for key in keys:
        state, value = data[key]
        if state == 'nested':
            result += make_property(data, key, n) + '{\n'
            result += make_format(value, n+indent_step)
            result += n*' ' + '  }\n'
        else:
            result += make_property(data, key, n)
    return result


def make_property(data, key, n):
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
    result = n*' ' + operator[state] + str(key) + ': '
    if state == 'nested':
        return result
    result += to_str(value, n+indent_step) + '\n'
    if state != 'changed':
        return result
    result += n*' ' + '+ ' + str(key) + ': ' + \
        to_str(new_value, n+indent_step) + '\n'
    return result


def to_str(value, n):
    if not isinstance(value, dict):
        return str(value)
    else:
        result = '{'
        keys = list(value.keys())
        for key in keys:
            result += '\n' + n*' ' + '  ' + str(key) + ': ' + \
                   to_str(value[key], n+4)
        return result + '\n' + (n-2)*' ' + '}'
