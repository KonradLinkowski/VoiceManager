import json

def parse(path):
    with open(path) as json_file:
        return json.load(json_file)
