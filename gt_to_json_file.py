import os
import sys
import json

sys.path.insert(1, 'pymot')

CURRENT_DIR = "mot17_with_siam/" + sys.argv[1]

groundtruth = [{ "frames": [], "class": "video" }]
frames = {}
f = open(CURRENT_DIR + "/gt/gt.txt")
lines = f.readlines()
f.close()

for line in lines:
    numbers = line.split(",")
    frame_id = numbers[0]
    object_id = numbers[1]
    is_considered = numbers[6]
    object_class = numbers[7]
    if is_considered == 0:
        continue
    if frame_id in frames.keys():
        new_annotation = {
            "dco": True,
            "height": numbers[5],
            "width": numbers[4],
            "x": numbers[2],
            "y": numbers[3],
            "id": object_id             
        }
        frames[frame_id].append(new_annotation)
    else:
        new_annotation = {
            "dco": True,
            "height": numbers[5],
            "width": numbers[4],
            "x": numbers[2],
            "y": numbers[3],
            "id": object_id             
        }
        annotations = [new_annotation]
        frames[frame_id] = annotations

for frame_id in frames.keys():
    new_frame_object = {
        "timestamp": frame_id,
        "num": frame_id,
        "class": "frame",
        "annotations": frames[frame_id]
    }
    groundtruth[0]["frames"].append(new_frame_object)

print("Done for the file ", sys.argv[1], end="\n")
print("Creating JSON file for ", sys.argv[1], end="\n")

json_string = json.dumps(groundtruth)

os.mkdir(CURRENT_DIR + "/gt_json")
os.chdir(CURRENT_DIR + "/gt_json")

with open("gt_json.json", "w") as outfile:
    outfile.write(json_string)

os.chdir("..")
os.chdir("..")

