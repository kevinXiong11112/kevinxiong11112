import pyautogui
import cv2
import numpy as np
import os
import time
import ctypes


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


click_x, click_y = 1450,720
time.sleep(3)  # Sleep for a few seconds    to switch to the window where you want to click
click_at_position(click_x, click_y)

