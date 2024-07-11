import cv2
import numpy as np

# 计算给定通道的直方图，并返回直方图的标准差，用于衡量通道的色彩分布
def histogram_spread(channel):
    hist, _ = np.histogram(channel, bins=256, range=(0, 1))
    return np.std(hist)

def LACC(input_img: np.ndarray):
    """
    局部自适应色彩校正

    Parameters：
    - img (numpy.ndarray): 一个三通道彩色图像（BGR）。取值范围为 [0, 1]

    Returns：
    - LACC_img (numpy.ndarray): 色彩校正后的图像。取值范围为 [0, 1]
    """

    # 图像通道排序：将图像的均值和各通道分离后进行组合，按均值从小到大排序
    # 得到small、medium和large三个通道的信息（包括均值、通道数据和颜色标记）。
    ## zip [(img_mean, img)], it (b, g, r)
    small, medium, large = sorted(list(zip(cv2.mean(input_img), cv2.split(input_img), ['b', 'g', 'r'])))
    ## sorted by mean (small to large)
    small, medium, large = list(small), list(medium), list(large)
    
    ## 通道交换 (only for images)
    if histogram_spread(medium[1]) < histogram_spread(large[1]) and (large[0] - medium[0]) < 0.07 and small[2] == 'r':
        large, medium = medium, large

    ## 最大衰减计算
    max_attenuation = 1 - (small[1]**1.2)
    max_attenuation = np.expand_dims(max_attenuation, axis=2)

    ## 细节图像计算
    blurred_image = cv2.GaussianBlur(input_img, (7, 7), 0)
    detail_image = input_img - blurred_image
    
    ## 校正最大通道
    large[1] = (large[1] - cv2.minMaxLoc(large[1])[0]) * (1/(cv2.minMaxLoc(large[1])[1] - cv2.minMaxLoc(large[1])[0]))
    large[0] = cv2.mean(large[1])[0]
    
    ## Iter corrected 迭代校正其他通道
    loss = float('inf')
    while loss > 1e-2:
        medium[1] = medium[1] + (large[0] - cv2.mean(medium[1])[0]) * large[1]
        small[1] = small[1] + (large[0] - cv2.mean(small[1])[0]) * large[1]
        loss = abs(large[0] - cv2.mean(medium[1])[0]) + abs(large[0] - cv2.mean(small[1])[0])

    ## b, g, r combine 通道合并
    for _, ch, color in [large, medium, small]:
        if color == 'b':
            b_ch = ch
        elif color == 'g':
            g_ch = ch
        else:
            r_ch = ch
    img_corrected = cv2.merge([b_ch, g_ch, r_ch])
    
    ## LACC Result
    LACC_img = detail_image + (max_attenuation * img_corrected) + ((1 - max_attenuation) * input_img)
    LACC_img = np.clip(LACC_img, 0.0, 1.0) 

    return LACC_img
