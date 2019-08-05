import os
from PIL import Image
from torch.utils.data import Dataset
from scipy.misc import imsave
import numpy as np

class MyDataset(Dataset):
    def __init__(self, txtpath, transform=None, target_transform=None):
        f = open(txtpath, 'r')

        imgs = []
        for line in f:
            line = line.rstrip()
            words = line.split()
            imgs.append((words[0], int(words[1])))
        self.imgs = imgs
        self.transform = transform
        self.target_transform = target_transform

    def __getitem__(self, item):

        fn, label = self.imgs[item]
        image = Image.open(fn).convert('RGB')

        if self.transform is not None:
            image = self.transform(image)
        # image = image.permute((1, 2, 0))
        # print(image.shape)

        return image, label

    def __len__(self):

        return len(self.imgs)