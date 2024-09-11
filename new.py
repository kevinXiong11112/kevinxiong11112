import pyautogui
import cv2
import numpy as np
import os
import time

def capture_screenshot(folder_path):
    screenshot = pyautogui.screenshot(region=(470, 100, 980, 980))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    file_path = os.path.join(folder_path, 'screenshot.png')
    cv2.imwrite(file_path, screenshot)
    return file_path

def process_image(file_path, template_folder):
    image = cv2.imread(file_path)
    if image is None:
        print(f"Error: Failed to load image from {file_path}")
        return
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    templates = [os.path.join(template_folder, fname) for fname in os.listdir(template_folder) if fname.endswith('.png')]
    if not templates:
        print(f"Error: No templates found in {template_folder}")
        return
    
    match_found = False
    for template_path in templates:
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            print(f"Error: Failed to load template from {template_path}")
            continue
        w, h = template.shape[::-1]
        
        scale_factor = 1.0
        while scale_factor > 0.5:
            resized_image = cv2.resize(gray, None, fx=scale_factor, fy=scale_factor)
            res = cv2.matchTemplate(resized_image, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.9
            loc = np.where(res >= threshold)
            
            for pt in zip(*loc[::-1]):
                match_found = True
                # Adjust coordinates based on scaling
                top_left = (int(pt[0] / scale_factor), int(pt[1] / scale_factor))
                bottom_right = (int((pt[0] + w) / scale_factor), int((pt[1] + h) / scale_factor))
                
                # Calculate center coordinates
                center_x = (top_left[0] + bottom_right[0]) // 2
                center_y = (top_left[1] + bottom_right[1]) // 2
                
                # Draw rectangle and print coordinates
                cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
                print(f"Detected shape: Top left: {top_left}, Bottom right: {bottom_right}, Center: ({center_x}, {center_y})")
            
            scale_factor -= 0.1
        
    if not match_found:
        print("No matches found.")
    
    cv2.imshow('Detected Shapes', image)
    cv2.waitKey(0)  # Show the image until a key is pressed
    cv2.destroyAllWindows()

def main_loop():
    folder_path = r"C:\Users\engik\.vscode"
    template_folder = r"C:\Users\engik\.vscode\ball"
    
    while True:
        screenshot_path = capture_screenshot(folder_path)
        process_image(screenshot_path, template_folder)
        
        # Sleep for a specified amount of time to avoid overlap
        time.sleep(0.3)  # Adjust the sleep duration as needed

if __name__ == "__main__":
    main_loop()
