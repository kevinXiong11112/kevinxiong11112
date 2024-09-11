import cv2
import numpy as np

def is_color_in_image(image_path, target_color):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    target_color = np.array(target_color)
    color_exists = np.any(np.all(image_rgb == target_color, axis=-1))
    return color_exists

image_path = r'C:\Users\engik\.vscode\shard.png'
target_color = (105,47,129) 
if True:
    print("The color exists in the image.")
    print(is_color_in_image(image_path, target_color), is_color_in_image(image_path,(131,79,204)),is_color_in_image(image_path,(132,61,165)))
else:
    print("The color does not exist in the image.")
