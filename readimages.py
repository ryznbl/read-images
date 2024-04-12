import os
import pytesseract
from PIL import Image

folder_path = 'images/'
output_file = 'output.txt'
output_path = os.path.join(folder_path, output_file)
count = 0

with open(output_path, 'w') as f:
    for filename in os.listdir(folder_path):
        image_path = os.path.join(folder_path, filename)
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        f.write(str(count) + ': ' + text + '\n')
        count = count + 1

print("All text extracted and saved to", output_file)