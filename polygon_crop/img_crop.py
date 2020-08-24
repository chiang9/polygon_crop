from tkinter import *
import PIL
from PIL import Image, ImageTk, ImageDraw
import numpy as np
import sys
import cv2


def img_crop(path, basewidth = 500):
    pp = polygon_select(path)
    newIm = polygon_crop(path, pp)
    return newIm


def polygon_select(path, basewidth = 500):
    cs = list()
    img = cv2.imread(path)
    length, wid, _ = img.shape

    wid_ratio = basewidth/wid
    baselength = int(round(length * wid_ratio))
    # img = img.resize((basewidth, baselength), Image.ANTIALIAS)
    img = cv2.resize(img, dsize=(basewidth, baselength), interpolation=cv2.INTER_CUBIC)

    # mouse callback function
    def draw_circle(event,x,y,flags,param):

        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(img,(x,y),5,(0,0,255),-1)
            cs.append((int(round(x/wid_ratio)), int(round(y/wid_ratio))))
            print("click on x: " + str(x) + " y: " + str(y))


    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_circle)

    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()
    return cs

def polygon_crop(path, polygon):
    img = Image.open(path).convert("RGB")
    img_array = np.asarray(img)

    mask_img = Image.new('1', (img_array.shape[1], img_array.shape[0]), 0)
    ImageDraw.Draw(mask_img).polygon(polygon, outline=1, fill=1)
    mask = np.array(mask_img)

    new_img_array = np.empty(img_array.shape, dtype='uint8')
    new_img_array[:,:,:3] = img_array[:,:,:3]

    new_img_array[:,:,0] = new_img_array[:,:,0] * mask
    new_img_array[:,:,1] = new_img_array[:,:,1] * mask
    new_img_array[:,:,2] = new_img_array[:,:,2] * mask

    # back to Image from numpy
    # newIm = Image.fromarray(new_img_array, "RGB")
    return new_img_array
