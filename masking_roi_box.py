import numpy as np
import cv2
import sys

image = cv2.imread("roi_box_source.jpg")
height, width, channel = image.shape
with open('guide_map.txt', 'r') as f:
    guide_lines = f.readlines()

point_count = 18
div_factor = point_count + 1
step_width = int(width/div_factor)
step_height = int(height/div_factor)
guide_map = np.zeros((point_count, point_count), dtype=int)
for y, guide_line in enumerate(guide_lines):
    if y == point_count:
        break
    guide_line = guide_line.strip()
    guide_line_elems = guide_line.split('\t')
    for x, elem in enumerate(guide_line_elems):
        guide_map[y, x] = int(elem)

# TOP
mask_top_y, mask_bot_y, mask_left_x, mask_right_x = -1,-1,-1,-1
top_count, bot_count, left_count, right_count = 0, 0, 0, 0
for y in range(point_count):
    if 1 in guide_map[y]:
        break
    if -1 in guide_map[y]:
        break
    mask_top_y = y

for y in range(point_count-1, -1, -1):
    if 1 in guide_map[y]:
        break
    if -1 in guide_map[y]:
        break
    mask_bot_y = y

for x in range(point_count):  
    y_elems = [row[x] for row in guide_map]  
    if 1 in y_elems:
        break
    if -1 in y_elems:
        break
    mask_left_x = x

for x in range(point_count-1, -1, -1):
    y_elements = [row[x] for row in guide_map]  
    if 1 in y_elements:
        break
    if -1 in y_elements:
        break
    mask_right_x = x

top_count = mask_top_y + 1
bot_count = point_count - mask_bot_y
left_count = mask_left_x + 1
right_count = point_count - mask_right_x

print(f"top count : {top_count}, bot count : {bot_count}, left count : {left_count}, right count : {right_count}")

left_bound = step_width * left_count
right_bound = width - (step_width * right_count)
top_bound = step_height * top_count
bot_bound = height - (step_height * bot_count)

left_mask = np.zeros((height, step_width*left_count), dtype=int)
right_mask = np.zeros((height, step_width*right_count), dtype=int)
top_mask = np.zeros((step_height*top_count, width), dtype=int)
bot_mask = np.zeros((step_height*bot_count, width), dtype=int)

left_mask = np.expand_dims(left_mask, axis=-1)
right_mask = np.expand_dims(right_mask, axis=-1)
top_mask = np.expand_dims(top_mask, axis=-1)
bot_mask = np.expand_dims(bot_mask, axis=-1)
image[:top_bound, :] = top_mask
image[bot_bound:, :] = bot_mask
image[:,:left_bound] = left_mask
image[:,right_bound:] = right_mask

cv2.imwrite("roi_box_result.jpg", image)
