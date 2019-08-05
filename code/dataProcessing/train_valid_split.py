import os
import glob
import random
import shutil
from scipy.misc import imsave
train_dir = '../../mydata/finall_path_1'
train_o_dir = '../../mydata/split-train'
valid_o_dir = '../../mydata/split-valid'
train_per = 0.9
valid_per = 0.1
for root, dirs, files in os.walk(train_dir):
    for dir in dirs:
        # print(dir)
        image_flies = glob.glob(os.path.join(root, dir)+'/*.jpg')
        random.seed(666)
        random.shuffle(image_flies)
        train_num = len(image_flies)*train_per
        for i in range(len(image_flies)):
            o_file = ''
            image_name = os.path.split(image_flies[i])[-1]
            if i<train_num:
                o_file = train_o_dir + '/' + dir + '/'
            else:
                o_file = valid_o_dir + '/' + dir + '/'
            if not os.path.isdir(o_file):
                os.makedirs(o_file)
            out_path = o_file + os.path.split(image_flies[i])[-1]
            # print(out_path)
            shutil.copy(image_flies[i], out_path)