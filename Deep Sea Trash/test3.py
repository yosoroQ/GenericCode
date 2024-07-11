import os
import glob
from skimage import io, img_as_float
from skimage.metrics import peak_signal_noise_ratio, structural_similarity

def calculate_metrics(original_image_path, enhanced_image_path):
    # 加载原始图像和增强图像
    original = img_as_float(io.imread(original_image_path))
    enhanced = img_as_float(io.imread(enhanced_image_path))
    
    # 检查图像的维度，如果是多通道图像（例如彩色图像）
    if original.ndim == 3 and enhanced.ndim == 3:
        # 设置channel_axis为2（即最后一个维度是颜色通道）
        channel_axis = 2
    else:
        channel_axis = None
    
    # 确定窗口大小，确保窗口大小是一个奇数且不超过图像的最小尺寸
    win_size = min(original.shape[0], original.shape[1], 7)
    if win_size % 2 == 0:
        win_size -= 1
    
    # 计算PSNR
    psnr_value = peak_signal_noise_ratio(original, enhanced, data_range=1.0)
    
    # 计算SSIM
    ssim_value, _ = structural_similarity(original, enhanced, win_size=win_size, channel_axis=channel_axis, full=True, data_range=1.0)
    
    return psnr_value, ssim_value

# 读取文件夹中的所有图像文件
original_folder = './Over'
enhanced_folder = './666'

original_images = sorted(glob.glob(os.path.join(original_folder, '*.png')))
enhanced_images = sorted(glob.glob(os.path.join(enhanced_folder, '*.png')))

# 确保两个文件夹中的图像数量相同
assert len(original_images) == len(enhanced_images), "The number of images in the two folders must be the same."

# 初始化累加器
total_psnr = 0
total_ssim = 0
num_images = len(original_images)

# 计算每对图像的PSNR和SSIM并累加
for original_image_path, enhanced_image_path in zip(original_images, enhanced_images):
    psnr_value, ssim_value = calculate_metrics(original_image_path, enhanced_image_path)
    total_psnr += psnr_value
    total_ssim += ssim_value
    print(f"Image: {os.path.basename(original_image_path)}")
    print(f"PSNR: {psnr_value} dB")
    print(f"SSIM: {ssim_value}")
    print('-' * 30)

# 计算平均值
average_psnr = total_psnr / num_images
average_ssim = total_ssim / num_images

print(f"Average PSNR: {average_psnr} dB")
print(f"Average SSIM: {average_ssim}")
