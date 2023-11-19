import cv2
import json

root_path = "C:/nerf/skull"
#C:\nerf\skull\processed_depth_nerfacto
with open(f"{root_path}/processed_guide_mask/transforms.json", 'r') as file:
    json_config = json.load(file)

# print(json_config)
frames_list = json_config["frames"]
new_frame_list = []
for frame_info in frames_list:
    file_name = frame_info["file_path"].split('/')[1]
    mask_name = file_name.split('.')[0].split('_')[1]
    mask_name = f"{str(int(mask_name)).zfill(3)}.png"
    frame_info["mask_path"] = f"masks/{mask_name}"
    new_frame_list.append(frame_info)

json_config["frames"] = new_frame_list
with open(f"{root_path}/processed_guide_mask/transforms.json", 'w') as file:
    json.dump(json_config, file, indent=2)

