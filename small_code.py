import cv2
mask_raw = cv2.imread("C:/nerf/skull/guide_mask_images/mask_raw/000.png")
mask = cv2.imread("C:/nerf/skull/guide_mask_images/mask/000.png")

print(mask_raw.shape)
print(mask.shape)