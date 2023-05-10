import cv2
import numpy as np
from pathlib import Path
import os

def crop_jpg(path_to_jpg:str = None):
    """Function to crop jpg file to remove black edges"""
    filename = Path(path_to_jpg).stem
    parent_dir = Path(path_to_jpg).parents[0]

    # Reading the jpg file
    img = cv2.imread(path_to_jpg)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray,1,255,cv2.THRESH_BINARY)   

    # Getting the contours
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    x,y,w,h = cv2.boundingRect(cnt)

    # Writing the cropped file
    cropped_file = os.path.join(parent_dir, f'{filename}_cropped.jpg')
    crop = img[y:y+h,x:x+w]
    cv2.imwrite(cropped_file,crop)     

if __name__ == "__main__":
    path_to_jpg = '/home/vardh/tmp/planet/stanlow/20230420_111156_17_2402_3B_Visual.jpg'
    crop_jpg(path_to_jpg)

