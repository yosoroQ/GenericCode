import os
import torch
from PIL import Image
import torchvision.transforms.functional as F
from concurrent.futures import ThreadPoolExecutor

def random_crop_and_save(image, filename, output_folder, crop_size, num_crops):
    width, height = image.size
    for i in range(num_crops):
        top = torch.randint(0, height - crop_size[1] + 1, (1,)).item()
        left = torch.randint(0, width - crop_size[0] + 1, (1,)).item()
        cropped_image = F.crop(image, top, left, crop_size[1], crop_size[0])
        output_filename = f'{os.path.splitext(filename)[0]}_random_{i+1}{os.path.splitext(filename)[1]}'
        output_path = os.path.join(output_folder, output_filename)
        cropped_image.save(output_path)
        print(f'Processed and saved: {output_path}')

def process_image(file_tuple, output_folder, crop_size, num_crops):
    image_path, filename = file_tuple
    image = Image.open(image_path).convert('RGB')
    random_crop_and_save(image, filename, output_folder, crop_size, num_crops)

def process_images(input_folder, output_folder, crop_size, num_crops, num_workers):
    os.makedirs(output_folder, exist_ok=True)
    file_list = [(os.path.join(input_folder, filename), filename) for filename in os.listdir(input_folder) if filename.endswith(('.jpg', '.jpeg', '.JPG', '.png'))]

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        for file_tuple in file_list:
            executor.submit(process_image, file_tuple, output_folder, crop_size, num_crops)

# 参数设置
input_folder = '/home/CropTest/beach'
output_folder = '/home/output1080Random'
crop_size = (1080, 1080)
num_crops = 4
num_workers = 8  # 使用的并行工作线程数

# 运行裁剪和保存函数
process_images(input_folder, output_folder, crop_size, num_crops, num_workers)
