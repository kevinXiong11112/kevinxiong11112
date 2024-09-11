from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def hold_key(key, duration):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)

hold_duration = 2  # Adjust hold duration as needed

for _ in range(2):
    hold_key('w', hold_duration)
    hold_key('s', hold_duration)
