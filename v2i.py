# import cv2
# import os

# path = './res/'
# out_path = './resVid/'
# out_video_name = 'res.mp4'
# out_video_full_path = out_path + out_video_name

# pre_imgs = os.listdir(path)
# img = []

# for i in pre_imgs: 
#     i = path + i
#     img.append(i)

# cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# frame = cv2.imread(img[0])
# size = list(frame.shape)
# del size[2]
# size.reverse()

# video = cv2.VideoWriter(out_video_full_path, cv2_fourcc, 48, size)

# for i in range(len(img)):
#     video.write(cv2.imread(img[i]))
#     print('fram ', i+1, ' of ', len(img))

# video.release()

import cv2
import numpy as np
import glob

img_array = []
for filename in glob.glob('./res/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 24, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()