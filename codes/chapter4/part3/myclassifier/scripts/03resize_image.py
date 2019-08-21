import urllib.request
import cv2
import numpy as np
import os

def resize_image():
    img = cv2.imread("object.jpg")
    resized_image = cv2.resize(img, (50, 50))
    cv2.imwrite("object5050.jpg",resized_image)

resize_image()