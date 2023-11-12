import os
import cv2
import numpy as np

def get_png_files(folder_path):
    png_files = []
    for file in os.listdir(folder_path):
        if file.lower().endswith(".png"):
            png_files.append(os.path.join(folder_path, file))
    return png_files

def get_file_name(file_path):
    return os.path.basename(file_path)

image_folder = "C:/nerf/skull/masked_images/image/"
mask_folder = "C:/nerf/skull/masked_images/mask/"
result_folder = "C:/nerf/skull/masked_images/result/"
image_path_list = get_png_files(image_folder)
mask_path_list = get_png_files(mask_folder)

for image_path in image_path_list:
    image_name = get_file_name(image_path)
    mask_name = f"{str(int(image_name.split('.')[0])).zfill(3)}.png"
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_folder + mask_name, cv2.IMREAD_GRAYSCALE)
    masked_image = cv2.bitwise_and(image, image, mask=mask)
    cv2.imwrite(f"{result_folder}{image_name}", masked_image)
