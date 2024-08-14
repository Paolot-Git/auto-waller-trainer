import json
import pprint

USER_DATA_PATH = "/home/paolot/.local/share/FoundryVTT/Data/"

# Use "JSON.stringify(Scenes.instance)" on Console for the json and copy string contents
f = open("a.json", "r")
data = json.load(f)

for x in data:
    if x["background"]["src"] is None:
        continue

    name = x["name"]
    grid_size = x["grid"]["size"]
    offset_x = x["padding"] * x["width"]
    offset_y = x["padding"] * x["height"]
    background_path = USER_DATA_PATH + x["background"]["src"]
    walls = x["walls"]

    data = {name, grid_size, offset_x, offset_y, background_path}

    try:
        pprint.pprint(x["walls"])
    except IndexError:
        print("this can't happen")
