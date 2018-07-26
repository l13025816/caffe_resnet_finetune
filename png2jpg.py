import os
import cv2
import sys
import numpy as np
    
birdroot = "/home/dy/xuke/niaolei/200bird/bird200/"

dirnames = os.listdir(birdroot)
dirnames = [int(i) for i in dirnames]
dirnames.sort()
dirnames = [str(i) for i in dirnames]
#print(dirnames)
directories = []

for filename in dirnames:
    path = os.path.join(birdroot, filename)

# path = "/home/dy/xuke/niaolei/200bird/200_bird/134/"
# print(path)
     
    for filename in os.listdir(path):
        if os.path.splitext(filename)[1] == '.png':
                # print(filename)
                img = cv2.imread(path + filename)
                print(filename.replace(".png",".jpg"))
                newfilename = filename.replace(".png",".jpg")
                # cv2.imshow("Image",img)
                # cv2.waitKey(0)
                cv2.imwrite(path + newfilename,img)
        elif os.path.splitext(filename)[1] == '.bmp':
                # print(filename)
                img = cv2.imread(path + filename)
                print(filename.replace(".bmp",".jpg"))
                newfilename = filename.replace(".bmp",".jpg")
                # cv2.imshow("Image",img)
                # cv2.waitKey(0)
                cv2.imwrite(path + newfilename,img)
        elif os.path.splitext(filename)[1] == '.gif':
                # print(filename)
                img = cv2.imread(path + filename)
                print(filename.replace(".gif",".jpg"))
                newfilename = filename.replace(".gif",".jpg")
                # cv2.imshow("Image",img)
                # cv2.waitKey(0)
                cv2.imwrite(path + newfilename,img)
