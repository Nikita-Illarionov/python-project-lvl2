def generate_string(input_data):
    n = 2

    def iter(data, n):
        answer = ''
        keys = list(data.keys())
        keys.sort()
        for item in keys:
            if data[item][0] == 'not changed' and type(data[item][1]) == dict:
                answer += n*' ' + '  ' + str(item) + ': ' + '{\n'
                answer += iter(data[item][1], n+4)
                answer += n*' ' + '  }\n'
            elif data[item][0] == 'not changed':
                answer += n*' ' + '  ' + str(item) + ': ' + \
                       dop_generate_string(data[item][1], n+4) + '\n'
            elif data[item][0] == 'changed':
                answer += n*' ' + '- ' + str(item) + ': ' + \
                       dop_generate_string(data[item][1], n+4) + '\n'
                answer += n*' ' + '+ ' + str(item) + ': ' + \
                    dop_generate_string(data[item][2], n+4) + '\n'
            elif data[item][0] == 'deleted':
                answer += n*' ' + '- ' + str(item) + ': ' + \
                       dop_generate_string(data[item][1], n+4) + '\n'
            elif data[item][0] == 'added':
                answer += n*' ' + '+ ' + str(item) + ': ' + \
                       dop_generate_string(data[item][1], n+4) + '\n'
        return answer
    return '{\n' + iter(input_data, n) + '}\n'


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
