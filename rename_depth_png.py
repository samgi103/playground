import os

def get_png_files(folder_path):
    png_files = []
    for file in os.listdir(folder_path):
        if file.lower().endswith(".png"):
            png_files.append(os.path.join(folder_path, file))
    return png_files


def get_file_name(file_path):
    return os.path.basename(file_path)

folder_path = "C:/nerf/skull/processed_depth_nerfacto/"
png_files_list = get_png_files(folder_path)

for png_file in png_files_list:
    file_name = get_file_name(png_file)
    file_name_elems = file_name.split('.')
    file_idx = file_name_elems[0].split('_')[0]
    new_file_name = f"frame_{str(int(file_idx)+1).zfill(5)}_depth.png"
    os.rename(os.path.join(folder_path + file_name), os.path.join(folder_path, new_file_name))
    