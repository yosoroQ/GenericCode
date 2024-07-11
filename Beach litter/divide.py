import os
import random
from shutil import copy2

# 源文件夹路径
file_path = r"C:\Users\one\Desktop\Beach litter\Miracle"

# 新文件路径
new_file_path = r"C:\Users\one\Desktop\Beach litter\Miracle_again"

# 划分数据比例7:2:1
split_rate = [0.7, 0.2, 0.1]
class_names = os.listdir(file_path)  # 数据集文件的名字
print(class_names)  # ['00000.jpg', '00001.jpg', '00002.jpg'... ]

# 判断是否存在目标文件夹，不存在则创建---->创建train\val\test文件夹
if not os.path.exists(new_file_path):
    os.makedirs(new_file_path)

split_names = ['train', 'val', 'test']
for split_name in split_names:
    split_path = os.path.join(new_file_path, split_name)
    if not os.path.exists(split_path):
        os.makedirs(split_path)

# 按照比例划分数据集，并进行数据图片的复制
current_all_data = [f for f in os.listdir(file_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
current_data_length = len(current_all_data)  # 文件夹下的图片个数
current_data_index_list = list(range(current_data_length))
random.shuffle(current_data_index_list)  # 将列表顺序打乱

train_stop_flag = int(current_data_length * split_rate[0])
val_stop_flag = int(current_data_length * (split_rate[0] + split_rate[1]))

train_path = os.path.join(new_file_path, 'train')
val_path = os.path.join(new_file_path, 'val')
test_path = os.path.join(new_file_path, 'test')

current_idx = 0
train_num = 0
val_num = 0
test_num = 0

# 图片复制到文件夹中
for i in current_data_index_list:
    src_img_path = os.path.join(file_path, current_all_data[i])
    if current_idx < train_stop_flag:
        copy2(src_img_path, train_path)
        train_num += 1
    elif train_stop_flag <= current_idx < val_stop_flag:
        copy2(src_img_path, val_path)
        val_num += 1
    else:
        copy2(src_img_path, test_path)
        test_num += 1
    current_idx += 1

print("Done!", train_num, val_num, test_num)
