from file_manager import get_images_list
from image_files import open_as_bytes, save_image
from image_processing import create_thumbnail, add_watermark


def run():
    for infile in get_images_list():
        print(infile)
        image = open_as_bytes(infile)
        create_thumbnail(image)
        add_watermark(image, 'Lienzos y arte')
        save_image(image, infile)


if __name__ == '__main__':
    run()
