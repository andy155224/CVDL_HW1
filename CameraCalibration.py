import cv2
import os
import numpy as np

class CameraCalibration():

    def __init__(self):
        self.folderPath = ''
        pass
    
    def LoadFolder(self, path):
        self.folderPath = path
        print(self.folderPath)

    def FindCorners(self):
        dirs = os.listdir(self.folderPath)
        patternSize = (11,8)

        # termination criteria
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((patternSize[0]*patternSize[1],3), np.float32)
        objp[:,:2] = np.mgrid[0:patternSize[0],0:patternSize[1]].T.reshape(-1,2)

        
        # Arrays to store object points and image points from all the images.
        objPoints = []  # 3d point in real world space
        imgPoints = []  # 2d point in image plane

        result = []     # store the image result

        for fileName in dirs:
            img = cv2.imread(self.folderPath+'/'+fileName)
            img = cv2.resize(img, (800,600), interpolation=cv2.INTER_AREA)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, corners = cv2.findChessboardCorners(img, patternSize, None)

            if ret == True:
                corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
                objPoints.append(objp)
                imgPoints.append(corners)
                cv2.drawChessboardCorners(img, patternSize, corners2, ret)    #draw corner point on the original image
                result.append(img)

        for img in result:
            cv2.namedWindow('image', 0)
            cv2.resizeWindow('image', 800, 600)
            cv2.imshow('image', img)
            cv2.waitKey(500)

        cv2.destroyAllWindows()

        ret, self.mtx, self.dist, self.rvecs, self.tvecs = cv2.calibrateCamera(objPoints, imgPoints, gray.shape[::-1], None, None)
    
    def FindIntrinsic(self):
        
        pass


# reference
# 1.https://blog.csdn.net/u010128736/article/details/52875137
# 2.https://docs.opencv.org/3.4/dc/dbb/tutorial_py_calibration.html
