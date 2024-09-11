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
