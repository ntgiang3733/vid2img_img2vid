import cv2
vidcap = cv2.VideoCapture('4.mp4')
success, image = vidcap.read()
count = 0
success = True
while success:
    cv2.imwrite("./res/frame%d.jpg" % count, image)
    success, image = vidcap.read()
    print('Read a new frame %d: ' % count, success)
    count += 1