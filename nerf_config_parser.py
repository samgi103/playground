import cv2
import json

root_path = "C:/nerf/skull"
#C:\nerf\skull\processed_depth_nerfacto
with open(f"{root_path}/processed_depth_nerfacto/transforms.json", 'r') as file:
    json_config = json.load(file)

# print(json_config)
frames_list = json_config["frames"]
new_frame_list = []
for frame_info in frames_list:
    file_name = frame_info["file_path"].split('/')[1]
    depth_name = file_name.split('.')[0] + "_depth.png"
    frame_info["depth_file_path"] = f"depth/{depth_name}"
    new_frame_list.append(frame_info)

json_config["frames"] = new_frame_list
with open(f"{root_path}/processed_depth_nerfacto/transforms.json", 'w') as file:
    json.dump(json_config, file, indent=2)

