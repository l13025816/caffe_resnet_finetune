import os
import cv2
import sys
import numpy as np
import random

SPLIT=0.8
birdroot = "/home/dy/xuke/niaolei/200bird/bird200/"
#print(path)
os.system('mkdir train')
os.system('mkdir val')

dirnames = os.listdir(birdroot)
dirnames = [int(i) for i in dirnames]
dirnames.sort()
dirnames = [str(i) for i in dirnames]
print(dirnames)
directories = []

for filename in dirnames:
    path = os.path.join(birdroot, filename)
    #path_train=os.path.join('./train/', filename)
    #path_val=os.path.join('./val/', filename)
    if os.path.isdir(path):
        directories.append(path)
       
       # os.system('mkdir '+path_train)
       # os.system('mkdir '+path_val)

txt_train=open('train.txt','w')
txt_val=open('val.txt','w')

classid=0
trainid=0
valid=0
for directory in directories:
    classid=classid+1
    img_pathes=os.listdir(directory)
    train_num=int(SPLIT*len(img_pathes))
    #print len(img_pathes)
    #val_num=len(img_pathes)-train_num
    random.seed(0)
    random.shuffle(img_pathes)
    training_filenames=img_pathes[:train_num]
    validation_filenames=img_pathes[train_num:]

    
    for filename in training_filenames:
        trainid+=1
        if filename[-4:]!=".jpg":
            print filename

        path = os.path.join(directory, filename)
        path=path.replace(" ","' '")
        path=path.replace("&","'&'")
        path=path.replace("(","'('")
        path=path.replace(")","')'")
        train_path = './train/'+str(trainid)+'.jpg'
        strtmp=train_path+' '+str(classid)+'\n'
        txt_train.writelines(strtmp)
        os.system('cp '+path+' '+train_path)

    
    for filename in validation_filenames:
        valid+=1
        if filename[-4:]!=".jpg":
            print filename
        path = os.path.join(directory, filename)
        path=path.replace(" ","' '")
        path=path.replace("&","'&'")
        path=path.replace("(","'('")
        path=path.replace(")","')'")
        val_path = './val/'+str(valid)+'.jpg'
        strtmp=val_path+' '+str(classid)+'\n'
        txt_val.writelines(strtmp)
        strtmp='cp '+path+' '+val_path
        #print strtmp
        os.system(strtmp)

txt_train.close()
txt_val.close()

#     if os.path.splitext(filename)[1] == '.png':
#             # print(filename)
#             img = cv2.imread(path + filename)
#             print(filename.replace(".png",".jpg"))
#             newfilename = filename.replace(".png",".jpg")
#             # cv2.imshow("Image",img)
#             # cv2.waitKey(0)
#             cv2.imwrite(path + newfilename,img)
#     elif os.path.splitext(filename)[1] == '.bmp':
#             # print(filename)
#             img = cv2.imread(path + filename)
#             print(filename.replace(".bmp",".jpg"))
#             newfilename = filename.replace(".bmp",".jpg")
#             # cv2.imshow("Image",img)
#             # cv2.waitKey(0)
#             cv2.imwrite(path + newfilename,img)
