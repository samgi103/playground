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

def convert_binary_mask_to_grayscale():
    mask_src_path = "C:/nerf/skull/guide_mask_images/mask_src/"
    mask_result_path = "C:/nerf/skull/guide_mask_images/mask/"
    # mask_filepath_list = get_png_files(mask_src_path)
    mask_filepath_list = get_png_files(mask_result_path)
    
    for mask_filepath in mask_filepath_list:
        binary_mask = cv2.imread(mask_filepath, cv2.IMREAD_UNCHANGED)
        print(binary_mask.shape)
        break
        # binary_mask = binary_mask[:,:,np.newaxis]
        # cv2.imwrite(mask_result_path + get_file_name(mask_filepath), binary_mask)
        # cv2.imwrite(mask_filepath, binary_mask)

        
convert_binary_mask_to_grayscale()