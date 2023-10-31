from PIL import Image
import time
import sys

Image.MAX_IMAGE_PIXELS = None


def display_loading():
    animation = "|/-\\"
    start_time = time.time()
    while True:
        for i in range(2):
            time.sleep(0.2)  # Feel free to experiment with the speed here
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        if time.time() - start_time > 1:  # The animation will last for 10 seconds
            break
    sys.stdout.write("\rDone!")


def image_convertor(path: str):
    display_loading()
    try:
        current_image = Image.open(path)
        new_image = current_image.convert('RGB')
        return new_image
    except FileNotFoundError:
        print('The given path is wrong')
    except ValueError:
        print('unknown file extension')


def conversion(fmt: str, path: str, quality: int, size: int):
    thumbnail_size = size, size
    output_path = 'convertor.' + fmt
    image = image_convertor(path)
    if size:
        image.thumbnail(thumbnail_size, Image.LANCZOS)

    try:
        image.save(output_path, fmt, subsampling=0, quality=quality)
    except Exception as err:
        print(err)

    print(f'convert to {output_path} successfully!')
