from PIL import Image

image_path = 'images/tower.bmp'

image = Image.open(image_path)

image.show()

image.save('archivo.bmp')
