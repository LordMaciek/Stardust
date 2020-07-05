import crop_scale
import stack
import take_picture
import serve
"""This wee app is designed specifically for astrophotography. Taking repeated pix, cropping, stacking and - in the
futur - sharpening. Finally, it should run a simple server showing you your creation"""
def main():
    with open("welcome.txt", "r") as f:
        WELCOME = f.read()

    with open("prompt.txt", "r") as f:
        MENU_PROMPT = f.read()

    print(WELCOME)
    input(MENU_PROMPT)
    take_picture.main()
    crop_scale.main()
    # stack()
    serve.main()
if __name__ == '__main__':
    main()