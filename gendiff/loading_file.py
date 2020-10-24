import json
import yaml
import os


def extract_data(file_path):
    with open(file_path) as file:
        return parse(file, get_type(file_path))


def parse(file_, type_):
    if type_ == '.json':
        return json.load(file_)
    return yaml.safe_load(file_)


def get_type(file_path):
    return os.path.splitext(file_path)[1]
