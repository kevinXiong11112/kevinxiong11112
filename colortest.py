
    # screenshot_path = capture_screenshot(folder_path)
    # is_present = process_image(screenshot_path, template_path)

    # if(is_present):
    #     #loomians
    #     hold_key('d', hold_duration)
    #     hold_key(Key.enter, hold_duration)
    #     time.sleep(2) 
    #     #switch
    #     click_at_position(700,450)
    #     click_at_position(800,550)
    #     time.sleep(15) 
    #     #fight spare
    #     hold_key('w', hold_duration)
    #     hold_key(Key.enter, hold_duration)
    #     hold_key('d', hold_duration)
    #     hold_key(Key.enter, hold_duration)
    #     time.sleep(10)
    #     #catch 20
    #     for i in range(30):
    #         hold_key('d', hold_duration)
    #         hold_key('a', hold_duration)
    #         hold_key(Key.enter, hold_duration)
    #         time.sleep(2)
    #         click_at_position(625,325)
    #         click_at_position(630,325)
    #         time.sleep(2)
    #         click_at_position(830,780)
    #         click_at_position(840,780)
    #         time.sleep(20)        
    #         screenshot_path = capture_screenshot(folder_path)
    #         no=r'C:\Users\engik\.vscode\no.png'
    #         nopresent = process_image(screenshot_path, no)
    #         if(nopresent):
    #             click_at_position(1450,720)
    #             click_at_position(1460,720)
    #             time.sleep(4)
    #             i=19
    #             break

    # elif (is_color_in_image(screenshot_path,  (105,47,129) ) and is_color_in_image(screenshot_path, (132,61,165)) and is_color_in_image(screenshot_path,(131,79,204))):
    #     hold_key('s', hold_duration)
    #     hold_key('w', hold_duration)
    #     hold_key(Key.enter, hold_duration)
    #     hold_key('d', hold_duration)
    #     hold_key('a', hold_duration)
    #     hold_key(Key.enter, hold_duration)
    #     time.sleep(10)
    # else:
    #     click_at_position(1200, 1000)
    #     click_at_position(1210, 1000)
    #     time.sleep(4)






# def calculate_histogram(image, mask):
#     hist = cv2.calcHist([image], [0, 1, 2], mask, [8, 8, 8], [0, 256, 0, 256, 0, 256])
#     cv2.normalize(hist, hist)
#     return hist

# def match_shapes_and_colors(ref_image, target_image):
#     # Convert to grayscale for contour detection
#     gray_ref = cv2.cvtColor(ref_image, cv2.COLOR_BGR2GRAY)
#     gray_target = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

#     # Find contours
#     contours_ref, _ = cv2.findContours(gray_ref, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     contours_target, _ = cv2.findContours(gray_target, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     for cnt_ref in contours_ref:
#         # Create mask for the reference contour
#         mask_ref = np.zeros(gray_ref.shape, dtype=np.uint8)
#         cv2.drawContours(mask_ref, [cnt_ref], -1, 255, -1)
        
#         # Calculate histogram for the reference shape
#         hist_ref = calculate_histogram(ref_image, mask_ref)

#         for cnt_target in contours_target:
#             # Create mask for the target contour
#             mask_target = np.zeros(gray_target.shape, dtype=np.uint8)
#             cv2.drawContours(mask_target, [cnt_target], -1, 255, -1)
            
#             # Calculate histogram for the target shape
#             hist_target = calculate_histogram(target_image, mask_target)

#             # Match shapes
#             shape_score = cv2.matchShapes(cnt_ref, cnt_target, cv2.CONTOURS_MATCH_I1, 0.0)
#             # Compare histograms (use Bhattacharyya distance)
#             color_score = cv2.compareHist(hist_ref, hist_target, cv2.HISTCMP_BHATTACHARYYA)

#             # Combine scores
#             final_score = (shape_score + color_score) / 2  # Adjust weights as needed
            
#             # Determine match based on final score
#             if final_score < 0.7:  # Set your threshold here
#                 print("Match found!")

# # Example usage
# ref_image = cv2.imread('reference.png')
# target_image = cv2.imread('target.png')
# match_shapes_and_colors(ref_image, target_image)
