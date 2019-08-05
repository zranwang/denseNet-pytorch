import os
import glob
from PIL import Image
import matplotlib.pylab as plt
import cv2
import numpy as np

number = 350
all_image_path = "./allData"
out_path = './finall_path'
lable = 0
for root, dirs, flies in os.walk(all_image_path):
    for dir in dirs:
        labeles_path = (os.path.join(root, dir))
        images_file_name = glob.glob(labeles_path+'/*.jpg')
        number_images = len(images_file_name)
        for k in range(number_images):
            image = Image.open(images_file_name[k], 'r')
            # print(os.path.join(out_path,dir, dir + '_' + str(k) + ".jpg"))
            if not os.path.exists(os.path.join(out_path, dir)):
                os.mkdir(os.path.join(out_path, dir))
            image.save(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"))