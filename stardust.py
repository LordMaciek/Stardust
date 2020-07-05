import crop_scale
import stack
import take_picture

def main():
    take_picture.main()
    crop_scale.main()
    stack()

if __name__ == '__main__':
    main()