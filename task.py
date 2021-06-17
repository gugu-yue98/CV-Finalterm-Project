import cv2
import numpy as np
import os

root = "D:/test3"
paths = sorted(os.listdir("D:/test3"))
for i in paths:
    path = os.path.join(root, i)
    img=cv2.imread(path)
    #cv2.imshow('img',img)
    #灰度化
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #输出图像大小，方便根据图像大小调节minRadius和maxRadius
    print(img.shape)
    #霍夫变换圆检测
    circles= cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,500,param1=100,param2=100,minRadius=20,maxRadius=80)
    #输出返回值，方便查看类型
    print(circles)
    #输出检测到圆的个数
    print(len(circles[0]))

    print('-------------我是条分割线-----------------')
    #根据检测到圆的信息，画出每一个圆
    for circle in circles[0]:
        #圆的基本信息
        print(circle[2])
        #坐标行列
        x=int(circle[0])
        y=int(circle[1])
        #半径
        r=int(circle[2])
        #在原图用指定颜色标记出圆的位置
        img=cv2.circle(img,(x,y),r,(0,0,255),-1)
    #显示新图像
    #cv2.imshow('res',img)
    cv2.imwrite(path[:-4]+'.png', img)

