import os
import cv2
import pyautogui
import numpy as np
from datetime import datetime
import time
import keyboard


def capture_screenshot(folder_path, count=15, interval=1):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)
    
    for i in range(count):
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_path = os.path.join(folder_path, f'screenshot_{timestamp}.png')
        
        cv2.imwrite(file_path, screenshot)
        print(f'Screenshot saved to {file_path}')
        
        time.sleep(interval)

time.sleep(5)
capture_screenshot(r'C:\Users\engik\.vscode\ap', count=5, interval=2)




def type_paragraph(paragraph):
    time.sleep(15)  
    
    keyboard.write(paragraph)

paragraph = """这是一个示例段落，将被自动输入。
它可以跨越多行并包含标点符号。您可以根据需要调整键入速度。"""

type_paragraph(paragraph)
