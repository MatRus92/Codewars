import json

def wrap(value):
    if isinstance(value, (bool, float, int)) :
        return json.loads('{"value":%s}' % value)

    if isinstance(value, dict):
        return json.loads('{"value":%s}' % json.dumps(value))

    return json.loads('{"value":"%s"}' % value)

print(wrap("my_test")["value"])
print(wrap({'test': 'testy'})["value"])
print(wrap(123)["value"])