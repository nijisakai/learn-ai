"""
@author: wanqingfeng
"""

#标定
import cv2
import numpy as np
import glob

criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
#标定板尺寸
w = 7#根据实际角点个数，9x7格子，角点就是8x6
h = 5#正确的数目很重要，否则会报错
objp = np.zeros((w*h,3), np.float32)
objp[:,:2] = np.mgrid[0:w, 0:h].T.reshape(-1,2)

obj_points = []
img_points = []

images = glob.glob('calib/*.jpg')#该文件夹下存着刚才采集并筛选过的图片

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    size = gray.shape[::-1]
    ret, corners = cv2.findChessboardCorners(gray,(w,h),None)
    if ret == True:
        cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
        obj_points.append(objp)
        img_points.append(corners)
        
        cv2.drawChessboardCorners(img,(w,h),corners,ret)
        cv2.imshow('findCorners',img)
        cv2.waitKey(0)#每按一次空格开始标定下一张
        
cv2.destroyAllWindows()
#标定
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points,gray.shape[::-1],None,None)

print("ret: \n",ret)
print("mtx: \n",mtx) #内参矩阵
