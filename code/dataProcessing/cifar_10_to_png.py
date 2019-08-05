from scipy.misc import imsave
import numpy as np
import os
import pickle
# from PIL import Image

data_dir = os.path.join('..', '..', 'data\\cifar-10-batches-py')
train_o_dir = os.path.join('..', '..', 'data\\cifar-10-png\\raw-train')
test_o_dir = os.path.join('..', '..', 'data\\cifar-10-png\\raw-test')

for j in range(1, 6):
    data_file_name = os.path.join(data_dir, 'data_batch_' + str(j))
    train_data = {}
    with open(data_file_name, 'rb') as of:
        train_data = pickle.load(of, encoding='bytes')
    for i in range(0, 10000):
        image_data = train_data[b'data'][i]
        image = np.reshape(image_data, (3, 32, 32))
        image = image.transpose((1, 2, 0))
        label = train_data[b'labels'][i]
        image_filename = str(label) + '_' + str(i + (j-1)*10000) + '.png'
        o_dir = os.path.join(train_o_dir, str(label))
        if not os.path.isdir(o_dir):
            os.makedirs(o_dir)
        image_path = os.path.join(o_dir, image_filename)
        # print(image_path)
        imsave(image_path, image)

data_file_name = os.path.join(data_dir, 'test_batch')
test_data = {}
with open(data_file_name, 'rb') as of:
    test_data = pickle.load(of, encoding='bytes')
for i in range(0, 10000):
    image_data = test_data[b'data'][i]
    image = np.reshape(image_data, (3, 32, 32))
    image = image.transpose((1, 2, 0))
    label = test_data[b'labels'][i]
    image_filename = str(label) + '_' + str(i) + '.png'
    o_dir = os.path.join(test_o_dir, str(label))
    if not os.path.isdir(o_dir):
        os.makedirs(o_dir)
    image_path = os.path.join(o_dir, image_filename)
    # print(image_path)
    imsave(image_path, image)