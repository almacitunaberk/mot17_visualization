import os
import sys

#print(sys.argv[1])
CURRENT_DIR = "mot17_with_siam/" + sys.argv[1] + "/img1/"
for file in os.listdir(CURRENT_DIR):
    file_int = int(file[:6])
    new_name_of_the_image = str(file_int) + ".jpg"
    os.rename(CURRENT_DIR + file, CURRENT_DIR + new_name_of_the_image)
