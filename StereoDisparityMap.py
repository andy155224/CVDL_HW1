import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

class StereoDisparityMap():

    def __init__(self):
        self.imgLPath = ''
        self.imgRPath = ''

    def SetImgPath(self, path, mode):
        if mode == 0:
            self.imgLPath = path
        else:
            self.imgRPath = path
    
    def Execute(self):
        if self.imgLPath == '' or self.imgRPath == '':
            print('ImageL or ImageR lost!')
            return

        imgL = cv2.imread(self.imgLPath)
        imgR = cv2.imread(self.imgRPath)
        imgL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
        imgR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

        stereo = cv2.StereoBM_create(numDisparities=256, blockSize=25)
        img = stereo.compute(imgL, imgR)
        img = cv2.normalize(img, img, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        
        img = cv2.resize(img, (800, 600), interpolation=cv2.INTER_AREA)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

        cv2.namedWindow('image', 0)
        cv2.resizeWindow('image', 800, 600)
        cv2.imshow('image', img)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()

        self.check()

    def check(self):
        if self.imgLPath == '' or self.imgRPath == '':
            print('ImageL or ImageR lost!')
            return
        
        imgL = cv2.imread(self.imgLPath)
        imgR = cv2.imread(self.imgRPath)

        stereo = cv2.StereoBM_create(numDisparities=256, blockSize=25)

        imgLGray = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
        imgRGray = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)
        disp  = stereo.compute(imgLGray, imgRGray)
        disp = cv2.normalize(disp, disp, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

        imgL = cv2.resize(imgL, (800, 600), interpolation=cv2.INTER_AREA)
        imgR = cv2.resize(imgR, (800, 600), interpolation=cv2.INTER_AREA)

        def OnMouseAction(event,x,y,flags,param):
            if event == cv2.EVENT_LBUTTONDOWN:
                dist = int(disp[y][x] / 4)
                img = imgR.copy()
                img = cv2.circle(img, (x - dist, y), 5, (0, 255, 0), 10)
                cv2.imshow('imgR_dot', img)

        cv2.namedWindow('imgL', 0)
        cv2.resizeWindow('imgL', 800, 600)
        cv2.setMouseCallback('imgL',OnMouseAction)
        cv2.imshow('imgL', imgL)
        cv2.namedWindow('imgR_dot', 0)
        cv2.resizeWindow('imgR_dot', 800, 600)
        cv2.imshow('imgR_dot', imgR)

        k = cv2.waitKey()
        cv2.destroyAllWindows()




        
        







        
    