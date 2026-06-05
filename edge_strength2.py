import os
import cv2
import numpy as np

# 目标文件夹绝对路径
IMG_DIR_ABS = ""
# 指定计算的9张图编号
target_numbers = {0, 149, 299, 399, 999, 1099, 1499, 1699, 1999}

# 提取文件名中的数字用于排序
def get_img_number(img_name):
    return int(''.join(filter(str.isdigit, img_name)))

# 计算边缘强度（Sobel算子，返回均值）
def calculate_edge_strength(img):
    # Sobel算子计算x、y方向梯度
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    # 计算梯度幅值（边缘强度）
    edge_strength = np.sqrt(sobel_x**2 + sobel_y**2)
    # 返回均值（代表整张图的边缘强度）
    return np.mean(edge_strength)

# 筛选bmp文件并按编号升序排列
img_files = [f for f in os.listdir(IMG_DIR_ABS) if f.lower().endswith('.bmp')]
img_files_sorted = sorted(img_files, key=get_img_number)

# 存储边缘强度结果
edge_strength_results = []

# 遍历计算边缘强度
for img_name in img_files_sorted:
    img_num = get_img_number(img_name)
    if img_num not in target_numbers:
        continue
    
    img_path = os.path.join(IMG_DIR_ABS, img_name)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"警告：{img_name} 读取失败，跳过")
        continue
    
    # 计算边缘强度
    edge_val = calculate_edge_strength(img)
    edge_val_rounded = round(edge_val, 4)  # 保留4位小数
    edge_strength_results.append(edge_val_rounded)
    
    # 输出单张图片结果
    print(f"图片 {img_name}：")
    print(f"  边缘强度均值：{edge_val_rounded}\n")

