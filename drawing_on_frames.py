import sys
import os
import random
from types import new_class
import cv2
import json

CURRENT_DIR = "mot17_with_siam/" + sys.argv[1]

f = open(CURRENT_DIR + "/siammot/" + sys.argv[1] + ".json")
data = json.load(f)

number_of_frames = data["metadata"]["number_of_frames"]

frames = {}
ids = []
ids_to_colors = {}

for entity in data["entities"]:
    frame_id = entity["blob"]["frame_idx"] + 1
    object_id = entity["id"]
    bounding_box = entity["bb"]
    if object_id == -1:
        continue
    if object_id not in ids:
        ids.append(object_id)
    if frame_id in frames.keys():
        new_object = {"object_id" : object_id, "bounding_box": bounding_box}
        objects = frames[frame_id]
        objects.append(new_object)
    else:
        new_object = {"object_id" : object_id, "bounding_box": bounding_box}
        objects = [new_object]
        frames[frame_id] = objects

for id in ids:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    ids_to_colors[id] = (r,g,b)

os.mkdir(CURRENT_DIR + "/images_with_boxes")

for frame_id in range(number_of_frames):
    img = cv2.imread(CURRENT_DIR + "/img1/" + str(frame_id + 1) + ".jpg")
    frame = frames[frame_id + 1]
    for object in frame:
        id = object["object_id"]
        bounding_box = object["bounding_box"]
        x = int(bounding_box[0])
        y = int(bounding_box[1])
        w = int(bounding_box[2])
        h = int(bounding_box[3])
        cv2.rectangle(img, (x,y), (x+w, y+h), ids_to_colors[id], 2)
        cv2.putText(img, str(id), (x+5, y+25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ids_to_colors[id], 2)
    cv2.imwrite(CURRENT_DIR + "/images_with_boxes/" + str(frame_id+1) + ".jpg", img)
    