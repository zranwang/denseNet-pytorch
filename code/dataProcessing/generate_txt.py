import os
import glob

train_dir = './mydata/split-train'
valid_dir = './mydata/split-valid'
train_txt_dir = './mydata/train.txt'
valid_txt_dir = './mydata/valid.txt'


def generate_txt(text_path, image_path):
    f = open(text_path, 'w')
    for root, dirs, files in os.walk(image_path):
        for dir in dirs:
            images_path = os.path.join(root, dir)
            label = dir
            image_list = glob.glob(images_path + '/*.jpg')
            for i in range(len(image_list)):
                line = image_list[i] + " " + label + '\n'
                print(line)
                f.write(line)


if __name__ == '__main__':
    generate_txt(train_txt_dir, train_dir)
    generate_txt(valid_txt_dir, valid_dir)