from PIL import Image, ImageDraw, ImageFont


THUMBNAIL_WIDTH = 400, 1000


def create_thumbnail(image):
    image.thumbnail(THUMBNAIL_WIDTH)
    return image


def add_watermark(image, text='watermark'):
    width, height = image.size
    watermark = Image.new("RGBA", image.size)

    waterdraw = ImageDraw.ImageDraw(watermark, "RGBA")
    font = ImageFont.truetype("arial.ttf", 25)
    waterdraw.text((10, 10), text, font=font)
    waterdraw.text((width/2, height-30), text, font=font)
    watermask = watermark.convert("L").point(lambda x: min(x, 100))
    watermark.putalpha(watermask)

    image.paste(watermark, None, watermark)