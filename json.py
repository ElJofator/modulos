import json

path = "data.json"

with open(path, "r") as f:
    camper = json.loads(f.read())