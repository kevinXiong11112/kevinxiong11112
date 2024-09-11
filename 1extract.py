import easyocr
from PIL import Image
import pyautogui
import numpy as np
import time
import os
import cv2
from datetime import datetime
import keyboard
from pynput.keyboard import Controller


def load_image(image_path):
    image = Image.open(image_path)
    return image

def capture_screenshot(folder_path, region, count, interval):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)
    
    file_paths = []
    
    for i in range(count):
        screenshot = pyautogui.screenshot(region=region)
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_path = os.path.join(folder_path, f'3screenshot_{timestamp}.png')
        
        cv2.imwrite(file_path, screenshot)
        file_paths.append(file_path)
        print(f'Screenshot saved to {file_path}')
        
        time.sleep(interval)
    
    return file_paths

def extract_text_from_image(image):
    image_np = np.array(image)
    reader = easyocr.Reader(['en']) 
    results = reader.readtext(image_np)
    text = ' '.join([result[1] for result in results])
    return text

keyboard = Controller()
def type_paragraph(paragraph):
    for char in paragraph:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.1)


left = 0
top = 100
width = pyautogui.size().width
height = pyautogui.size().height - top
region = (left, top, width, height)

# time.sleep(6)
# while True:
#     type_paragraph("""aaaaaaa""")
#     file_paths = capture_screenshot(r'C:\Users\engik\.vscode\ap', region, 1, 0)
#     time.sleep(30)

time.sleep(6)
while True:
    file_paths = capture_screenshot(r'C:\Users\engik\.vscode\ap', region, 1, 0)
    type_paragraph("apple is a")
    time.sleep(1)





import ctypes
import time

# Define necessary constants
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_KEYDOWN = 0x0000

# Define the key code for 'a'
VK_A = 0x41

def press_key(key_code):
    # Create a keyboard event for key press
    ctypes.windll.user32.SendMessageW(0xFFFF, 0x0100, key_code, 0)
    time.sleep(0.05)  # Small delay to simulate real key press duration
    ctypes.windll.user32.SendMessageW(0xFFFF, 0x0101, key_code, 0)  # Key release

# Simulate pressing 'a'
press_key(VK_A)
