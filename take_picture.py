import subprocess
import os
from datetime import date, time

dirName = "pictures_" + str(date.today())
os.mkdir(dirName)
os.chdir(dirName)
# camList = subprocess.run(["gphoto2", "--auto-detect"])
# print(camList)
#
# camSets = subprocess.run(["gphoto2", "--port", "usb:", "--abilities"])
# print(camSets)

def takePic():
    numpix = input("How many pictures would you like to take?")
    numpix = int(numpix)
    for i in range(numpix):
        filname = "--filename=pix_" + str(i)
        subprocess.run(["gphoto2", "--capture-image-and-download", filname])

takePic()