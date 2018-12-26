import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.

# load the image, create the mirrored image, and the result placeholder
img    = Image.open('test.jpg')
mirror = img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90)
sz     = max(img.size + mirror.size)
result = Image.new(img.mode, (sz,sz))
result.paste(img, (0,0)+img.size)

# now paste the mirrored image, but with a triangular binary mask
mask = Image.new('1', mirror.size)
draw = ImageDraw.Draw(mask)
draw.polygon([0,0,0,sz,sz,sz], outline='white', fill='white')
result.paste(mirror, (0,0)+mirror.size, mask)

# clean up and save the result
del mirror, mask, draw
result.save('result.jpg')


def rotate(image_path, degrees_to_rotate, saved_location):
    image_obj = Image.open(image_path)
    rotated_image = image_obj.rotate(degrees_to_rotate)
    rotated_image.save(saved_location)
    rotated_image.show()

image = Image.open('test.jpg')
image = 'test.jpg'
rotate(image, 90, 'rotated_mantis.jpg')


def flip_image(image_path, saved_location):
    image_obj = Image.open(image_path)
    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    rotated_image.save(saved_location)
    rotated_image.show()

image = 'flipped_2_mantis.jpg'
flip_image(image, 'test_2.jpg')

rotate(image, 10, 'rotated_10.jpg')

import Image, ImageOps
img = Image.open('rotated_5.jpg')
img_with_border = ImageOps.expand(img,border=300,fill='black')
img_with_border.save('imaged-with-border.jpg')


