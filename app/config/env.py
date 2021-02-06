import os
from enum import Enum

class Variable(Enum):
    BASE_URL_LOCATION = 'http://0.0.0.0:8081'

def _find(env):
    try:
        return os.environ[env.name]
    except KeyError:
        print('Environment {name} not found, the default value is {value}'.format(name=env.name, value=env.value))
    return env.value

class Env:
    def __init__(self):
        self.base_url_location = _find(Variable.BASE_URL_LOCATION)