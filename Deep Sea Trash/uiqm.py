import os
import glob
import numpy as np
from skimage import io, img_as_float
from skimage.color import rgb2lab
from scipy.ndimage import sobel

def calculate_uicm(image):
    lab_image = rgb2lab(image)
    L, a, b = lab_image[:,:,0], lab_image[:,:,1], lab_image[:,:,2]
    uicm = np.std(a) + np.std(b)
    return uicm

def calculate_uis(image):
    dx = sobel(image, axis=0)
    dy = sobel(image, axis=1)
    grad_magnitude = np.sqrt(dx**2 + dy**2)
    uism = np.mean(grad_magnitude)
    return uism

def calculate_uiconm(image):
    L = image[:,:,0]
    mean_L = np.mean(L)
    uiconm = np.std(L - mean_L)
    return uiconm

def calculate_uiqm(image):
    uicm = calculate_uicm(image)
    uism = calculate_uis(image)
    uiconm = calculate_uiconm(image)
    uiqm = 0.028 * uicm + 0.295 * uism + 3.575 * uiconm
    return uiqm

# 批量处理图像文件并计算平均 UIQM
def process_images(folder_path):
    image_files = glob.glob(os.path.join(folder_path, '*.png')) + \
                  glob.glob(os.path.join(folder_path, '*.jpg'))

    total_uiqm = 0
    num_images = len(image_files)

    for image_path in image_files:
        image = img_as_float(io.imread(image_path))
        uiqm = calculate_uiqm(image)
        total_uiqm += uiqm
        print(f"Image: {os.path.basename(image_path)} UIQM: {uiqm}")

    average_uiqm = total_uiqm / num_images if num_images > 0 else 0
    print(f"Average UIQM: {average_uiqm}")

# 设置图像文件夹路径
folder_path = './666'
process_images(folder_path)
