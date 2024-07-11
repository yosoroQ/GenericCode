# import os
# from PIL import Image, ImageEnhance
# import torchvision.transforms as transforms
# import torchvision.transforms.functional as F

# # 指定源文件夹和目标文件夹
# source_folder = '/root/autodl-tmp/output1080dislodge'
# target_folder = '/home/CropTest/1080Flip'

# # 创建目标文件夹（如果不存在）
# os.makedirs(target_folder, exist_ok=True) 

# # 遍历源文件夹中的所有文件
# for filename in os.listdir(source_folder):
#     if filename.endswith('.jpg') or filename.endswith('.png'):  # 可根据需要添加其他扩展名
#         # 加载图像
#         image_path = os.path.join(source_folder, filename)
#         image = Image.open(image_path)
        
#         # 水平翻转图像
#         flipped_image = F.hflip(image)
        
#         # # 降低对比度
#         # enhancer = ImageEnhance.Contrast(flipped_image)
#         # low_contrast_image = enhancer.enhance(0.5)  # 0.5 表示降低一半对比度，可调整

#         # 提高亮度（模拟过曝效果）
#         enhancer = ImageEnhance.Brightness(flipped_image)
#         overexposed_image = enhancer.enhance(2.0)  # 2.0 表示亮度加倍，可根据需要调整
        
#         # 生成新文件名
#         base, ext = os.path.splitext(filename)
#         new_filename = f"{base}_Flip{ext}"
#         new_image_path = os.path.join(target_folder, new_filename)
        
#         # 保存处理后的图像
#         low_contrast_image.save(new_image_path)
        
#         print(f"Processed and saved: {new_image_path}")
import os
from PIL import Image, ImageEnhance
import torchvision.transforms.functional as F

# 指定源文件夹和目标文件夹
source_folder = '/root/autodl-tmp/output1080dislodge'
target_folder = '/home/CropTest/1080Flip'

# 创建目标文件夹（如果不存在）
os.makedirs(target_folder, exist_ok=True)

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # 可根据需要添加其他扩展名
        # 加载图像
        image_path = os.path.join(source_folder, filename)
        image = Image.open(image_path)
        
        # 水平翻转图像
        flipped_image = F.hflip(image)
        
        # 提高亮度（模拟过曝效果）
        enhancer = ImageEnhance.Brightness(flipped_image)
        overexposed_image = enhancer.enhance(1.5)  # 2.0 表示亮度加倍，可根据需要调整
        
        # 生成新文件名
        base, ext = os.path.splitext(filename)
        new_filename = f"{base}_Flip{ext}"
        new_image_path = os.path.join(target_folder, new_filename)
        
        # 保存处理后的图像
        overexposed_image.save(new_image_path)
        
        print(f"Processed and saved: {new_image_path}")
