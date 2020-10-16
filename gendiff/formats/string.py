indent = 2
indent_step = 4


def generate_string(input_data):
    return '{\n' + generate_main(input_data, indent) + '}\n'


def generate_main(data, n):
    string_format = ''
    keys = list(data.keys())
    keys.sort()
    for key in keys:
        status, value = data[key]
        if status == 'nested':
            string_format += add_string(data, key, n) + '{\n'
            string_format += generate_main(value, n+indent_step)
            string_format += n*' ' + '  }\n'
        else:
            string_format += add_string(data, key, n)
    return string_format


def add_string(data, key, n):
    status, value = data[key]
    if status == 'changed':
        value, new_value = value
    statuses = {
                'nested': '  ',
                'not changed': '  ',
                'deleted': '- ',
                'added': '+ ',
                'changed': '- '
               }
    string = ''
    string += n*' ' + statuses[status] + str(key) + ': '
    if status == 'nested':
        return string
    string += form_value(value, n+indent_step) + '\n'
    if status != 'changed':
        return string
    string += n*' ' + '+ ' + str(key) + ': ' + \
        form_value(new_value, n+indent_step) + '\n'
    return string


def form_value(value, n):
    if not isinstance(value, dict):
        return str(value)
    else:
        answer = '{'
        keys = list(value.keys())
        for key in keys:
            answer += '\n' + n*' ' + '  ' + str(key) + ': ' + \
                   form_value(value[key], n+4)
        return answer + '\n' + (n-2)*' ' + '}'
