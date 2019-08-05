import os
import glob
from PIL import Image
import matplotlib.pylab as plt
import cv2
import numpy as np

number = 350
all_image_path = "mydata/split-train"
out_path = 'mydata/split-train'
lable = 0
diff_cat = 10
for root, dirs, flies in os.walk(all_image_path):
    print(dirs)
    for dir in dirs:
        labeles_path = (os.path.join(root, dir))
        images_file_name = glob.glob(labeles_path+'/*.jpg')
        number_images = len(images_file_name)
        for k in range(number_images):
            image = cv2.imread(images_file_name[k])
            size = image.shape
            image_new = cv2.copyMakeBorder(image, diff_cat, diff_cat, diff_cat, diff_cat, cv2.BORDER_CONSTANT, value=0)
            print(images_file_name[k])
            cv2.imwrite(images_file_name[k], image_new)

all_image_path = "./mydata/split-valid"
out_path = './mydata/split-valid'
lable = 0
diff_cat = 10
for root, dirs, flies in os.walk(all_image_path):
    print(dirs)
    for dir in dirs:
        labeles_path = (os.path.join(root, dir))
        images_file_name = glob.glob(labeles_path+'/*.jpg')
        number_images = len(images_file_name)
        for k in range(number_images):
            image = cv2.imread(images_file_name[k])
            size = image.shape
            image_new = cv2.copyMakeBorder(image, diff_cat, diff_cat, diff_cat, diff_cat, cv2.BORDER_CONSTANT, value=0)
            print(images_file_name[k])
            cv2.imwrite(images_file_name[k], image_new)