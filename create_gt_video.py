import os
import sys
import json
import cv2

CURRENT_DIR = "mot17_with_siam/" + sys.argv[1]

f = open(CURRENT_DIR + "/siammot/" + sys.argv[1] + ".json")
data = json.load(f)
size = (data["metadata"]["resolution"]["width"], data["metadata"]["resolution"]["height"])
fps = data["metadata"]["fps"]
number_of_frames = data["metadata"]["number_of_frames"]

os.chdir(CURRENT_DIR + "/videos")

gt_video_creator = cv2.VideoWriter("GT-" + sys.argv[1] + ".mp4", cv2.VideoWriter_fourcc(*'MP4V'), fps, size)

for i in range(number_of_frames):
    img = cv2.imread("../images_with_boxes_gt/" + str(i+1) + ".jpg")
    gt_video_creator.write(img)
gt_video_creator.release()

print(sys.argv[1], " finished.", end="\n")
os.chdir("..")
os.chdir("..")