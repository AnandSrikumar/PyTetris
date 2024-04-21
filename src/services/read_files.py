import json

def read_json(path):
    with open(path, 'r') as fp:
        payload = json.load(fp)
    return payload

def write_json(path, content):
    with open(path,'w') as fp:
        json.dump(content, fp)