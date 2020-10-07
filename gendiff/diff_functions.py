from gendiff.loading_files import extract_data


def generate_diff(file_path1, file_path2):
    data1 = extract_data(file_path1)
    data2 = extract_data(file_path2)

    def iter(obj1, obj2):
        obj = {}
        list_of_keys = get_keys(obj1, obj2)
        for item in list_of_keys:
            dat1 = obj1.get(item)
            dat2 = obj2.get(item)
            if item in obj1 and item in obj2:
                if isinstance(dat1, dict) and isinstance(dat2,dict):
                    extend_object(obj, item, iter(dat1, dat2),
                                  'not changed')
                else:
                    generate_obj(obj, item, dat1, dat2)
            else: 
                generate_dop_obj(obj1, obj, item, dat1, dat2)
        return obj
    return iter(data1, data2)


def generate_obj(obj, item, dat1, dat2):
    if dat1 == dat2:
        extend_object(obj, item, dat1, 'not changed')
    else:
        extend_object(obj, item, [dat1, dat2],
                                  'changed')

def generate_dop_obj(obj1, obj, item, dat1, dat2):
    if item in obj1:
        extend_object(obj, item, dat1, 'deleted')
    else:
        extend_object(obj, item, dat2, 'added')



def extend_object(obj, item, value, status):
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
