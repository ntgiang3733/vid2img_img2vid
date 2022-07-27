# import cv2
# vidcap = cv2.VideoCapture('4.mp4')
# success, image = vidcap.read()
# count = 0
# success = True
# while success:
#     cv2.imwrite("./res/frame%d.jpg" % count, image)
#     success, image = vidcap.read()
#     print('Read a new frame %d: ' % count, success)
#     count += 1

import cv2
import math
import numpy as np

cap = cv2.VideoCapture('4.mp4')
frameRate = cap.get(5)
x = 1
while(cap.isOpened()):
    frameId = cap.get(1)
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % 0.2 == 0):
        print(x)
        filename = './res/img' + str(int(x)) + '.jpg'
        x += 1
        cv2.imwrite(filename, frame)

cap.release()