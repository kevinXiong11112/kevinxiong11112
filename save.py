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
    
    shape_names = [os.path.basename(t).split('.')[0] for t in templates] 
    coordinates_matrix = [['' for _ in range(8)] for _ in range(8)]  
    
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
                
                row = center_y // (image.shape[0] // 8) 
                col = center_x // (image.shape[1] // 8)  
                
                if 0 <= row < 8 and 0 <= col < 8:
                    coordinates_matrix[row][col] = shape_name
            
            scale_factor -= 0.1

    return coordinates_matrix

    


####!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def swap_and_check(board):
    matches=[]
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if(c<5):
                if(col==board[r][c+2]==board[r][c+3]):
                    matches.append([[r,c],[r,c+1]])
            if(r>0 and r<7 and c<7):
                if(col==board[r+1][c+1]==board[r-1][c+1]):
                    matches.append([[r,c],[r,c+1]])
            if(r<6 and c<7):
                if(col==board[r+1][c+1]==board[r+2][c+1]):
                    matches.append([[r,c],[r,c+1]])

            if(r>1 and c<7):
                if(col==board[r-1][c+1]==board[r-2][c+1]):
                    matches.append([[r,c],[r,c+1]])
            
            if(c>2):
                if(col==board[r][c-2]==board[r][c-3]):
                    matches.append([[r,c],[r,c-1]])
            if(r>0 and r<7 and c>0):
                if(col==board[r+1][c-1]==board[r-1][c-1]):
                    matches.append([[r,c],[r,c-1]])
            if(r<6 and c>0):
                if(col==board[r+1][c-1]==board[r+2][c-1]):
                    matches.append([[r,c],[r,c-1]])
            if(r>1 and c>0):
                if(col==board[r-1][c-1]==board[r-2][c-1]):
                    matches.append([[r,c],[r,c-1]])
                
            if(r<5):
                if(col==board[r+2][c]==board[r+3][c]):
                    matches.append([[r,c],[r+1,c]])
            if(c>0 and c<7 and r<7):
                if(col==board[r+1][c-1]==board[r+1][c+1]):
                    matches.append([[r,c],[r+1,c]])
            if(c>1 and r<7):
                if(col==board[r+1][c-1]==board[r+1][c-2]):
                    matches.append([[r,c],[r+1,c]])
            if(c<6 and r<7):
                if(col==board[r+1][c+1]==board[r+1][c+2]):
                    matches.append([[r,c],[r+1,c]])

            if(r>2):
                if(col==board[r-2][c]==board[r-3][c]):
                    matches.append([[r,c],[r-1,c]])
            if(c>0 and c<7 and r>0):
                if(col==board[r-1][c-1]==board[r-1][c+1]):
                    matches.append([[r,c],[r-1,c]])
            if(c>1 and r>0):
                if(col==board[r-1][c-1]==board[r-1][c-2]):
                    matches.append([[r,c],[r-1,c]])
            if(c<6 and r>0):
                if(col==board[r-1][c+1]==board[r-1][c+2]):
                    matches.append([[r,c],[r-1,c]])
    return matches
################!!!!!!!!!!!!!!!!!!!!!



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
    time.sleep(0.01)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def click_at_position(x, y):
    """Move the mouse to a specified position and click."""
    move_to_position(x, y)
    time.sleep(0.1) 
    click()

def empty4wayfunction(board):
    emptylist=[]
    for row_index, row in enumerate(board):
        for col_index, value in enumerate(row):
            if value == '':
                emptylist.append([row_index, col_index])
    if(emptylist==[]):
        return [] 
    else:
        return emptylist


def main_loop():
    folder_path = r"C:\Users\engik\.vscode"
    template_folder = r"C:\Users\engik\Downloads\template"
    while True:
        screenshot_path = capture_screenshot(folder_path)
        board = process_image(screenshot_path, template_folder)
        valid_moves=swap_and_check(board) 
        empty4way=empty4wayfunction(board)
        

        if(len(valid_moves)>0 and len(valid_moves)<664):
            one=valid_moves[-1][0]
            two=valid_moves[-1][1]
            tile_position_1 = (530 + (120 * one[1]), 145 + (120 * one[0])) 
            tile_position_2 = (530 + (120 * two[1]), 145 + (120 * two[0]))  
            click_at_position(tile_position_1[0], tile_position_1[1])
            click_at_position(tile_position_2[0], tile_position_2[1])
            time.sleep(2)  # Add a delay to ensure the swap is registered
            break 
        
        elif(len(empty4way)==64):
            click_at_position(1550,750)
        else:
            for i,eloc in enumerate(empty4way):
                tile_position_1 = (530 + (120 * eloc[1]), 145 + (120 *eloc[0])) 
                if(eloc[1]>0):
                    tile_position_2 = (530 + (120 * eloc[1])-120, 145 + (120 * eloc[0]))  
                    click_at_position(tile_position_1[0], tile_position_1[1])
                    click_at_position(tile_position_2[0], tile_position_2[1])
                    time.sleep(2)  
                if(eloc[1]<7):
                    tile_position_2 = (530 + (120 * eloc[1])+120, 145 + (120 * eloc[0]))  
                    click_at_position(tile_position_1[0], tile_position_1[1])
                    click_at_position(tile_position_2[0], tile_position_2[1])
                    time.sleep(2) 
                if(eloc[0]>0):
                    tile_position_2 = (530 + (120 * eloc[1]), 145 + (120 * eloc[0])-120)  
                    click_at_position(tile_position_1[0], tile_position_1[1])
                    click_at_position(tile_position_2[0], tile_position_2[1])
                    time.sleep(2) 
                if(eloc[0]<7):
                    tile_position_2 = (530 + (120 * eloc[1]), 145 + (120 * eloc[0])+120)  
                    click_at_position(tile_position_1[0], tile_position_1[1])
                    click_at_position(tile_position_2[0], tile_position_2[1])
                    time.sleep(2) 
                if(eloc[0]>1):
                    tile_position_1 = (530 + (120 * eloc[1])-120, 145 + (120 * eloc[0]))  
                    tile_position_2 = (530 + (120 * eloc[1]-240), 145 + (120 *eloc[0])) 
                    click_at_position(tile_position_1[0], tile_position_1[1])
                    click_at_position(tile_position_2[0], tile_position_2[1])
                    time.sleep(2) 
                if(eloc[0]<6):
                    tile_position_1 = (530 + (120 * eloc[1])+120, 145 + (120 * eloc[0]))  
                    tile_position_2 = (530 + (120 * eloc[1]+240), 145 + (120 *eloc[0])) 
                    click_at_position(tile_position_1[0], tile_position_1[1])
                    click_at_position(tile_position_2[0], tile_position_2[1])
                    time.sleep(2) 
                if(eloc[1]>1):
                    tile_position_1 = (530 + (120 * eloc[1]), 145 + (120 * eloc[0])-120)  
                    tile_position_2 = (530 + (120 * eloc[1]), 145 + (120 *eloc[0])-240) 
                    click_at_position(tile_position_1[0], tile_position_1[1])
                    click_at_position(tile_position_2[0], tile_position_2[1])
                    time.sleep(2) 
                if(eloc[1]<6):
                    tile_position_1 = (530 + (120 * eloc[1]), 145 + (120 * eloc[0])+120)  
                    tile_position_2 = (530 + (120 * eloc[1]), 145 + (120 *eloc[0])+240) 
                    click_at_position(tile_position_1[0], tile_position_1[1])
                    click_at_position(tile_position_2[0], tile_position_2[1])
                    time.sleep(2) 
            

if __name__ == "__main__":
    while True:
        main_loop()
