import pyautogui
import cv2
import numpy as np
import os
import time
import ctypes
from pynput.keyboard import Key, Controller
from datetime import datetime



def capture_screenshot(folder_path):
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Generate a timestamp for the filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_path = os.path.join(folder_path, f'screenshot_{timestamp}.png')
    
    cv2.imwrite(file_path, screenshot)
    return file_path

def process_image(file_path, template_path):
    image = cv2.imread(file_path)
    if image is None:
        print(f"Error: Failed to load image from {file_path}")
        return False
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        print(f"Error: Failed to load template from {template_path}")
        return False
    
    w, h = template.shape[::-1]
    scale_factor = 1.0
    found = False
    
    while scale_factor > 0.5:
        resized_template = cv2.resize(template, None, fx=scale_factor, fy=scale_factor)
        res = cv2.matchTemplate(gray, resized_template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        loc = np.where(res >= threshold)
        
        if len(loc[0]) > 0: 
            found = True
            for pt in zip(*loc[::-1]):
                top_left = (pt[0], pt[1])
                bottom_right = (pt[0] + int(w * scale_factor), pt[1] + int(h * scale_factor))
                cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        
        if found:
            break 
        scale_factor -= 0.1

    return found


MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_ABSOLUTE = 0x8000
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

screen_width = ctypes.windll.user32.GetSystemMetrics(0)
screen_height = ctypes.windll.user32.GetSystemMetrics(1)

def move_to_position(x, y, duration=0.1):
    """Smoothly move the mouse to a specified position."""
    current_x, current_y = pyautogui.position()
    steps = max(1, int(duration * 100))  
    step_delay = duration / steps
    delta_x = (x - current_x) / steps
    delta_y = (y - current_y) / steps
    
    for _ in range(steps):
        current_x += delta_x
        current_y += delta_y
        abs_x = int(current_x * 65535 / screen_width)
        abs_y = int(current_y * 65535 / screen_height)
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE, abs_x, abs_y, 0, 0)
        time.sleep(step_delay)

def click():
    """Simulate a mouse click."""
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def click_at_position(x, y):
    """Move the mouse to a specified position and click."""
    move_to_position(x, y)
    click()


keyboard = Controller()
def hold_key(key, duration):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)

def is_color_in_image(image_path, target_color):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    target_color = np.array(target_color)
    color_exists = np.any(np.all(image_rgb == target_color, axis=-1))
    return color_exists



folder_path = r"C:\Users\engik\.vscode"
template_path = r'C:\Users\engik\.vscode\duskit.png'
template_pathm= r'C:\Users\engik\.vscode\dicro.png'
target_color = (105,47,129) 
micro=False
target=False
color=False
time.sleep(0)
click()

while True:
    hold_duration = 0.5

    for _ in range(30):
        keyboard.press('w')
        time.sleep(2) #
        screenshot_path = capture_screenshot(folder_path)
        is_present = process_image(screenshot_path, template_path)
        print("aaaa")
        keyboard.release('w')
        keyboard.press('s')
        is_presentm=process_image(screenshot_path, template_pathm)
        keyboard.release('s')
        keyboard.press('w')
        if(is_presentm and is_present==False and (is_color_in_image(screenshot_path,(105,47,129))==False and is_color_in_image(screenshot_path, (132,61,165))==False and is_color_in_image(screenshot_path,(131,79,204)==False))):
            micro=True
            keyboard.release('w')
            break
        if(is_present):
            target=True
            keyboard.release('w')
            break
        if (is_color_in_image(screenshot_path,  (105,47,129) ) and is_color_in_image(screenshot_path, (132,61,165)) and is_color_in_image(screenshot_path,(131,79,204))):
            color=True
            keyboard.release('w')
            break

    if(micro):
        click_at_position(1200, 1000)
        click_at_position(1210, 1000)
        time.sleep(4)
        continue
    elif(target):
        #loomians
        hold_key('d', hold_duration)
        hold_key(Key.enter, hold_duration)
        time.sleep(2) 
        #switch
        click_at_position(700,450)
        click_at_position(800,550)
        time.sleep(15) 
        #fight spare
        hold_key('w', hold_duration)
        hold_key(Key.enter, hold_duration)
        hold_key('d', hold_duration)
        hold_key(Key.enter, hold_duration)
        time.sleep(10)
        #catch 20
        for i in range(30):
            hold_key('d', hold_duration)
            hold_key('a', hold_duration)
            hold_key(Key.enter, hold_duration)
            time.sleep(2)
            click_at_position(625,325)
            click_at_position(630,325)
            time.sleep(2)
            click_at_position(830,780)
            click_at_position(840,780)
            time.sleep(20)        
            screenshot_path = capture_screenshot(folder_path)
            no=r'C:\Users\engik\.vscode\no.png'
            nopresent = process_image(screenshot_path, no)
            if(nopresent):
                click_at_position(1450,720)
                click_at_position(1460,720)
                time.sleep(4)
                i=19
                break
        print("b")
        continue
    elif(color):
        hold_key('s', hold_duration)
        hold_key('w', hold_duration)
        hold_key(Key.enter, hold_duration)
        hold_key('d', hold_duration)
        hold_key('a', hold_duration)
        hold_key(Key.enter, hold_duration)
        time.sleep(10)
        print("p")
        continue
    
