import os
from PIL import Image

print('Will now proceed with stacking pictures from the \'cropped\' directory...')
def main():
    try:
        os.chdir('cropped')
        images = os.listdir()
        num_images = len(images)

        red_data = []
        green_data = []
        blue_data = []
        for img_num, image in enumerate(images, start=1):
            print('Working on image {}/{}...{}'.format(img_num, num_images, image))
            with Image.open(image) as img:
                if img_num == 1:
                    img_size = img.size
                    print('Got the baseline imagesize, it\'s {}.'.format(img_size))
                red_data.append(list(img.getdata(0)))
                green_data.append(list(img.getdata(1)))
                blue_data.append(list(img.getdata(2)))

        ave_red = [round(sum(x) / len(red_data)) for x in zip(*red_data)]
        ave_green = [round(sum(x) / len(green_data)) for x in zip(*green_data)]
        ave_blue = [round(sum(x) / len(red_data)) for x in zip(*blue_data)]

        merged_data = [(x) for x in zip(ave_red, ave_green, ave_blue)]
        stacked = Image.new('RGB', (img_size))
        stacked.putdata(merged_data)
        stacked.show()

        os.chdir('..')
        os.chdir('pix_ready')
        stacked.save('stacked_img.tif', 'TIFF')
    except:
        print("No pix to crop! Make sure you've followed the order of actions I've had in mind while coding this...")

if __name__ == '__main__':
    main()