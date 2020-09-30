from gendiff.loading_files import extract_data


def generate_diff(file_path1, file_path2):
    data1 = extract_data(file_path1)
    data2 = extract_data(file_path2)

    def iter(obj1, obj2):
        obj = {}
        list_of_keys = get_keys(obj1, obj2)
        for item in list_of_keys:
            if item in obj1 and item in obj2:
                if type(obj1[item]) == dict and type(obj2[item]) == dict:
                    extend_object(obj, item, iter(obj1[item], obj2[item]),
                                  status='not changed')
                elif obj1[item] == obj2[item]:
                    extend_object(obj, item, obj1[item], status='not changed')
                else:
                    extend_object(obj, item, [obj1[item], obj2[item]],
                                  status='changed')
            elif item in obj1:
                extend_object(obj, item, obj1[item], status='deleted')
            else:
                extend_object(obj, item, obj2[item], status='added')
        return obj
    return iter(data1, data2)


def extend_object(obj, item, value, status='not changed'):
    obj[item] = [status]
    if status == 'not changed':
        obj[item].append(value)
    elif status == 'changed':
        obj[item].append(value[0])
        obj[item].append(value[1])
    elif status == 'deleted':
        obj[item].append(value)
    elif status == 'added':
        obj[item].append(value)
    else:
        print('Incorrect status.\n')


def get_keys(obj1, obj2):
    list_of_keys = list(set(obj1.keys()) | set(obj2.keys()))
    list_of_keys.sort()
    return list_of_keys


def get_value(obj, item):
    return obj[item]
