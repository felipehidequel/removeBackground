from rembg import remove
from PIL import Image

i = 1
input_path = './input/bner.jpg'
output_path = './output/bner.png'

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)