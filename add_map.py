import json
import pprint

USER_DATA_PATH = "/home/paolot/.local/share/FoundryVTT/Data/"


f = open("a.json", "r")
data = json.load(f)
for z in data:
    if z["background"]["src"] is None:
        continue

    name = z["name"]
    grid_size = z["grid"]["size"]
    offset_x = z["padding"] * z["width"]
    offset_y = z["padding"] * z["height"]
    background_path = USER_DATA_PATH + z["background"]["src"]
    walls = z["walls"]

    data = {name, grid_size, offset_x, offset_y, background_path}

    try:
        pprint.pprint(z["walls"][0]["c"])
    except IndexError:
        pass
