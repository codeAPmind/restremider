
import json
from common import load_json

def getLicense():
    data =  load_json("License.json")
    i = 0
    for key, value in data.items():
        if "License" in key:
            print("new vluae", value)
            return value
    return ""