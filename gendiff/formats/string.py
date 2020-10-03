def generate_string(input_data):
    n = 2

    def iter(data, n):
        answer = ''
        keys = list(data.keys())
        keys.sort()
        for item in keys:
            status = data[item][0]
            value = data[item][1]
            if status == 'not changed' and type(value) == dict:
                answer += start_of_string(item, status, n) + '{\n'
                answer += iter(value, n+4)
                answer += n*' ' + '  }\n'
            elif status == 'not changed':
                answer += start_of_string(item, status, n) + \
                       dop_generate_string(value, n+4) + '\n'
            elif status == 'changed':
                answer += start_of_string(item, status+'-', n) + \
                       dop_generate_string(data[item][1], n+4) + '\n'
                answer += start_of_string(item, status+'+', n) + \
                    dop_generate_string(data[item][2], n+4) + '\n'
            elif status == 'deleted':
                answer += start_of_string(item, status, n) + \
                       dop_generate_string(value, n+4) + '\n'
            elif status == 'added':
                answer += start_of_string(item, status, n) + \
                       dop_generate_string(value, n+4) + '\n'
        return answer
    return '{\n' + iter(input_data, n) + '}\n'


def start_of_string(item, status, n):
    if status == 'not changed':
        return n*' ' + '  ' + str(item) + ': '
    elif status == 'changed-' or status == 'deleted':
        return n*' ' + '- ' + str(item) + ': '
    elif status == 'changed+' or status == 'added':
        return n*' ' + '+ ' + str(item) + ': '


def dop_generate_string(d, n):
    if not isinstance(d, dict):
        return str(d)
    else:
        answer = '{'
        keys = list(d.keys())
        for item in keys:
            answer += '\n' + n*' ' + '  ' + str(item) + ': ' + \
                   dop_generate_string(d[item], n+4)
        return answer + '\n' + (n-2)*' ' + '}'
