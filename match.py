import pyautogui
import cv2
import numpy as np
import os
import time
import ctypes

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
        return []
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    templates = [os.path.join(template_folder, fname) for fname in os.listdir(template_folder) if fname.endswith('.png')]
    if not templates:
        print(f"Error: No templates found in {template_folder}")
        return []
    
    match_found = False
    shape_names = [os.path.basename(t).split('.')[0] for t in templates]  # Get shape names from template filenames
    coordinates_matrix = [['' for _ in range(8)] for _ in range(8)]  # Initialize 8x8 matrix
    
    for template_path, shape_name in zip(templates, shape_names):
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            print(f"Error: Failed to load template from {template_path}")
            continue
        w, h = template.shape[::-1]
        
        scale_factor = 1.0
        while scale_factor > 0.5:
            resized_template = cv2.resize(template, None, fx=scale_factor, fy=scale_factor)
            res = cv2.matchTemplate(gray, resized_template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.9
            loc = np.where(res >= threshold)
            
            for pt in zip(*loc[::-1]):
                match_found = True
                top_left = (pt[0], pt[1])
                bottom_right = (pt[0] + int(w * scale_factor), pt[1] + int(h * scale_factor))
                
                center_x = (top_left[0] + bottom_right[0]) // 2
                center_y = (top_left[1] + bottom_right[1]) // 2
                cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
                
                # Calculate grid position
                row = center_y // (image.shape[0] // 8)  # Assuming image height is divided into 8 rows
                col = center_x // (image.shape[1] // 8)  # Assuming image width is divided into 8 columns
                
                if 0 <= row < 8 and 0 <= col < 8:
                    coordinates_matrix[row][col] = shape_name
            
            scale_factor -= 0.1
        
    if not match_found:
        print("No matches found.")
    
    return coordinates_matrix






def check_match(board):
    # Check for horizontal matches
    for r in range(len(board)):
        for c in range(len(board[0]) - 2):
            if board[r][c] == board[r][c + 1] == board[r][c + 2] and board[r][c] != 0:
                return True  # Match found

    # Check for vertical matches
    for r in range(len(board) - 2):
        for c in range(len(board[0])):
            if board[r][c] == board[r + 1][c] == board[r + 2][c] and board[r][c] != 0:
                return True  # Match found

    return False  # No match found

def find_one_possible_swap(board):
    rows = len(board)
    cols = len(board[0])

    for r in range(rows):
        for c in range(cols):
            # Check right swap
            if c < cols - 1 and board[r][c] != board[r][c + 1]:  # Ensure tiles are different
                # Swap tiles
                board[r][c], board[r][c + 1] = board[r][c + 1], board[r][c]
                if check_match(board):
                    return ((r, c), (r, c + 1))  # Return the swap positions
                # Swap back
                board[r][c], board[r][c + 1] = board[r][c + 1], board[r][c]

            # Check down swap
            if r < rows - 1 and board[r][c] != board[r + 1][c]:  # Ensure tiles are different
                # Swap tiles
                board[r][c], board[r + 1][c] = board[r + 1][c], board[r][c]
                if check_match(board):
                    return ((r, c), (r + 1, c))  # Return the swap positions
                # Swap back
                board[r][c], board[r + 1][c] = board[r + 1][c], board[r][c]

    return None  # No valid swap found


# Mouse event constants
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_ABSOLUTE = 0x8000
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

# Screen dimensions
screen_width = ctypes.windll.user32.GetSystemMetrics(0)
screen_height = ctypes.windll.user32.GetSystemMetrics(1)

def move_to_position(x, y, duration=0.1):
    """Smoothly move the mouse to a specified position."""
    current_x, current_y = pyautogui.position()
    steps = max(1, int(duration * 100))  # Calculate the number of steps based on duration
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
    time.sleep(0.01)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def click_at_position(x, y):
    """Move the mouse to a specified position and click."""
    move_to_position(x, y)
    time.sleep(0.1)  # Ensure there's a small delay before the click
    click()


def main_loop():
    folder_path = r"C:\Users\engik\.vscode"
    template_folder = r"C:\Users\engik\.vscode\template"
    
    while True:
        screenshot_path = capture_screenshot(folder_path)
        coordinates_matrix = process_image(screenshot_path, template_folder)
        if not coordinates_matrix:
            continue
        
        valid_swaps = find_one_possible_swap(coordinates_matrix)
        if valid_swaps:
            (tile_position_1, tile_position_2) = valid_swaps
            row1, col1 = tile_position_1    
            row2, col2 = tile_position_2
        
            tile_position_1 = (530 + (120 * col1), 145 + (120 * row1)) 
            tile_position_2 = (530 + (120 * col2), 145 + (120 * row2))  
            
            click_at_position(tile_position_1[0], tile_position_1[1])
            click_at_position(tile_position_2[0], tile_position_2[1])
            time.sleep(0.3)  # Add a delay to ensure the swap is registered
            break  # Exit the loop after a successful swap

if __name__ == "__main__":
    while True:
        main_loop()
