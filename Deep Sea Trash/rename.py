import os

def rename_files_in_folders(root_dir):
    # 遍历根目录下的所有文件夹
    for folder_name in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder_name)
        
        if os.path.isdir(folder_path):
            # 遍历文件夹中的所有文件
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                
                if os.path.isfile(file_path):
                    # 创建新的文件名
                    new_filename = f"{folder_name}_{filename}"
                    new_file_path = os.path.join(folder_path, new_filename)
                    
                    # 重命名文件
                    os.rename(file_path, new_file_path)
                    print(f"Renamed: {file_path} -> {new_file_path}")

# 指定根目录
root_directory = "/FFOUTPUT"

# 批量重命名文件
rename_files_in_folders(root_directory)
