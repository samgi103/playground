# import cv2
# mask_raw = cv2.imread("C:/nerf/skull/guide_mask_images/mask_raw/000.png")
# mask = cv2.imread("C:/nerf/skull/guide_mask_images/mask/000.png")

# print(mask_raw.shape)
# print(mask.shape)

import os

def find_yaml_files(directory='.'):
    yaml_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.yml'):
                yaml_files.append(os.path.join(root, file))
    return yaml_files

# 현재 작업 디렉토리에서 .yml 파일 찾기
yaml_files = find_yaml_files("C:/nerf/skull")

# 결과 출력
for yaml_file in yaml_files:
    print(yaml_file)