from io import BytesIO
from os.path import join
from PIL import Image

from file_manager import get_file_name

RESULTS_DIR = '../test_files/processed_images/'


def open_as_bytes(file_path):
    with open(file_path, 'rb') as f:
        img = Image.open(f)
        byte_io = BytesIO()
        img.save(byte_io, 'PNG')
        byte_io.seek(0)
    return Image.open(byte_io)


def save_image(image, file_path):
    filename, ext = get_file_name(file_path)
    image.save(join(RESULTS_DIR, '{filename}.thumbnail{ext}').format(filename=filename, ext=ext), "JPEG", dpi=[75, 75],
               quality=50, optimize=True)
