import os
import matplotlib.pyplot as plt
import cv2
import numpy as np

gray_img_dir = "./reconstruct/256badge1/5"
color_save_dir = "./reconstruct/256badge1/5/colored_results"
cmap = "hot"

if not os.path.exists(gray_img_dir):
    exit()

os.makedirs(color_save_dir, exist_ok=True)
img_suffix = (".bmp",)
img_count = 0

for img_name in os.listdir(gray_img_dir):
    if not img_name.lower().endswith(img_suffix):
        continue
    gray_img_path = os.path.join(gray_img_dir, img_name)
    gray_img = cv2.imread(gray_img_path, cv2.IMREAD_GRAYSCALE)
    if gray_img is None:
        continue
    gray_img = (gray_img - gray_img.min()) / (gray_img.max() - gray_img.min())
    color_img_name = f"color_{img_name}"
    color_img_path = os.path.join(color_save_dir, color_img_name)
    plt.imsave(color_img_path, gray_img, cmap=cmap, vmin=0, vmax=1)
    plt.close()
    img_count += 1
