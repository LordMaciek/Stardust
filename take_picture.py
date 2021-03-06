import subprocess
import os
from datetime import date, time

with open("folder_exitst.txt", "r") as f:
    FOLDER_EXISTS = f.read()

with open("pic_error.txt", "r") as f:
    PIC_ERROR = f.read()

def main():
    dirName = "pictures_" + str(date.today())
    if os.path.exists(dirName):
        dirName = input(FOLDER_EXISTS.format(dirName)) + "_" + str(date.today())
    os.mkdir(dirName)
    os.chdir(dirName)
    try:
        takePic()
    except:
        print(PIC_ERROR)
    finally:
        with open("whereabouts", "w") as f:
            f.write(dirName)


def takePic():
    numpix = input("How many pictures would you like to take? ")
    numpix = int(numpix)
    for i in range(numpix):
        filname = "--filename=pix_" + str(i)
        subprocess.run(["gphoto2", "--capture-image-and-download", filname])

if __name__ == '__main__':
    main()