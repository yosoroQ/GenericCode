import os
from PIL import Image
import torch
from torchvision import transforms
import matplotlib.pyplot as plt

# 定义图像处理变换，使用较小的调整因子
transform = transforms.ColorJitter(
    brightness=0.1,   # 较小的亮度调整因子
    contrast=0.1,     # 较小的对比度调整因子
    saturation=0.1,   # 较小的饱和度调整因子
    hue=0.05          # 较小的色调调整因子（取值范围在[-0.5, 0.5]之间）
)

# 输入和输出文件夹路径
input_folder = '/home/output1080'
output_folder = '/home/output108000000_color'

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 处理每个图像
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        # 加载图像
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)
        
        # 应用变换
        transformed_image = transform(image)
        
        # 修改文件名，添加前缀“color”
        new_filename = f"color_{filename}"
        output_path = os.path.join(output_folder, new_filename)
        
        # 保存处理后的图像
        transformed_image.save(output_path)

        # 打印已处理的文件名
        print(f'Processed and saved: {output_path}')

        # 显示原始图像和处理后的图像以进行比较
        fig, ax = plt.subplots(1, 2, figsize=(12, 6))
        ax[0].imshow(image)
        ax[0].set_title('Original Image')
        ax[0].axis('off')

        ax[1].imshow(transformed_image)
        ax[1].set_title('Transformed Image')
        ax[1].axis('off')

        plt.show()
