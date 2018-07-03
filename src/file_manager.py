from glob import iglob
from itertools import chain
from os.path import splitext, join, split

IMAGES_DIR = '../test_files/source_images/'
IMAGE_TYPES = ['jpg', 'png']  # Consider too  'jpeg', 'bmp', 'gif'


def search_path(ext, source_dir=IMAGES_DIR):
    return join(source_dir, '*.{ext}'.format(ext=ext))


def files_path(extensions=IMAGE_TYPES, **kwargs):
    return (iglob(search_path(extension, **kwargs)) for extension in extensions)


def get_images_list(**kwargs):
    return chain.from_iterable(files_path(**kwargs))


def file_splitext(infile):
    return splitext(infile)


def get_file_name(file):
    file_path, ext = file_splitext(file)
    return split(file)[-1], ext
