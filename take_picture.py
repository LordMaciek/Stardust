import subprocess
import os
import datetime
import time

dirName = "pictures_" + datetime.date
os.mkdir(dirName)
os.chdir(dirName)
# camList = subprocess.run(["gphoto2", "--auto-detect"])
# print(camList)
#
# camSets = subprocess.run(["gphoto2", "--port", "usb:", "--abilities"])
# print(camSets)

def takePic():
    numpix = input("How many pictures would you like to take?")
    for i in range(numpix):
        filname = "pix_" + i
        subprocess.run(["gphoto2", "-capture-image-and-download", "--filename=", filname])
        time.sleep(5)