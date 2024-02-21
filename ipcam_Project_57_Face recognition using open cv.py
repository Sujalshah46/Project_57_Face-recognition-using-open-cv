# Project_57_Face recognition using open cv_BY_EdgeAIHub
import urllib.request
import cv2
# Project_57_Face recognition using open cv_BY_EdgeAIHub
import numpy as np
import imutils
# Project_57_Face recognition using open cv_BY_EdgeAIHub
url='http://192.168.1.6:8080/shot.jpg'
while True:
    imgPath = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgPath.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    img = imutils.resize(img, width=450)
    cv2.imshow("CameraFeed",img)
    if ord('q') ==  cv2.waitKey(1):
        exit(0)
