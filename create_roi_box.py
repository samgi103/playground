import numpy as np
import cv2

# 이미지 크기 설정
width, height = 1920, 1080

# 모든 픽셀을 1로 채운 NumPy 배열 생성
image = np.ones((height, width, 3), dtype=np.uint8) * 255  # 255는 흰색을 나타냅니다.

point_count = 18

div_factor = point_count + 1

step_height = int(height/div_factor)
step_width = int(width/div_factor)

point_color = (0, 255, 0)
for y in range(step_height, height-step_height, step_height):
    for x in range(step_width, width-step_width, step_width):
        point_position = (x, y)
        cv2.circle(image, point_position, 5, point_color, -1)

cv2.imwrite("roi_box_source.jpg", image)

with open("point_map.txt", 'w') as file:
    for y in range(point_count):
        line = ""
        for x in range(point_count):
            line += "1"
            if x != point_count:
                line += "\t"
        file.write(line + "\n")