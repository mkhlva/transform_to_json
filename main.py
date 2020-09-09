import functools
import json

def decorator(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        resultat = json.dumps(func(*args, **kwargs))
        with open('transform.json', 'w') as f:
            f.write(str(resultat))
            return resultat
    return wrapped



@decorator
def trunk(s_name):
    return (s_name)
jsonn = {'trunk' : None}

print(trunk(jsonn))