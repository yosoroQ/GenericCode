import os
import torch
from torchvision import transforms
from PIL import Image

def crop_image_to_patches(image, patch_size=(1080, 1080)):
    """
    Crop a 4K image into multiple 720P patches.

    Args:
        image (PIL.Image): The 4K image.
        patch_size (tuple): Size of the patches (height, width).

    Returns:
        List of PIL Image patches.
    """
    width, height = image.size

    # # Check if the image is 4K resolution
    # if width < 3840 or height < 2160:
    #     raise ValueError("The input image must be of at least 4K resolution (3840x2160).")

    patches = []

    # Calculate the number of patches in both dimensions
    num_patches_x = width // patch_size[1]
    num_patches_y = height // patch_size[0]

    for i in range(num_patches_y):
        for j in range(num_patches_x):
            left = j * patch_size[1]
            upper = i * patch_size[0]
            right = left + patch_size[1]
            lower = upper + patch_size[0]
            patch = image.crop((left, upper, right, lower))
            patches.append(patch)

    return patches

def process_folder(folder_path, output_folder):
    """
    Process all 4K images in a folder and crop them into 720P patches.

    Args:
        folder_path (str): Path to the folder containing 4K images.
        output_folder (str): Path to the folder to save the 720P patches.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)

            try:
                patches = crop_image_to_patches(image)

                for idx, patch in enumerate(patches):
                    patch_filename = f'{os.path.splitext(filename)[0]}_patch_{idx}.jpg'
                    patch.save(os.path.join(output_folder, patch_filename))

            except ValueError as e:
                print(f"Skipping {filename}: {e}")

# Example usage
folder_path = '/root/autodl-tmp/#U2466#U5b9d#U94a2#U6e5b#U6c5f#U94a2#U94c1#U5382#U4e1c#U751f#U6d3b#U533a#U70b9#U4f4d2'
output_folder = '/home/output3'
process_folder(folder_path, output_folder)
