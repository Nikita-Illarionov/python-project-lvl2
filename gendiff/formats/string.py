indent = 2
indent_step = 4


def generate_string(input_data):
    return '{\n' + generate_main(input_data, indent) + '}\n'


def generate_main(data, n):
    string_format = ''
    keys = list(data.keys())
    keys.sort()
    for item in keys:
        status = data[item][0]
        value = data[item][1]
        if status == 'nested':
            string_format += add_string(data, item, n) + '{\n'
            string_format += generate_main(value, n+indent_step)
            string_format += n*' ' + '  }\n'
        else:
            string_format += add_string(data, item, n)
    return string_format


def add_string(data, item, n):
    statuses = {
                'nested': '  ',
                'not changed': '  ',
                'deleted': '- ',
                'added': '+ ',
                'changed': '- '
               }
    status = data[item][0]
    string = ''
    string += n*' ' + statuses[status] + str(item) + ': '
    if status == 'nested':
        return string
    elif status != 'changed':
        string += form_value(data[item][1], n+indent_step) + '\n'
        return string
    else:
        string += form_value(data[item][1], n+indent_step) + '\n'
        string += n*' ' + '+ ' + str(item) + ': '
        string += form_value(data[item][2], n+indent_step) + '\n'
        return string


def form_value(value, n):
    if not isinstance(value, dict):
        return str(value)
    else:
        answer = '{'
        keys = list(value.keys())
        for item in keys:
            answer += '\n' + n*' ' + '  ' + str(item) + ': ' + \
                   form_value(value[item], n+4)
        return answer + '\n' + (n-2)*' ' + '}'
