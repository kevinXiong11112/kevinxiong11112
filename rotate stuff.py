import cv2
import numpy as np
import os

def rotate_image(image, angle):
    """Rotate the image by the given angle."""
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h), flags=cv2.INTER_CUBIC)
    return rotated_image

def generate_rotated_templates(template_folder, output_folder,  angles=range(0, 360, 90)):
    """Generate rotated versions of all templates in the template folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    templates = [f for f in os.listdir(template_folder) if f.endswith('.png')]
    for template_file in templates:
        template_path = os.path.join(template_folder, template_file)
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        
        if template is None:
            print(f"Error: Failed to load template from {template_path}")
            continue
        
        for angle in angles:
            rotated_template = rotate_image(template, angle)
            rotated_template_path = os.path.join(output_folder, f'{os.path.splitext(template_file)[0]}_{angle}.png')
            cv2.imwrite(rotated_template_path, rotated_template)
            print(f"Saved rotated template to {rotated_template_path}")

# Example usage
template_folder = r"C:\Users\engik\.vscode\templates"
output_folder = r"C:\Users\engik\.vscode\templates"
generate_rotated_templates(template_folder, output_folder)
