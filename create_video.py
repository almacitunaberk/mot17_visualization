import cv2
import os
import sys
import json

CURRENT_DIR = "mot17_with_siam/" + sys.argv[1]

print("Working on " + CURRENT_DIR, end="\n")

f = open(CURRENT_DIR + "/siammot/" + sys.argv[1] + ".json")
data = json.load(f)
size = (data["metadata"]["resolution"]["width"], data["metadata"]["resolution"]["height"])
fps = data["metadata"]["fps"]
number_of_frames = data["metadata"]["number_of_frames"]

siam_video_creator = cv2.VideoWriter("SIAM-" + sys.argv[1] + ".mp4", cv2.VideoWriter_fourcc(*'MP4V'), fps, size)

# ----- CREATING SIAM RESULTS VIDEO ---------
for i in range(number_of_frames):
    img = cv2.imread("images_with_boxes/" + str(i+1) + ".jpg")
    siam_video_creator.write(img)
siam_video_creator.release()

# ------ CREATING GROUND TRUTH VIDEO --------
    