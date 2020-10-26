import json


def render(data):
    return json.dumps(data, sort_keys=True, indent=4) + '\n'
