import os
import glob
import argparse
import cv2
import time
from utils.LACC import LACC
from utils.fusion import fusion

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--type', type=str, default='image', choices=['image', 'img'])
parser.add_argument('-m', '--mode', default='fusion')
parser.add_argument('-d', '--detect', action='store_true')
args = parser.parse_args()

def run():
    if not (args.detect or args.mode): return print("no") 
    
    folder_path = './Input/'
    output_path = './Output/'
    start_time = time.time()

    if args.type in ['img', 'image']:
        image_files = glob.glob(os.path.join(folder_path, '*.png')) + \
                    glob.glob(os.path.join(folder_path, '*.jpg'))
        total_images = len(image_files)
        for img_path in image_files:
            img_start_time = time.time()
            img = cv2.imread(img_path)
            if args.mode == 'fusion':
                img = LACC(img/255.)
                img = fusion(img)*255
            if args.detect:
                img = model(source=img, conf=0.6)
                img = img[0].plot()
            cv2.imwrite(os.path.join(output_path, os.path.basename(img_path)), img)
            print(f'Image {img_path} Done!!!')
            img_end_time = time.time()
            print(f'Image {img_path} processed in {img_end_time - img_start_time:.2f} seconds')

        end_time = time.time()
        total_time = end_time - start_time
        average_time = total_time / total_images if total_images > 0 else 0
        print(f'Total processing time: {total_time:.2f} seconds')
        print(f'Average processing time per image: {average_time:.2f} seconds')

if __name__ == '__main__':
    run()