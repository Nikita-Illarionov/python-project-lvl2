def generate_string(input_data):
    n = 2
    step = 4

    def iter(data, n):
        answer = ''
        keys = get_keys(data)
        for item in keys:
            status = data[item][0]
            value = data[item][1]
            if status == 'not changed' and isinstance(value, dict):
                answer += start_of_string(item, status, n) + '{\n'
                answer += iter(value, n+step)
                answer += n*' ' + '  }\n'
            elif status in ['not changed', 'deleted', 'added']:
                answer += start_of_string(item, status, n) + \
                       get_string_value(value, n+step) + '\n'
            elif status == 'changed':
                answer += start_of_string(item, status+'-', n) + \
                       get_string_value(value, n+step) + '\n' +\
                       start_of_string(item, status+'+', n) + \
                       get_string_value(data[item][2], n+step) + '\n'
        return answer
    return '{\n' + iter(input_data, n) + '}\n'


def start_of_string(item, status, n):
    dict_of_statuses = {
                         'not changed': '  ',
                         'deleted': '- ',
                         'added': '+ ',
                         'changed-': '- ',
                         'changed+': '+ '
                        }
    return n*' ' + dict_of_statuses[status] + str(item) + ': '


def get_string_value(d, n):
    if not isinstance(d, dict):
        return str(d)
    else:
        answer = '{'
        keys = list(d.keys())
        for item in keys:
            answer += '\n' + n*' ' + '  ' + str(item) + ': ' + \
                   get_string_value(d[item], n+4)
        return answer + '\n' + (n-2)*' ' + '}'


def get_keys(data):
    keys = list(data.keys())
    keys.sort()
    return keys
