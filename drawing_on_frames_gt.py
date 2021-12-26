import os
import cv2
import sys
import json
import random

CURRENT_DIR = "mot17_with_siam/" + sys.argv[1]

lines = []

with open(CURRENT_DIR + "/gt/gt.txt") as f:
    lines = f.readlines()

frames = {}
ids = []
ids_to_colors = {}

for line in lines:
    numbers = line.split(",")
    frame_id = numbers[0]
    object_id = numbers[1]
    object_class = numbers[7]    
    if numbers[6] == 0:
        continue
    if object_id not in ids:
        ids.append(object_id)
    if frame_id in frames.keys():
        new_tracked_object = {
            "object_id": object_id,
            "bb-x": numbers[2],
            "bb-y": numbers[3],
            "bb-width": numbers[4],
            "bb-height": numbers[5],
            "class": object_class            
        }        
        frames[frame_id].append(new_tracked_object)
    else:
        new_tracked_object = {
            "object_id": object_id,
            "bb-x": numbers[2],
            "bb-y": numbers[3],
            "bb-width": numbers[4],
            "bb-height": numbers[5],
            "class": object_class            
        }        
        objects = [new_tracked_object]
        frames[frame_id] = objects

for id in ids:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    ids_to_colors[id] = (r,g,b)


if not os.path.exists(os.path.join(CURRENT_DIR, "images_with_boxes_gt")):
    os.mkdir(CURRENT_DIR + "/images_with_boxes_gt")

for frame_id in frames.keys():
    img = cv2.imread(CURRENT_DIR + "/img1/" + str(frame_id) + ".jpg")
    frame = frames[frame_id]
    for object in frame:
        id = object["object_id"]
        x = int(object["bb-x"])
        y = int(object["bb-y"])
        width = int(object["bb-width"])
        height = int(object["bb-height"])
        cv2.rectangle(img, (x,y), (x+width, y+height), ids_to_colors[id], 2)
        cv2.putText(img, str(id), (x+5, y+25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ids_to_colors[id], 2)
    print(sys.argv[1], " ", frame_id, " writing finished.", end="\n")
    cv2.imwrite(CURRENT_DIR+"/images_with_boxes_gt/" + str(frame_id) + ".jpg", img)