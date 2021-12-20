import os
import glob
import shutil

os.mkdir("mot17_with_siam")

for file in os.listdir("mot17_train"):   
    if file.startswith("."):
        continue
    print(file, end="\n")
    os.mkdir("mot17_with_siam/" + file)
    os.mkdir("mot17_with_siam/" + file + "/siammot")
    os.mkdir("mot17_with_siam/" + file + "/det")
    os.mkdir("mot17_with_siam/" + file + "/gt")
    os.mkdir("mot17_with_siam/" + file + "/img1")
    shutil.copy("siammot_results/" + file + ".json", "mot17_with_siam/" + file + "/siammot/")
    shutil.copy("mot17_train/" + file + "/det/det.txt", "mot17_with_siam/" + file + "/det/")
    shutil.copy("mot17_train/" + file + "/gt/gt.txt", "mot17_with_siam/" + file + "/gt/")
    for jpgfile in glob.glob("mot17_train/" + file + "/img1/*.jpg"):
        shutil.copy(jpgfile, "mot17_with_siam/" + file + "/img1")
