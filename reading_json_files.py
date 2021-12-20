import json
import random

f = open("MOT17-02-SDP.json")
data = json.load(f)
frames = {}
ids = []
ids_to_colors = {}

for entity in data["entities"]:
    frame_id = entity["blob"]["frame_idx"] + 1
    print(frame_id, end="\n")
    object_id = entity["id"]
    print(object_id, end="\n")
    bounding_box = entity["bb"]
    print(bounding_box, end="\n")
    if object_id not in ids:
        ids.append(object_id)
    if object_id == -1:
        continue
    if frame_id in frames.keys():
        new_obj = {"object_id" : object_id, "bounding_box": bounding_box }        
        objects = frames.get(frame_id)
        objects.append(new_obj)
    else:
        new_obj = {"object_id": object_id, "bounding_box": bounding_box}
        objects = [new_obj]
        frames[frame_id] = objects

for id in ids:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    ids_to_colors[id] = (r,g,b)