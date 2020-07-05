import subprocess
import os
from datetime import date, time


def main():
    dirName = "pictures_" + str(date.today())
    os.mkdir(dirName)
    os.chdir(dirName)
    takePic()


def takePic():
    numpix = input("How many pictures would you like to take? ")
    numpix = int(numpix)
    for i in range(numpix):
        filname = "--filename=pix_" + str(i)
        subprocess.run(["gphoto2", "--capture-image-and-download", filname])

if __name__ == __main__:
    main()