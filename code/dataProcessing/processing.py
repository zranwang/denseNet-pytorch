import os
import glob
from PIL import Image
import matplotlib.pylab as plt
import cv2
import numpy as np

number = 350
all_image_path = "./finall_path"
out_path = './finall_path_1'
lable = 0
for root, dirs, flies in os.walk(all_image_path):
    for dir in dirs:
        labeles_path = (os.path.join(root, dir))
        images_file_name = glob.glob(labeles_path+'/*.jpg')
        number_images = len(images_file_name)
        if number_images >= number:
            continue
            for k in range(number):
                image = Image.open(images_file_name[k], 'r')
                # print(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"))
                if not os.path.exists(os.path.join(out_path, dir)):
                    os.mkdir(os.path.join(out_path, dir))
                image.save(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"))
        else:
            for k in range(number_images):
                image = Image.open(images_file_name[k], 'r')
                # print(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"))
                if not os.path.exists(os.path.join(out_path, dir)):
                    os.mkdir(os.path.join(out_path, dir))
                image.save(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"))
            diffs = number - number_images
            k = number_images
            diff = diffs // number_images + 1
            diff_cat = diff // 2 + 1
            print(diff_cat)
            for i in range(number_images):
                if k >= number:
                    break

                # image0 = Image.open(images_file_name[i], 'r')
                image = cv2.imread(images_file_name[i])

                size = image.shape
                # crop

                # image_new = Image.new("RGB", [size[0] + diff_cat, size[1] + diff_cat])

                image_new = cv2.copyMakeBorder(image, diff_cat, diff_cat, diff_cat, diff_cat, cv2.BORDER_CONSTANT, value=0)
                # image_new.show()
                new_size = image_new.shape
                res = diff_cat-1
                print("#####################################crop#######################################")
                for g in range(diff):

                    if res < 0:
                        break
                    if diff > 4 and g >= diff - 4:
                        break

                    image_temp = image_new[res:size[0] + res, res:size[1] + res]
                    print(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"))
                    cv2.imwrite(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"), image_temp)
                    k += 1

                    if diff == 1:
                        break
                    image_temp = image_new[new_size[0] - size[0] - res:new_size[0] - res, res:size[1] + res]
                    print(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"))
                    cv2.imwrite(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"), image_temp)
                    k += 1

                    if diff == 2:
                        break
                    image_temp = image_new[res: size[0] + res, new_size[1] - size[1] - res:new_size[1] - res]
                    print(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"))
                    cv2.imwrite(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"), image_temp)
                    k += 1

                    if diff == 3:
                        break

                    image_temp = image_new[new_size[0] - size[0] - res:new_size[0] - res, new_size[1] - size[1] - res:new_size[1] - res]
                    print(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"))
                    cv2.imwrite(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"), image_temp)
                    k += 1
                    '''
                    image_temp = image_new.crop((res, res, size[0]+res, size[1]+res))
                    plt.save(os.path.join(out_path, str(lable), str(lable) + '_' + str(k) + ".jpg"), image_temp)
                    k += 1

                    image_temp = image_new.crop((image_new.size[0]-size[0]-res, res, image_new.size[0]-res, size[1] + res))
                    plt.save(os.path.join(out_path, str(lable), str(lable) + '_' + str(k) + ".jpg"), image_temp)
                    k += 1

                    image_temp = image_new.crop((res, image_new.size[1]-size[1]-res, size[0] + res, image_new.size[1]-res))
                    plt.save(os.path.join(out_path, str(lable), str(lable) + '_' + str(k) + ".jpg"), image_temp)
                    k += 1

                    image_temp = image_new.crop((image_new.size[0]-size[0]-res, image_new.size[1]-size[1]-res, image_new.size[0]-res, image_new.size[1]-res))
                    plt.save(os.path.join(out_path, str(lable), str(lable) + '_' + str(k) + ".jpg"), image_temp)
                    k += 1
                    '''
                    res -= 1
                print("#########################################dilete###################################")
                # dilite
                if diff == 4:
                    continue
                if k >= number:
                    continue
                image = cv2.imread(images_file_name[i])
                element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
                element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
                dilation = cv2.dilate(image, element2, iterations=1)
                print(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"))
                cv2.imwrite(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"), dilation)
                k += 1
                if diff <= 5:
                    continue
                erosion = cv2.erode(image, element1, iterations=1)
                print(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"))
                cv2.imwrite(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"), erosion)
                k += 1
                if diff <= 6:
                    continue
                binary = cv2.dilate(erosion, element2, iterations=1)
                print(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"))
                cv2.imwrite(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"), binary)
                k += 1
                if diff <= 7:
                    continue
                binary = cv2.erode(dilation, element2, iterations=1)
                print(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"))
                cv2.imwrite(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"), binary)
                k += 1
                #if diff <= 8:
                #   continue
                #binary = cv2.dilate(erosion, element2, iterations=1)
                #print(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"))
                #cv2.imwrite(os.path.join(out_path, dir, dir + '_' + str(k) + ".jpg"), binary)
                #k += 1
