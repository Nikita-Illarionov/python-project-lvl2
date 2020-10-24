import json

def format(data):
    return json.dumps(data, sort_keys=True, indent=4) + '\n'
