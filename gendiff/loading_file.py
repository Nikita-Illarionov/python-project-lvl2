import json
import yaml


def extract_data(file_path):
    format_of_file = file_path[-4:]
    if format_of_file == 'json':
        return json.load(open(file_path))
    elif format_of_file in {'yaml', '.yml'}:
        return yaml.safe_load(open(file_path))
    else:
        print('Incorrect format. Use only "json" or "yaml/yml" format')
        return
