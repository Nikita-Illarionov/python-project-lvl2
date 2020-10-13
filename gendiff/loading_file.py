import json
import yaml


def extract_data(file_path):
    format_of_file = file_path[-4:]
    with open(file_path) as file:
        if format_of_file == 'json':
            result = json.load(file)
        elif format_of_file in {'yaml', '.yml'}:
            result = yaml.safe_load(file)
    return result
