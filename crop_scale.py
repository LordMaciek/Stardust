import os
import shutil
from PIL import Image, ImageOps

"""This programme will prepare a serie of images for further processing,
by cropping them to only include the object of interest."""



def main():
    if os.path.exists('photos_raw'):
        raw_folder = get_raw_folder()
        del_folders('cropped')
        shutil.copytree(raw_folder, 'cropped')
        print("Cropping and scaling images")
        os.chdir('cropped')
        crop_imgs()
        clean_folder(prefix_to_save='cropped')
        print("Done cropping and scaling!\n")
    else:
        print("Somehow the pictures aren't there. You sure you started by taking pictures?")


def get_raw_folder():
    try:
        with open('whereabouts', "r") as f:
            raw_dir = f.read()
    except:
        print("There are no pictures, please start over.")

def del_folders(name):
    contents=os.listdir()
    for item in contents:
        if os.path.isdir(item) and item.startswith(name):
            shutil.rmtree(item)

def clean_folder(prefix_to_save):
    files=os.listdir()
    for file in files:
        if not file.startswith(prefix_to_save):
            os.remove(file)

def crop_imgs():
    files = os.listdir()
    for file_num, file in enumerate(files, start=1):
        with Image.open(file) as img:
            gray = img.convert('L')
            bw = gray.point(lambda x: 0 if x < 90 else 225)
            box = bw.getbbox()
            padded_box = (box[0]-20, box[1]-20, box[2]+20, box[3]+20)
            cropped = img.crop(padded_box)
            scaled = ImageOps.fit(cropped, (860, 860),
                                  Image.LANCZOS, 0, (0.5, 0.5))
            file_name = 'cropped{}.jpg'.format(file_num)
            scaled.save(file_name, 'JPEG')

if __name__ == '__main__':
    main()