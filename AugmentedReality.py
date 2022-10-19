import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

class AugmentedReality():

    def __init__(self):
        self.folderPath = ''
        self.libPath = './Alphabet_lib/'
        self.onboard = cv2.FileStorage(self.libPath+'alphabet_lib_onboard.txt', cv2.FILE_STORAGE_READ)
        self.vertical = cv2.FileStorage(self.libPath+'alphabet_lib_vertical.txt', cv2.FILE_STORAGE_READ)
        self.imgs = []
        self.intrinsicMatrix = None
        self.dist = None
        self.rvecs = None
        self.tvecs = None
        

    def LoadFolder(self, path):
        self.folderPath = path

    def CalculateParameters(self):
        dirs = os.listdir(self.folderPath)
        dirs.sort(key=len)
        patternSize = (11,8)

        # termination criteria
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((patternSize[0]*patternSize[1],3), np.float32)
        objp[:,:2] = np.mgrid[0:patternSize[0],0:patternSize[1]].T.reshape(-1,2)

        # Arrays to store object points and image points from all the images.
        objPoints = []  # 3d point in real world space
        imgPoints = []  # 2d point in image plane

        self.imgs = []     # store the image result

        for fileName in dirs:
            img = cv2.imread(self.folderPath+'/'+fileName)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, corners = cv2.findChessboardCorners(img, patternSize, None)

            if ret == True:
                corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
                objPoints.append(objp)
                imgPoints.append(corners)
                self.imgs.append(img)

        ret, self.intrinsicMatrix, self.dist, self.rvecs, self.tvecs = cv2.calibrateCamera(objPoints, imgPoints, gray.shape[::-1], None, None)

    def ShowWordsOnBoard(self, word):
        self.CalculateParameters()
        if self.imgs == []:
            print('No image!')
            return

        imgsResult = []

        for i in range(len(self.imgs)):
            img = self.imgs[i].copy()
            rvec = self.rvecs[i]
            tvec = self.tvecs[i]
            
            cnt = 0
            for c in word:
                if(c.isalpha()):
                    ch = self.onboard.getNode(c).mat()
                    posX = (cnt % 4) * 3
                    posY = int(cnt / 4) * 3

                    for y in ch:
                        src = np.array(y, np.float)
                        src[0][0] += 9 - posX
                        src[0][1] += 6 - posY
                        src[1][0] += 9 - posX
                        src[1][1] += 6 - posY
                        result = cv2.projectPoints(src, rvec, tvec, self.intrinsicMatrix, None)
                        result = tuple(map(tuple, result[0]))
                        start = tuple(map(int, result[0][0]))
                        end = tuple(map(int, result[1][0]))
                        cv2.line(img, start, end, (255, 0, 0), 10)
                    cnt += 1

            img = cv2.resize(img, (800, 600), interpolation=cv2.INTER_AREA)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgsResult.append(img)
        
        for img in imgsResult:
            cv2.namedWindow('image', 0)
            cv2.resizeWindow('image', 800, 600)
            cv2.imshow('image', img)
            cv2.waitKey(1000)

        cv2.destroyAllWindows()

    def ShowWordsVertically(self, word):
        self.CalculateParameters()
        if self.imgs == []:
            print('No image!')
            return

        imgsResult = []

        for i in range(len(self.imgs)):
            img = self.imgs[i].copy()
            rvec = self.rvecs[i]
            tvec = self.tvecs[i]
            
            cnt = 0
            for c in word:
                if(c.isalpha()):
                    ch = self.vertical.getNode(c).mat()
                    posX = (cnt % 4) * 3
                    posY = int(cnt / 4) * 3

                    for y in ch:
                        src = np.array(y, np.float)
                        src[0][0] += 9 - posX
                        src[0][1] += 6 - posY
                        src[1][0] += 9 - posX
                        src[1][1] += 6 - posY
                        result = cv2.projectPoints(src, rvec, tvec, self.intrinsicMatrix, None)
                        result = tuple(map(tuple, result[0]))
                        start = tuple(map(int, result[0][0]))
                        end = tuple(map(int, result[1][0]))
                        cv2.line(img, start, end, (255, 0, 0), 10)
                    cnt += 1

            img = cv2.resize(img, (800, 600), interpolation=cv2.INTER_AREA)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgsResult.append(img)
        
        for img in imgsResult:
            cv2.namedWindow('image', 0)
            cv2.resizeWindow('image', 800, 600)
            cv2.imshow('image', img)
            cv2.waitKey(1000)

        cv2.destroyAllWindows()



                
                
        

        

        
        


