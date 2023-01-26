from rembg import remove
from PIL import Image
input_path = 'beach.jpg'
output_path = 'beach.png'
inp = Image.open(input_path)
output = remove(inp)
ouput.save(output_path)